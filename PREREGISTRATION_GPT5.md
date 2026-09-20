# GPT-5 follow-up comparison

Frozen before new inference. This supplements, and does not change, the original
PREREGISTRATION.md. The previous Jev and GPT-4.1-mini outcomes are already known,
so this is a follow-up comparison on reused cases, not a fresh blind replication.

- Reuse all 1,000 sampled items, their 500 tune / 500 evaluate assignment, criteria
  order, prompt text, and original Jev responses from
  data/cascade-20260920T132403-7f53cfef. Record source hashes and preserve originals.
- Run the new comparator only: OpenAI gpt-5-2025-08-07, Chat Completions,
  reasoning_effort=medium, max_completion_tokens=4096, no temperature override.
  Reasoning and visible output share this cap. Preserve the original bare-label
  prompt; no examples, answer repairs, label remapping or outcome-driven retries.
- One synthetic, non-dataset smoke call checks model access and response format.
  If it fails, stop and report the issue before changing the protocol.
- Use four concurrent calls, each with an independent append-only attempt journal.
  Transport retries transient HTTP errors at most five times as before. Preserve
  failures, usage, finish reasons, reasoning tokens and every attempt.
- Collect all tune predictions first; freeze the lowest parity threshold and peak
  threshold (tie: lowest) using the unchanged 0.00..1.00 grid, strict confidence
  less than tau escalation. Save selection before any evaluate API request.
- Report all 500 evaluate outcomes. Valid HTTP responses with non-label answers or
  truncation count as wrong. Missing responses/usage or version mismatch invalidate
  a complete cost/quality claim; stop on access/version errors.
- Use per-item fallback correctness and actual per-item input, cached-input and
  output usage. Reasoning tokens are included in completion tokens, not added twice.
  GPT-5 USD per million tokens: input 1.25, cached input 0.125, output 10.
  Jev keeps the original 0.042 input price. Report observed-cache economics;
  hypothetical production cache hit rates may differ.
- Report standalone accuracy and cost separately from cascade savings at the
  tune-selected threshold. State held-out parity failure if it occurs. Empirical
  parity is not a statistical non-inferiority result. Report tune results too.
- Reuse the documented rounded-probability parser correction without changing raw
  Jev rows. Analysis remains descriptive. Latencies combine historical sequential
  Jev calls and new concurrent GPT-5 calls; simulated cascade latency is not a
  contemporaneous or production end-to-end benchmark.
- Do not rerun Study A: changing the LLM comparator cannot alter its Jev-only tests.
- Budget: 1,000 new study calls and one smoke. Completion cap permits up to about
  USD 41 in output charges if all calls exhaust it, plus input and transient retry
  charges. Actual usage is reported. No batch discount is assumed.

Sources verified 2026-09-20:
https://developers.openai.com/api/docs/models/gpt-5
https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create
