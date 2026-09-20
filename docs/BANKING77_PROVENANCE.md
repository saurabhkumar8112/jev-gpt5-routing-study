# Banking77 source and the MTEB distribution

The study used PolyAI's original Banking77 release, introduced by Casanueva et al. in 2020. Its loader downloaded the original `banking_data/test.csv` and used the label metadata from `PolyAI/banking77`. The source metadata is recorded in [dataset.json](../data/cascade-20260920T135930-b9ae3c81/dataset.json).

- Original GitHub revision: `57ec275d8078af65b7731c2a98be812d844a6d6b`.
- PolyAI Hugging Face metadata revision: `90d4e2ee5521c04fc1488f065b8b083658768c57`.
- Original [test CSV](https://github.com/PolyAI-LDN/task-specific-datasets/blob/57ec275d8078af65b7731c2a98be812d844a6d6b/banking_data/test.csv): 3,080 rows and 77 intents.
- Sampling: 1,000 items without replacement, seed `20260920`; 500 tune and 500 evaluate. The stored items preserve the original text and gold labels.

## Comparison with MTEB

On 21 September 2026, the study sources were compared with the Parquet files selected by the default configuration of [`mteb/banking77`](https://huggingface.co/datasets/mteb/banking77/tree/18072d2685ea682290f7b8924d94c62acc19c0b2), revision `18072d2685ea682290f7b8924d94c62acc19c0b2`.

| Split | Original PolyAI rows | MTEB rows | Original pairs absent from MTEB |
|---|---:|---:|---:|
| Train | 10,003 | 9,993 | 10 |
| Test | 3,080 | 3,076 | 4 |

Comparison used exact Unicode text and the human-readable label, with no text normalization or relabeling. There were no additional or altered text-and-label pairs in the checked MTEB files; they were subsets of the original splits.

**All 500 tuning examples and all 500 evaluation examples in this study are present with identical text and labels in that MTEB distribution.** None of its four omitted test examples occurs in the study sample. The [machine-readable comparison](../appendix/banking77_source_comparison.json) includes the source URLs, pinned revisions, SHA-256 checksums and counts. The original training split was downloaded only for this provenance comparison; it was not used in the study's threshold selection or evaluation.

This does not mean that resampling 1,000 positions with the same seed from MTEB would select the same examples: removing rows changes the population size and indices. Reproduction should use the published frozen [items.json](../data/cascade-20260920T135930-b9ae3c81/items.json).

The provenance check does not rerun inference, change results, or turn this experiment into an MTEB evaluation. Model configuration, selected examples and evaluation protocol still determine whether scores are comparable.
