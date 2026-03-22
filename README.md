# Awesome Egocentric Video Datasets 🎥

> A curated list of high-quality egocentric (first-person) video datasets, associated papers, benchmarks, tools and resources.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

## Repository structure

| Path | Contents |
|------|----------|
| [`datasets.md`](datasets.md) | **Dataset catalog only:** summary table + detailed per-dataset entries (scale, paper, download). |
| [`benchmarks.md`](benchmarks.md) | **Benchmarks & challenges** built on egocentric video, ordered **newest → oldest** by year. |
| [`tasks/`](tasks/) | **Seven downstream-task views** — datasets grouped by research direction (generation, memory, VLM/QA, action, hand–object, procedural, 3D scene). A dataset may appear in more than one file. |

`README.md` is the navigation hub; [`datasets.md`](datasets.md) is the dataset index; [`benchmarks.md`](benchmarks.md) is the evaluation index.

## Table of Contents

- [Papers & Surveys](#papers--surveys)
- [Benchmarks & challenges (`benchmarks.md`)](benchmarks.md)
- [Tools & Libraries](#tools--libraries)
- [Related Awesome Lists](#related-awesome-lists)
- [Contributing](#contributing)
- [License](#license)

### Task files (`tasks/`)

- [Video generation & world-model pretraining](tasks/video-generation-world-models.md)
- [Memory, summarization & long-form understanding](tasks/memory-long-form.md)
- [VLMs, instructions & QA](tasks/vlm-instruction-qa.md)
- [Action & activity recognition](tasks/action-activity.md)
- [Hand–object interaction, dexterity & 3D](tasks/hand-object-dexterity-3d.md)
- [Procedural activities & skill learning](tasks/procedural-skill-learning.md)
- [Egocentric 3D scene understanding & localization](tasks/scene-understanding-localization.md)

## Papers & Surveys

Sorted by **year (newest first)**.

- [Challenges and Trends in Egocentric Vision: A Survey](https://arxiv.org/abs/2503.15275) — Li et al., 2025 (MIR / arXiv).
- [Bridging Perspectives: A Survey on Cross-view Collaborative Intelligence with Egocentric-Exocentric Vision](https://arxiv.org/abs/2506.06253) — 2025 / IJCV 2026.
- [HD-EPIC: A Highly-Detailed Egocentric Video Dataset](https://arxiv.org/abs/2502.04144) — Perrett et al., CVPR 2025.
- [Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives](https://arxiv.org/abs/2311.18259) — Grauman et al., CVPR 2024.
- [EgoExoLearn: A Dataset for Bridging Asynchronous Ego- and Exo-centric View of Procedural Activities in Real World](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_EgoExoLearn_A_Dataset_for_Bridging_Asynchronous_Ego-_and_Exo-centric_View_CVPR_2024_paper.html) — Huang et al., CVPR 2024.
- [EgoSchema: A Diagnostic Benchmark for Very Long-form Video Language Understanding](https://arxiv.org/abs/2308.09126) — Mangalam et al., NeurIPS 2023 (Datasets & Benchmarks).
- [Ego4D: Around the World in 3,000 Hours of Egocentric Video](https://arxiv.org/abs/2110.07058) — Grauman et al., CVPR 2022.
- [Rescaling Egocentric Vision: Collection, Pipeline and Challenges for EPIC-KITCHENS-100](https://epic-kitchens.github.io/public/ek100.pdf) — Damen et al., IJCV 2021.
- [Charades-Ego: A Large-Scale Dataset of Paired Third and First Person Videos](https://arxiv.org/abs/1804.09626) — Sigurdsson et al., 2018.

## Benchmarks & challenges

Evaluation benchmarks and official challenge suites (with **primary egocentric data** called out) live in **[`benchmarks.md`](benchmarks.md)**, sorted **newest → oldest** by year. Dataset downloads and per-dataset metadata stay in [`datasets.md`](datasets.md).

## Tools & Libraries

| Name | Description | Link |
|------|-------------|------|
| Ego4D CLI | Official downloader and tooling for accessing Ego4D releases. | [GitHub](https://github.com/facebookresearch/Ego4d) |
| HOMIE-toolkit | Toolkit released with Ropedia Xperience-10M. | [GitHub](https://github.com/Ropedia/HOMIE-toolkit) |
| AssemblyHands Toolkit | Official toolkit for the AssemblyHands benchmark. | [GitHub](https://github.com/facebookresearch/assemblyhands-toolkit) |
| TREK-150 Toolkit | Official toolkit for the TREK-150 tracking benchmark. | [GitHub](https://github.com/matteo-dunnhofer/TREK-150-toolkit) |

## Related Awesome Lists

- [Awesome-Egocentric](https://github.com/EgoAlpha/Awesome-Egocentric)
- [awesome-egocentric-vision](https://github.com/Sid2697/awesome-egocentric-vision)
- [Awesome-Egocentric-and-Exocentric-Vision](https://github.com/ayiyayi/Awesome-Egocentric-and-Exocentric-Vision)

## Contributing

1. High-quality, citable datasets with official access.
2. **Datasets:** update [`datasets.md`](datasets.md) (summary + detailed entry) and the relevant [`tasks/`](tasks/) file.
3. **Benchmarks:** add or edit rows in [`benchmarks.md`](benchmarks.md) (year sections, newest first).
4. Keep the dataset summary table, **benchmarks.md** year sections, and **Papers & Surveys** sorted by **year (newest first)**.

[CONTRIBUTING.md](CONTRIBUTING.md)

## License

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). See [LICENSE](LICENSE).
