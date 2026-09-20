# Dataset attribution and licensing

The sampled utterances and gold labels originate from Banking77 by PolyAI, described in:

Iñigo Casanueva, Tadas Temčinas, Daniela Gerz, Matthew Henderson, and Ivan Vulić. 2020. *Efficient Intent Detection with Dual Sentence Encoders.* https://arxiv.org/abs/2003.04807

Dataset: https://huggingface.co/datasets/PolyAI/banking77
Upstream: https://github.com/PolyAI-LDN/task-specific-datasets/tree/master/banking_data
License: Creative Commons Attribution 4.0 International, https://creativecommons.org/licenses/by/4.0/

This release selects 1,000 examples from the test split, adds fixed tune/evaluate assignments and measured model outputs, and removes unrelated API metadata. It does not modify the sampled source text or gold labels. Source revisions, indices and checksums are in data/cascade-20260920T135930-b9ae3c81/dataset.json and items.json.

The dataset license does not imply endorsement by PolyAI or the authors. API providers do not endorse this analysis.

The later [MTEB comparison](docs/BANKING77_PROVENANCE.md) verifies overlap with another distribution; it does not replace the original source, change the frozen sample, or change the attribution and license used for this release.
