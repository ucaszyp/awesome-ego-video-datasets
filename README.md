# Awesome Egocentric Video Datasets

A curated index of **public egocentric (first-person) video** datasets. Each entry links to the **official release and its companion paper**. Content is split by **downstream task**; within each task file, **non-flagship** datasets are listed **from newest to oldest** by publication year.

## Metadata fields (entry template)

When adding a dataset, please fill in as many of the following as possible to keep the list maintainable and searchable.

| Field | Description |
|------|-------------|
| **Year** | Year of the dataset or companion paper’s first public release |
| **Scale** | Duration, number of clips, participants, etc. (as in the paper) |
| **Video** | Resolution, frame rate, number of viewpoints, etc. |
| **Other modalities** | Audio, depth, IMU, eye tracking, transcripts, etc. (use “—” if none) |
| **Benchmark / task** | Primary evaluation or task the entry supports |
| **Paper** | Main dataset paper (bib or official citation page) |
| **Official** | Project page, download, or access instructions |

---

## Flagship datasets and companion papers

These are widely used **umbrella benchmarks or historically central** resources. They are listed here only and **do not** appear in the per-task timelines below.

### Ego4D (2021 / CVPR 2022)

| Field | Detail |
|------|--------|
| **Scale** | ~3,670 hours of daily-life video, 931 wearers, many countries and settings |
| **Other modalities** | Audio, 3D, gaze, multi-camera, etc. (see official documentation) |
| **Paper** | Grauman, K. et al. [Ego4D: Around the World in 3,000 Hours of Egocentric Video](https://arxiv.org/abs/2110.07058). CVPR 2022 |
| **Official** | [ego4d-data.org](https://ego4d-data.org/) · [Ego4d (GitHub)](https://github.com/facebookresearch/Ego4d) |

### Ego-Exo4D (CVPR 2024)

| Field | Detail |
|------|--------|
| **Scale** | Thousands of hours of synchronized ego + exo video, many skills and scenes (see official stats) |
| **Other modalities** | Audio, gaze, point clouds, IMU, etc. |
| **Paper** | Grauman, K. et al. [Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives](https://arxiv.org/abs/2311.18259). CVPR 2024 |
| **Official** | [ego-exo4d-data.org](https://ego-exo4d-data.org/) |

### EPIC-KITCHENS-100 (2021)

| Field | Detail |
|------|--------|
| **Scale** | 100 hours, ~90K action segments, many kitchen environments |
| **Paper** | Damen, D. et al. [Rescaling Egocentric Vision: Collection, Pipeline and Challenges for EPIC-KITCHENS-100](https://epic-kitchens.github.io/public/ek100.pdf). IJCV 2021 |
| **Official** | [epic-kitchens.github.io](https://epic-kitchens.github.io/) · [Annotations](https://github.com/epic-kitchens/epic-kitchens-100-annotations) |

### Charades-Ego (2018)

| Field | Detail |
|------|--------|
| **Scale** | Large-scale paired third-person and first-person video |
| **Paper** | Sigurdsson, G.A. et al. [Charades-Ego: A Large-Scale Dataset of Paired Third and First Person Videos](https://arxiv.org/abs/1804.09626) |
| **Official** | See paper and project pages (availability per authors) |

---

## Browse by downstream task

| Direction | File |
|-----------|------|
| Video generation & world-model pretraining | [tasks/video-generation.md](tasks/video-generation.md) |
| Memory, summarization & long-form understanding | [tasks/video-memory.md](tasks/video-memory.md) |
| VLMs, instructions & QA | [tasks/vlm-instruction-and-qa.md](tasks/vlm-instruction-and-qa.md) |
| Action & activity recognition | [tasks/action-and-activity.md](tasks/action-and-activity.md) |
| Hand–object interaction, dexterity & 3D | [tasks/hand-object-and-dexterity.md](tasks/hand-object-and-dexterity.md) |
| Procedural activities & skill learning | [tasks/procedural-and-skill-learning.md](tasks/procedural-and-skill-learning.md) |

---

## Maintenance

- **Ordering**: Entries in `tasks/*.md` are **non-flagship** datasets, sorted by **year (descending)**; within the same year, order may follow arXiv or conference release dates.
- **Inclusion**: Prefer entries with a **citable paper** and **official access** (download or documented application process).
- **Contributions**: Open a PR to edit the relevant task file, or an Issue with the dataset name and paper link.
