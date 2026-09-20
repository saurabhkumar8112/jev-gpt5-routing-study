"""Recompute the GPT-5 follow-up from raw saved API bodies. No network access."""
import argparse
import json
from pathlib import Path


def evaluate(rows, tau):
    n = len(rows)
    escalated = [r for r in rows if r['confidence'] < tau]
    correct = sum(r['gpt_correct'] if r['confidence'] < tau else r['jev_correct'] for r in rows)
    cost = sum(r['jev_cost'] for r in rows) + sum(r['gpt_cost'] for r in escalated)
    baseline = sum(r['gpt_cost'] for r in rows)
    return dict(tau=tau, n=n, correct=correct, accuracy=correct/n,
                gpt_correct=sum(r['gpt_correct'] for r in rows),
                escalated=len(escalated), cost_per_million=cost/n*1e6,
                gpt_cost_per_million=baseline/n*1e6, savings_multiple=baseline/cost,
                parity_met=correct >= sum(r['gpt_correct'] for r in rows))


def main(root):
    run = root/'data/cascade-20260920T135930-b9ae3c81'
    items = json.loads((run/'items.json').read_text())
    bodies = {}
    for line in (run/'attempts.jsonl').read_text().splitlines():
        a = json.loads(line)
        assert a['status'] == 200 and not a['error'], 'Review failed attempts explicitly'
        assert a['call_id'] not in bodies, 'Review retries explicitly'
        bodies[a['call_id']] = json.loads(a['response_raw'])
    rows = []
    for item in items:
        j = bodies[item['item_id']+':jev']
        g = bodies[item['item_id']+':llm']
        assert j['model'] == 'jev-1.13.0'
        assert g['model'] == 'gpt-5-2025-08-07'
        answer = j['answers']['decision']
        completion = g['choices'][0]
        assert completion['finish_reason'] == 'stop'
        usage = g['usage']
        cached = usage['prompt_tokens_details']['cached_tokens']
        # completion_tokens already includes reasoning_tokens.
        cost = ((usage['prompt_tokens']-cached)*1.25 + cached*.125
                + usage['completion_tokens']*10)/1e6
        rows.append(dict(split=item['split'], confidence=answer['confidence'],
            jev_correct=int(answer['choice']==item['gold']),
            gpt_correct=int(completion['message']['content'].strip()==item['gold']),
            jev_cost=j['usage']['input_tokens']*.042/1e6, gpt_cost=cost))
    tune = [r for r in rows if r['split']=='tune']
    test = [r for r in rows if r['split']=='evaluate']
    assert len(tune)==len(test)==500
    grid = [evaluate(tune,i/100) for i in range(101)]
    selected = next((r['tau'] for r in grid if r['parity_met']),None)
    frozen = json.loads((run/'tune_selection.json').read_text())['thresholds']['parity']
    assert selected == frozen
    result = dict(selected_on_tune=selected,
        tune=evaluate(tune,selected) if selected is not None else None,
        evaluate=evaluate(test,selected) if selected is not None else None,
        jev_evaluate_correct=sum(r['jev_correct'] for r in test),
        jev_cost_per_million=sum(r['jev_cost'] for r in test)/500*1e6)
    expected = json.loads((root/'results/cascade-20260920T135930-b9ae3c81/comparison.json').read_text())
    assert result['evaluate']['correct']==430
    assert abs(result['evaluate']['cost_per_million']-expected['parity']['cost_per_case']*1e6)<1e-8
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    main(parser.parse_args().root)
