# Public-release review

Reviewed 2026-09-21. Scope: this new public repository snapshot, not the private workspace or previously generated archives.

## Included and excluded

The release was assembled using explicit file selection and response-field projection. It contains public benchmark examples, measured model outputs, numeric usage, aggregate reports, formal protocols, article and supporting report figures, and one offline Python reproduction script.

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

## GitHub history recheck, 21 September 2026

A fresh mirror was fetched from the public GitHub repository before the documentation update. Its only advertised ref was `main`, at `49a012a119613df94e234ad855d19c6040a9d12d`, with four reachable commits.

- Gitleaks 8.30.1 scanned the complete reachable history and the current working tree with redacted reports: zero findings.
- Exact-byte checks for both available study API credentials covered every reachable blob, commit and tag object: zero matches. The values were neither printed nor included in the public audit.
- Checks of those objects for local user/temp paths, private-key markers and provider response IDs/fingerprints found no matches. All commit author and committer addresses were GitHub noreply addresses.
- GitHub reported no open secret-scanning alerts, pull requests, issues, releases, workflow runs, workflow artifacts or forks at the time of review.
- The updated documentation and source-comparison records preserve the original study data and thresholds. Offline reproduction still matches the published result exactly, including the failed held-out parity criterion.

No sensitive content requiring removal was identified in this scope, so no history rewrite was needed. The scan covers the repository's reachable published history and checked GitHub surfaces; it cannot attest to inaccessible server-side objects or third-party copies.
