# Jev study preregistration v2

Preregistration commit: 681b6030ef53767aea28a98fe90144a676b9ce6b

Date: 2026-09-20. Written before collection. Frozen after first API run.
The next commit fills only the hash above. This document is the authoritative
merged protocol; historical handoffs are retained separately.

## Scope and limitations

Study A tests identifier sensitivity in one fixed mailbox routing state, not
population-wide robustness. Study B tests a confidence-gated cascade on banking77.
No article or vendor message is authorized by this implementation task.
No claim of first publication, universal naming bias, or externally established
ladder correctness follows from these experiments. No confidence floor is assumed.

## Study A design

Pinned model: jev-1.13.0. State, identical in every request:
`{"user_request": "Find the latest Acme invoice email."}`

Instructions: `Choose the single best tool for the user's request.`

Anchor: `Search the mailbox for the latest Acme invoice email.`

Rivals:

| Rung | Description |
|---|---|
| R1 | Search the mailbox for the newest Acme invoice email. |
| R2 | Search the mailbox for the most recent Acme billing email. |
| R3 | Search the mailbox for recent Acme billing documents. |
| R4 | Search the mailbox for Acme payment records. |
| R5 | Search the mailbox for messages from Acme. |

| Condition | Anchor identifier | Rival identifier |
|---|---|---|
| A_random | q7f | m2k |
| B_neutral | option_a | option_b |
| C_lengthctl | drant_blorch | kesp_blorch |
| D_domain | search_by_date | search_by_sender |
| E_versioned | legacy_search | search_v2 |
| F_evaluative | wrong_choice | best_choice |

The control matches character lengths (12/11), underscore placement, and shared
second-component structure of F. Syllable matching is approximate; the vendor's
tokenizer is unavailable, so no token-level match is claimed. Nonsense strings
are not proved semantically inert.

Ten successful planned observations per cell are required, 310 planned logical
calls. Errors are retained and not replaced. Retry attempts are recorded separately.
Each phase's call order is shuffled with seed 20260920 to reduce time confounding.
JSON insertion order is preserved explicitly.

1. Evidence ladder: B and F at R1-R5, anchor in slot 1. 100 calls.
2. Position: B and F at the boundary rung, each with anchor in slot 1 and 2.
   40 calls.
3. Taxonomy: A-F at the boundary, anchor in slot 1. 60 calls.
4. Symmetry: identical anchor descriptions, B, F and E, each in original and
   reversed order. 60 calls. Record absolute first-minus-second probability,
   the larger-share key, and descriptive confidence. No correctness labels.
5. Multiclass: anchor, R1-R5, `Search the mailbox for Acme contract attachments.`,
   `Search the mailbox for unread messages.` in that order, named option_1 through
   option_8. Baseline; rename only option_5 to best_choice; rename only option_1
   to wrong_choice. 30 calls.
6. Disclaimer: boundary, F, anchor first; standard instructions versus:
   `Choose the single best tool for the user's request. The identifiers are arbitrary internal keys and carry no information. Judge only by the description text.`
   20 calls.

Boundary is the neutral Test 1 rung with median anchor probability closest to
0.50; ties use the lowest rung. An override must be recorded before collection
and marks the batch as a protocol override. Test 1 must complete before selection.
Later tests use fresh calls, not reused Test 1 observations.

## Computed verdicts

All numerical comparisons use unrounded values. Separated ranges means strictly
non-overlapping min-to-max intervals. Cell effects are median differences.
C0 uses all 31 cells, including a consistent named anchor in swapped symmetry
arms and option_1's mapped identifier in multiclass arms.

- **C0 Reproducibility:** PASS if median within-cell anchor-probability range is
  <= 0.20 and all 310 calls return jev-1.13.0. Any version mismatch voids batch.
  Missing/invalid observations give INCOMPLETE, not a positive verdict.
- **C1 Identifier sensitivity:** Test 3 F vs B. SUPPORTED if absolute median
  difference >= 0.10 with separated ranges. KILLED if C vs B absolute median
  difference >= 0.10, regardless of range separation. Otherwise NOT SUPPORTED.
  C2 failure blocks C1 support, but the length-control kill is still reported.
- **C2 Position gate:** Test 2 neutral slot 1 vs 2. PASS if absolute median
  difference <= 0.10. Failure blocks C1, C3 and C4.
- **C3 Reversal of internal ordering:** Test 1 R2-R5 only. SUPPORTED if at least
  one rung has neutral anchor wins >= 8/10 and loaded anchor wins < 5/10.
  Report deepest qualifying rung. R1 is descriptive sensitivity only.
  A win is the returned choice matching the anchor identifier.
  Claim, only when supported: Under neutral identifiers, Jev's own probability
  mass ranks the anchor above the rival. Changing only the identifiers reverses
  that ranking. The model's own evidential ordering is inverted by a
  non-evidential change.
- **C4 Production naming:** Test 3 D or E vs B. SUPPORTED if either absolute
  median difference >= 0.05 with separated ranges; otherwise NOT SUPPORTED.
- **C5 Symmetry:** pool asymmetries from the 20 loaded calls and separately the
  20 neutral calls. SUPPORTED if loaded median >= neutral median + 0.10 with
  separated pooled ranges, AND the same named key receives strictly greater
  probability in >= 8/10 observations in EACH loaded order. Either key may
  qualify; ties do not count. Otherwise NOT SUPPORTED. Versioned arms are
  descriptive. This test carries its own position control and is independent
  of C2. Confidence is descriptive only; a distribution change does not imply
  a change in an unspecified confidence statistic.
- **C6 Multiclass sensitivity:** align renamed identifiers, average each option's
  probability over the ten runs within each arm, then compute TVD against the
  baseline mean distribution. SUPPORTED if either edited arm TVD >= 0.05.
  Report both. This does not establish growth with class count, because a matched
  two-class versus eight-class interaction is not tested.
- **C7 Mitigation:** compare median anchor probabilities of each Test 6 arm to
  the neutral Test 1 boundary cell. If no-disclaimer deviation < 0.10,
  NOT APPLICABLE. Otherwise MITIGATED if disclaimer deviation <= 0.05;
  PARTIAL if disclaimer deviation is strictly less than half the initial
  deviation but > 0.05; otherwise NOT MITIGATED.

Publication decision precedence: INCOMPLETE or version mismatch or C0 failure
or length-control kill means DO NOT PUBLISH. Otherwise publish full only if C2
passes and C1 and C4 are SUPPORTED. Otherwise publish C5 alone if C5 SUPPORTED,
including when C2 fails, explicitly disclosing that failure. Otherwise DO NOT
PUBLISH. C5-only framing concerns identifier asymmetry, not calibration.
Report C2 and length-control results first, then C4 failure, then other results.
No automated result constitutes permission to publish or send messages.

## Study B design and selection

Use PolyAI/banking77 test split, sampling without replacement with Python RNG
seed 20260920. Sample 1000 source indices, first 500 tune and last 500 evaluate.
Persist exact selected items, IDs, labels, dataset revision and split before calls.
Criteria are the 77 original intent names and their underscore-to-space text.
Instruction: `Which banking intent does this customer message express?`
Jev receives the raw utterance as state, one choice question, pinned version.
LLM receives the same utterance, intent descriptions and closed label set, with
instructions to return only the intent name; max_tokens=32. Haiku first:
claude-haiku-4-5-20251001. Providers anthropic, openai-compatible or none.
Unknown prices mean accuracy-only unless explicit per-million rates are supplied.
Jev $0.042/M input, $0 output; Haiku $1/M input, $5/M output. Prices are dated
assumptions until verified against vendor sources and preserved with each run.
No caching or batch discount is requested. Cache usage, if returned, is accounted
at provider rates, not billed as ordinary input. Never silently substitute models.

Sweep tau=0.00 through 1.00 inclusive by 0.01, gate strictly confidence < tau.
Confidence 1.00 remains kept at tau=1.00; all-LLM is a separate baseline. Parity
need not exist within this grid. Choose smallest tune tau reaching tune all-LLM
accuracy. Separately choose tune accuracy-maximizing tau, ties lowest tau. Evaluate
both unchanged on evaluate. Never select thresholds using evaluate outcomes.
Held-out parity means empirical evaluate accuracy >= evaluate all-LLM accuracy,
not a statistical non-inferiority claim. If it fails, label all savings as at the
tune-selected threshold, not at held-out parity. Tune results are in-sample.

Per item: cost always includes Jev, plus that item's LLM cost when escalated;
correctness uses that item's selected arm. Latency is Jev elapsed plus LLM
elapsed for escalated items, Jev elapsed otherwise. Summed independently measured
hops are a simulated serial cascade, not an end-to-end production latency test.
Report p50/p95/p99 using linear interpolation, and flag simulated cascade p99
above all-LLM p99. Include retry waits in elapsed latency.

Report escalation rate, accuracy, selected-subset LLM accuracies, actual-token
cost/case, savings multiple, savings per million calls, and assumed maintenance
break-even table at $10k/$30k/$100k/$250k per year. If per-call savings <=0,
there is no finite break-even. Annual volume primary, monthly optional.
Report all confidently wrong kept items at tune-selected parity threshold.
If no tune parity exists, these operating-point metrics are unavailable.
If held-out parity is met and savings <3x, lead with that fact without claiming
it proves any particular architecture is inferior.

Reliability: ten equal-width bins, left-inclusive, last includes 1.00; show count,
mean confidence, midpoint and accuracy. Report requested midpoint-gap statistic
as midpoint ECE, and standard ECE using mean observed confidence as a separate
metric. Neither establishes the vendor confidence's intended mathematical meaning.
Compute on evaluate; show tune metrics separately. Include Wilson 95% intervals
for observed accuracy bins. Report evaluated sample sizes and all errors.

No-LLM mode: measured Jev reliability, distribution and errors; conditional
sensitivity for assumed per-item LLM accuracy 0.60-0.95 by 0.05 and estimated
prompt cost (UTF-8 byte length/4 input, 32 output tokens, explicitly heuristic).
Assumed accuracy is constant across items including escalated cases, a strong
untested assumption. Select each scenario's thresholds on tune and evaluate
unchanged. All scenario outcomes and savings are conditional, never measured.
No measured LLM latency or paired outcomes are invented. Without a measured
parity threshold, show wrong Jev cases and mark retention separately by scenario.

## Evidence and errors

Retain append-only CSV rows and raw response/attempt JSONL, timestamps, request
payloads excluding credentials, usage, elapsed times, requested/returned models,
source code commit, protocol hash and all configuration. New runs have unique
paths. Existing rows are never overwritten or deleted. Interrupted runs remain
incomplete; explicit resume uses the persisted plan and completed logical IDs.
Retries on 429/500/502/503/504/529: up to 5 total attempts, exponential backoff,
respect Retry-After. Requests spaced at least 50ms. Transport errors retained.
Invalid predictions count as wrong in descriptive coverage reporting; missing
usage cannot be treated as zero cost. Any failed pair prevents a confirmatory
Study B economics claim; complete-pair summaries are explicitly descriptive.
No reruns to obtain a preferred outcome. Schema and exact version are checked in
one recorded smoke call before either study. Smoke is excluded from study data.
