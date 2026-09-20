# Source checks and implementation decisions

Checked 2026-09-20 before collection.

- TypeSafe endpoint and response structure: https://docs.typesafe.ai/introduction/quickstart
- TypeSafe confidence meaning: https://docs.typesafe.ai/confidence
  It is a statistic of distribution shape. The interactive example uses an
  approximation, not a published definition of the endpoint's exact statistic.
- TypeSafe price: https://typesafe.ai/ states $42 per billion input tokens,
  equivalent to $0.042 per million. Output-free pricing follows the handoff;
  no output charge is included in this study.
- OpenAI model, snapshot, pricing, Chat Completions support:
  https://developers.openai.com/api/docs/models/gpt-4.1-mini
  Snapshot gpt-4.1-mini-2025-04-14. $0.40 input, $0.10 cached input,
  $1.60 output, per million tokens. No reasoning step.
- Anthropic optional Haiku pricing: https://www.anthropic.com/claude/haiku
  $1 input and $5 output per million. Other handoff Anthropic model prices
  are NOT treated as verified defaults.
- Dataset: https://huggingface.co/datasets/PolyAI/banking77
  Dataset revision and fingerprint are recorded when downloaded.

## User-authorized comparator change, before data

The user requested OpenAI instead of Anthropic on 2026-09-20. The first measured
comparison therefore uses the pinned GPT-4.1 mini snapshot. It is a modest-cost,
non-reasoning instruction-following model compatible with the 32-output-token
closed-label task. This is not a claim that it is the latest or optimal model.
No inference about Haiku economics is made from an OpenAI comparison. The
protocol already permits OpenAI-compatible providers and external verified prices.
No outcome-dependent comparator selection is performed.

## Interpretive corrections

C5 uses its swap control and can support a narrow result despite C2 failure;
C0 failure or the length-control kill still prevents publication. C6 is named
multiclass sensitivity: its TVD threshold does not test growth with class count.
No thresholds from the supplied C0-C7 rules have been relaxed.

The revised handoff says v1 omitted Jev's cost during escalation. V1's written
formula actually included it. The real correction is replacing subset-wide mean
LLM cost/accuracy with per-item outcomes and usage. The code pays Jev on every case.

Repeated identical prompts might be deterministic or cached. Min-max ranges
summarize repeatability only, not independent-sampling confidence intervals.
No claims about all routers follow from one mailbox state. A naming intervention
can identify an identifier effect, but does not prove that meaning is the only
mechanism: string and token-shape residuals remain possible.

## GPT-5 follow-up, 2026-09-20

User requested a stronger comparator, naming GPT-5. Frozen settings and scope:
[follow-up protocol](../PREREGISTRATION_GPT5.md), protocol commit `514e8ff`.
Pinned `gpt-5-2025-08-07`, medium reasoning, `max_completion_tokens=4096`.
The original prompt and cases are unchanged. GPT-4.1-mini evidence stays intact.

Official OpenAI documentation:
- https://developers.openai.com/api/docs/models/gpt-5
- https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create

USD per million tokens: input 1.25, cached input 0.125, output 10.
The completion cap covers reasoning and visible output together. Recorded
`completion_tokens` already includes reasoning, so costs do not add it twice.
The synthetic smoke call verified access to the exact pinned model before study
collection. All new study calls use concurrency four; reused Jev calls were
sequential and noncontemporaneous. Raw cost ratios are distinct from savings at
matched observed quality. Observed caching is not a production cache guarantee.
