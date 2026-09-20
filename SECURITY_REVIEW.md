# Public-release review

Reviewed 2026-09-21. Scope: this new public repository snapshot, not the private workspace or previously generated archives.

## Included and excluded

The release was assembled using explicit file selection and response-field projection. It contains public benchmark examples, measured model outputs, numeric usage, aggregate reports, formal protocols, two article figures, supporting report figures, and one offline Python reproduction script.

It excludes environment/configuration secrets, authentication headers, private Git history, provider response IDs and fingerprints, local paths, account metadata, full handoff archives, desktop/terminal screenshots, and live API collectors. The original private evidence was not edited. Public journal transformations are documented in PUBLIC_RELEASE.md.

## Checks performed

- Gitleaks 8.30.1 directory scan with redacted reporting: no findings. The tool binary was obtained from the official release and checked against its published SHA-256 checksum.
- Exact-byte checks for the locally available study credentials: no matches. Credential values were never included in this report.
- Checks for local filesystem paths, provider response-ID prefixes, token prefixes and private-key markers: no matches in published text.
- Public dataset screening: no email-address patterns or sequences of seven or more digits in the 1,000 sampled utterances. This is limited pattern screening, not a comprehensive personal-data classifier.
- Source review: the only Python file reads local JSON/JSONL, calculates metrics, and prints results. It has no networking, credential loading, subprocess execution, eval, pickle loading, or third-party dependency installation.
- Offline reproduction from sanitized records agrees with the original reported threshold, accuracy and costs.
- Relative article and README links checked; figures visually inspected.
- Publication uses a new Git history with a public noreply commit address, not a push of the original working repository.

These checks reduce identified disclosure and execution risks. They are not a claim that arbitrary future changes, dependencies, or downstream uses are free of vulnerabilities. API request examples describe authenticated provider operations but contain no credentials and are not executed by this repository.
