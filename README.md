# Jev vs. GPT-5

**The frozen cascade missed its evaluation accuracy target:** 430/500 correct, versus GPT-5's 432/500. Its observed API cost was 47.34% lower. This is not demonstrated equal-quality savings. An earlier naming experiment failed its controls; its intended attribution claim is not supported.

## Read the article

[**Jev vs. GPT-5**](article/ARTICLE.md)

This public release includes the fixed 1,000-item Banking77 sample, sanitized response records, exact request examples, code, figures, protocols, and computed results for the GPT-5 follow-up. It is a descriptive comparison on reused cases, not a production benchmark.

| Evaluation method | Correct / 500 | Cost / million equivalent requests |
|---|---:|---:|
| Jev | 416 | $70.88 |
| GPT-5 | 432 | $2,246.57 |
| Jev → GPT-5 | 430 | $1,183.05 |

## Reproduce offline

Python 3.9+; standard library only. No credentials, network calls, or packages required.

```bash
python3 article/reproduce.py
```

The script derives tuning selection, accuracy and costs from the published response fields and checks the saved result. [Verified output](article/reproduced_metrics.json).

- [Per-item scoring](article/reproduce.py#L8-L20)
- [Usage-based billing](article/reproduce.py#L39-L47)
- [Threshold selection](article/reproduce.py#L53-L60)
- [Complete request and response examples](article/examples/)
- [Formal protocols](PREREGISTRATION.md) and [GPT-5 follow-up](PREREGISTRATION_GPT5.md)
- [Computed results](results/cascade-20260920T135930-b9ae3c81/summary.json)
- [Public release scope](PUBLIC_RELEASE.md), [security review](SECURITY_REVIEW.md), [dataset attribution](DATA_LICENSE.md)

The original protocol contains historical task-scope instructions. It is preserved as a frozen scientific record. This later public release does not change its thresholds or verdicts.

## Licenses

Code: MIT. Original article text and figures: CC BY 4.0, attribution to saurabhkumar8112. Banking77 text and annotations: CC BY 4.0 with attribution to PolyAI and the dataset authors; see DATA_LICENSE.md. Recorded model outputs are measurements, not model weights or proprietary implementation code. These licenses do not grant rights to third-party trademarks or APIs.
