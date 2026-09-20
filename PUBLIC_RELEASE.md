# Public release boundary

This is a fresh repository created from an explicit file allowlist. It does not include private Git history, handoff archives, environment files, live credentials, account identifiers, provider response IDs, provider fingerprints, local filesystem paths, desktop screenshots, or API-calling collectors.

The public journal is a **sanitized derivative**, not the original raw journal. It preserves logical sample IDs, status/error fields, attempt timing, pinned model names, predictions, confidence, probability distributions and token usage. It omits duplicated full requests; complete example requests and the fixed prompt-building code are included. Provider-generated IDs, creation timestamps, service-tier fields and fingerprints were removed from response bodies. Local client timestamps were retained to document the tune/evaluate sequence.

The numerical outputs of the offline reproduction agree with the private original analysis. Hashes of the original and sanitized journals are recorded in appendix/release_provenance.json. The original source evidence remains unchanged in the private workspace. This release cannot independently establish the authenticity or prior commit timing of the private originals; checksums and copied protocols are provenance records, not independent attestation.

The published data consists of a sample of the public Banking77 benchmark and model responses to those questions, not real production customer traffic. Some public benchmark questions contain personal-sounding first-person wording; that wording is part of the attributed source dataset.

No executable source file in this release sends API requests or loads credentials. Request JSON is documentation, not an automatically executed workload. Running article/reproduce.py is offline. Tests and scans described in SECURITY_REVIEW.md are scoped checks, not a guarantee against every possible vulnerability.
