<div align="center">

# 🎥 Awesome Egocentric Video Datasets

**📜 A Curated List of Egocentric (First-Person) Video Datasets, Benchmarks, and Tools**

<p align="center">
  <img src="banner.png" alt="Awesome Egocentric Video Datasets" width="100%">
</p>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)

</div>

## Overview

- 🎯 [Aim](#aim) | 📚 [Papers & Surveys](#papers--surveys)
- 🎬 [Video Generation & World-Model Pretraining](#-video-generation--world-model-pretraining)
- 🧠 [Memory, Summarization & Long-form Understanding](#-memory-summarization--long-form-understanding)
- 💬 [VLMs, Instructions & QA](#-vlms-instructions--qa)
- 🏃 [Action & Activity Recognition](#-action--activity-recognition)
- ✋ [Hand–Object Interaction, Dexterity & 3D](#-handobject-interaction-dexterity--3d)
- 📋 [Procedural Activities & Skill Learning](#-procedural-activities--skill-learning)
- 🗺️ [3D Scene Understanding & Localization](#-3d-scene-understanding--localization)
- 🛠️ [Tools & Libraries](#-tools--libraries) | 🔗 [Related Awesome Lists](#-related-awesome-lists) | 🤝 [Contributing](#-contributing) | 📄 [License](#license)

## Aim

This repository tracks egocentric video datasets through a task-first view: every dataset appears once as a primary entry under one of seven research themes, with cross-links where it also matters. The goal is fast navigation for researchers who need scale, task fit, benchmark context, and official resources without bouncing across multiple index files.

## Papers & Surveys

Sorted newest to oldest, with flagship surveys and corpus papers highlighted first.

- [⭐️] **Challenges and Trends in Egocentric Vision: A Survey** (2025) — Li et al., 2025 survey of datasets, tasks, benchmarks, and open challenges in egocentric vision.
  [![arXiv](https://img.shields.io/badge/arXiv-2503.15275-b31b1b.svg)](https://arxiv.org/abs/2503.15275)

- [⭐️] **Bridging Perspectives: A Survey on Cross-view Collaborative Intelligence with Egocentric-Exocentric Vision** (2025) — Cross-view survey covering ego-exo collaboration, paired capture, and collaborative perception.
  [![arXiv](https://img.shields.io/badge/arXiv-2506.06253-b31b1b.svg)](https://arxiv.org/abs/2506.06253)

- **HD-EPIC: A Highly-Detailed Egocentric Video Dataset** (2025) — Dataset paper introducing fine-grained kitchen understanding with dense multimodal annotations.
  [![arXiv](https://img.shields.io/badge/arXiv-2502.04144-b31b1b.svg)](https://arxiv.org/abs/2502.04144)

- **Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives** (2024) — Large-scale paired ego-exo dataset paper spanning skilled activity and multiview understanding.
  [![arXiv](https://img.shields.io/badge/arXiv-2311.18259-b31b1b.svg)](https://arxiv.org/abs/2311.18259)

- **EgoExoLearn: A Dataset for Bridging Asynchronous Ego- and Exo-centric View of Procedural Activities in Real World** (2024) — Procedural ego-exo paper focused on asynchronous activity alignment in real environments.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_EgoExoLearn_A_Dataset_for_Bridging_Asynchronous_Ego-_and_Exo-centric_View_CVPR_2024_paper.html)

- **EgoSchema: A Diagnostic Benchmark for Very Long-form Video Language Understanding** (2023) — Benchmark paper targeting long-form memory and reasoning over egocentric video.
  [![arXiv](https://img.shields.io/badge/arXiv-2308.09126-b31b1b.svg)](https://arxiv.org/abs/2308.09126)

- [⭐️] **Ego4D: Around the World in 3,000 Hours of Egocentric Video** (2022) — Flagship corpus paper introducing the large-scale Ego4D benchmark suite.
  [![arXiv](https://img.shields.io/badge/arXiv-2110.07058-b31b1b.svg)](https://arxiv.org/abs/2110.07058)

- [⭐️] **Rescaling Egocentric Vision: Collection, Pipeline and Challenges for EPIC-KITCHENS-100** (2021) — Canonical kitchen benchmark paper for action recognition, detection, and anticipation.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://epic-kitchens.github.io/public/ek100.pdf)

- **Charades-Ego: A Large-Scale Dataset of Paired Third and First Person Videos** (2018) — Early paired ego-exo benchmark for activity transfer and alignment.
  [![arXiv](https://img.shields.io/badge/arXiv-1804.09626-b31b1b.svg)](https://arxiv.org/abs/1804.09626)

## 🎬 Video Generation & World-Model Pretraining

> Datasets here emphasize large-scale first-person pretraining corpora, video generation, editing, or world-model supervision from ego video.

### Datasets at a glance

| Name | Year | Scale | Key tasks | Paper | Link |
|------|------|-------|-----------|-------|------|
| ⭐ Ropedia Xperience-10M | 2026 | Large multi-stream experiences | Multimodal ego learning | [Paper](https://ropedia.com/) | [Hugging Face](https://huggingface.co/datasets/ropedia-ai/xperience-10m) |
| ⭐ EgoVid-5M | 2024 | 5M clips | Video generation, motion+text | [Paper](https://arxiv.org/abs/2411.08380) | [Site](https://egovid.github.io/) |
| DreamDojo-HV | 2026 | Very large FP video (see paper) | World models, pretraining | [Paper](https://arxiv.org/abs/2602.06949) | N/A |
| Ego-1K | 2026 | Multiview clips (~1K takes) | Neural 3D/4D synthesis | [Paper](https://arxiv.org/abs/2603.13741) | [Hugging Face](https://huggingface.co/datasets/facebook/ego-1k) |
| In-lab | 2026 | Lab tabletop trajectories | Skills, world models (w/ DreamDojo) | [Paper](https://arxiv.org/abs/2602.06949) | N/A |
| EgoEdit | 2025 | 100K editing pairs | Egocentric video editing | [Paper](https://arxiv.org/abs/2512.06065) | [Site](https://snap-research.github.io/EgoEdit) |

### Entries

- [⭐️] **Ropedia Xperience-10M** (2026) — 10M multimodal experiences with 6 RGB streams, stereo depth, pose/SLAM, hand-body mocap, audio, and IMU for large-scale ego pretraining.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://ropedia.com/) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/Ropedia/HOMIE-toolkit) [![🤗](https://img.shields.io/badge/%F0%9F%A4%97-Dataset-yellow.svg)](https://huggingface.co/datasets/ropedia-ai/xperience-10m)

- [⭐️] **EgoVid-5M** (2024) — 5M first-person clips curated for text-and-motion-conditioned video generation from wearable footage.
  [![arXiv](https://img.shields.io/badge/arXiv-2411.08380-b31b1b.svg)](https://arxiv.org/abs/2411.08380) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2411.08380) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/JeffWang987/EgoVid)

- **DreamDojo-HV** (2026) — Very large FP video (see paper); World models, pretraining.
  [![arXiv](https://img.shields.io/badge/arXiv-2602.06949-b31b1b.svg)](https://arxiv.org/abs/2602.06949) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2602.06949)

- **Ego-1K** (2026) — Multiview clips (~1K takes); Neural 3D/4D synthesis.
  [![arXiv](https://img.shields.io/badge/arXiv-2603.13741-b31b1b.svg)](https://arxiv.org/abs/2603.13741) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2603.13741) [![🤗](https://img.shields.io/badge/%F0%9F%A4%97-Dataset-yellow.svg)](https://huggingface.co/datasets/facebook/ego-1k)

- **In-lab** (2026) — Lab tabletop trajectories; Skills, world models (w/ DreamDojo).
  [![arXiv](https://img.shields.io/badge/arXiv-2602.06949-b31b1b.svg)](https://arxiv.org/abs/2602.06949) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2602.06949)

- **EgoEdit** (2025) — 100K editing pairs; Egocentric video editing.
  [![arXiv](https://img.shields.io/badge/arXiv-2512.06065-b31b1b.svg)](https://arxiv.org/abs/2512.06065) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2512.06065)

### Benchmarks built on these datasets

| Benchmark | Capability | Primary data | Official link | Notes |
|-----------|------------|--------------|---------------|-------|
| EgoEdit | Egocentric video editing | EgoEdit / EgoEditData | [Project](https://snap-research.github.io/EgoEdit) | Dataset+benchmark |

## 🧠 Memory, Summarization & Long-form Understanding

> This section collects long-horizon lifelog, summarization, and persistent-memory datasets where temporal continuity matters as much as recognition.

### Datasets at a glance

| Name | Year | Scale | Key tasks | Paper | Link |
|------|------|-------|-----------|-------|------|
| ⭐ EgoLife | 2025 | ~266–300 h daily life | Long-form assistants, memory | [Paper](https://arxiv.org/abs/2503.01773) | [Site](https://egolife-ai.github.io/) |
| ⭐ EgoSchema | 2023 | 250+ h / 5K QA | Long-form video QA | [Paper](https://arxiv.org/abs/2308.09126) | [Site](https://egoschema.github.io/) |
| VidChapters-7M | 2023 | 817K videos / 7M chapters | Chaptering (not ego-only) | N/A | [Site](https://antoyang.github.io/vidchapters.html) |
| Multi-Ego | 2022 | ~12 h / 41 seq. | Multi-wearer, summarization | N/A | [GitHub](https://github.com/M-Elfeki/Multi-DPP) |
| DoMSEV | 2018 | 80 h, 48 seq. | Semantic fast-forward, first-person video | N/A | [Site](https://www.verlab.dcc.ufmg.br/semantic-hyperlapse/cvpr2018-dataset/) |
| HUJI-EgoSeg | 2014 | 29 long egocentric videos (~1–5 h each), pixel-level temporal segmentation annotations | memory, summarization & long-form understanding | N/A | [Site](http://www.cs.huji.ac.il/~yedMDpid/egoseg/) |
| UT Ego | 2012 | ~17 h, 4 long videos | Summarization, long-form ego | N/A | [Site](http://vision.cs.utexas.edu/projects/egocentric_data/UT_Egocentric_Dataset.html) |
| VINST / Visual Diaries | 2011 | 31 egocentric videos capturing daily commutes; used for temporal segmentation and video summarization | memory, summarization & long-form understanding | N/A | N/A |

### Entries

- [⭐️] **EgoLife** (2025) — ~266-300 h of daily-life capture in EgoHouse with Meta Aria, third-person cameras, and mmWave sensors for persistent assistant memory.
  [![arXiv](https://img.shields.io/badge/arXiv-2503.01773-b31b1b.svg)](https://arxiv.org/abs/2503.01773) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2503.01773) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/EvolvingLMMs-Lab/EgoLife) [![🤗](https://img.shields.io/badge/%F0%9F%A4%97-Dataset-yellow.svg)](https://huggingface.co/datasets/lmms-lab/EgoLife)

- [⭐️] **EgoSchema** (2023) — 250+ h of long-form Ego4D video with 5K QA pairs designed to probe memory and causal understanding over extended clips.
  [![arXiv](https://img.shields.io/badge/arXiv-2308.09126-b31b1b.svg)](https://arxiv.org/abs/2308.09126) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2308.09126) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/egoschema/EgoSchema)

- **VidChapters-7M** (2023) — 817K videos / 7M chapters; Chaptering (not ego-only).
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://antoyang.github.io/vidchapters.html) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/antoyang/VidChapters)

- **Multi-Ego** (2022) — ~12 h / 41 seq; Multi-wearer, summarization.
  [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/M-Elfeki/Multi-DPP)

- **DoMSEV** (2018) — 80 h, 48 seq; Semantic fast-forward, first-person video.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://www.verlab.dcc.ufmg.br/semantic-hyperlapse/cvpr2018-dataset/)

- **HUJI-EgoSeg** (2014) — 29 long egocentric videos (~1–5 h each), pixel-level temporal segmentation annotations; memory, summarization & long-form understanding.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](http://www.cs.huji.ac.il/~yedMDpid/egoseg/)

- **UT Ego** (2012) — ~17 h, 4 long videos; Summarization, long-form ego.
  [![Project](https://img.shields.io/badge/Project-Link-blue.svg)](http://vision.cs.utexas.edu/projects/egocentric_data/UT_Egocentric_Dataset.html)

- **VINST / Visual Diaries** (2011) — 31 egocentric videos capturing daily commutes; used for temporal segmentation and video summarization; memory, summarization & long-form understanding.

### Benchmarks built on these datasets

| Benchmark | Capability | Primary data | Official link | Notes |
|-----------|------------|--------------|---------------|-------|
| EgoSchema | Long-form video-language understanding | Ego4D | [Site](https://egoschema.github.io/) | Standalone |

## 💬 VLMs, Instructions & QA

> These datasets target egocentric video-language pretraining, instruction following, dialog, and question answering over first-person streams.

### Datasets at a glance

| Name | Year | Scale | Key tasks | Paper | Link |
|------|------|-------|-----------|-------|------|
| ⭐ HD-EPIC | 2025 | ~41 h / dense labels | Fine-grained kitchen, VQA | [Paper](https://arxiv.org/abs/2502.04144) | [Site](https://hd-epic.github.io/) |
| EgoEMS | 2025 | 20+ h emergency scenarios | EMS QA, multimodal | [Paper](https://arxiv.org/abs/2511.09894) | [GitHub](https://github.com/UVA-DSA/EgoEMS) |
| HowToDIV | 2025 | ~24 h instructional | Dialog, procedural QA | [Paper](https://arxiv.org/abs/2508.11192) | [GitHub](https://github.com/google/howtodiv) |
| InterVLA | 2025 | 11.4 h interactions | Instruction, ego–exo mocap | [Paper](https://arxiv.org/abs/2508.04681) | [Site](https://liangxuy.github.io/InterVLA/) |
| AssistQ | 2022 | 100 long videos / 529 QA | Instructional QA | N/A | [GitHub](https://github.com/showlab/AssistQ) |
| EgoClip | 2022 | 3.8M clip–text pairs | Video-language pretraining | N/A | [GitHub](https://github.com/showlab/EgoVLP) |
| EgoTaskQA | 2022 | ~2K videos / 40K QA | Causal & task QA | N/A | [Site](https://sites.google.com/view/egotaskqa) |
| EgoVQA | 2019 | 600+ QAs | Video QA | N/A | N/A |

### Entries

- [⭐️] **HD-EPIC** (2025) — ~41 h of densely labeled cooking video with recipe steps, audio events, gaze, 3D grounding, and VQA supervision.
  [![arXiv](https://img.shields.io/badge/arXiv-2502.04144-b31b1b.svg)](https://arxiv.org/abs/2502.04144) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2502.04144) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/hd-epic/hd-epic-annotations)

- **EgoEMS** (2025) — 20+ h emergency scenarios; EMS QA, multimodal.
  [![arXiv](https://img.shields.io/badge/arXiv-2511.09894-b31b1b.svg)](https://arxiv.org/abs/2511.09894) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2511.09894) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/UVA-DSA/EgoEMS)

- **HowToDIV** (2025) — ~24 h instructional; Dialog, procedural QA.
  [![arXiv](https://img.shields.io/badge/arXiv-2508.11192-b31b1b.svg)](https://arxiv.org/abs/2508.11192) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2508.11192) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/google/howtodiv)

- **InterVLA** (2025) — 11.4 h interactions; Instruction, ego–exo mocap.
  [![arXiv](https://img.shields.io/badge/arXiv-2508.04681-b31b1b.svg)](https://arxiv.org/abs/2508.04681) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2508.04681)

- **AssistQ** (2022) — 100 long videos / 529 QA; Instructional QA.
  [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/showlab/AssistQ)

- **EgoClip** (2022) — 3.8M clip–text pairs; Video-language pretraining.
  [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/showlab/EgoVLP)

- **EgoTaskQA** (2022) — ~2K videos / 40K QA; Causal & task QA.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://sites.google.com/view/egotaskqa) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/Buzz-Beater/EgoTaskQA)

- **EgoVQA** (2019) — 600+ QAs; Video QA.

- *EgoSchema — see [Memory, Summarization & Long-form Understanding](#-memory-summarization--long-form-understanding)*

### Benchmarks built on these datasets

| Benchmark | Capability | Primary data | Official link | Notes |
|-----------|------------|--------------|---------------|-------|
| EgoEMS | EMS QA, multimodal assessment | EgoEMS | [GitHub](https://github.com/UVA-DSA/EgoEMS) | Dataset+benchmark |
| HD-EPIC | Fine-grained kitchen understanding, VQA | HD-EPIC | [Site](https://hd-epic.github.io/) | Dataset+benchmark |
| HowToDIV | Multi-turn instructional dialog & QA | HowToDIV | [GitHub](https://github.com/google/howtodiv) | Standalone |
| InterVLA | Instruction following, interaction understanding | InterVLA | [Site](https://liangxuy.github.io/InterVLA/) | Dataset+benchmark |
| AssistQ | Instructional affordance-centric QA | AssistQ | [GitHub](https://github.com/showlab/AssistQ) | Standalone |
| EgoTaskQA | Causal, predictive, explanatory, counterfactual QA | EgoTaskQA | [Site](https://sites.google.com/view/egotaskqa) | Standalone |
| EgoVQA | Egocentric video QA | EgoVQA | ICCV 2019 EPIC workshop release | Standalone |

## 🏃 Action & Activity Recognition

> Canonical action-recognition, activity-analysis, affect, and interaction datasets built around first-person human behavior live here.

### Datasets at a glance

| Name | Year | Scale | Key tasks | Paper | Link |
|------|------|-------|-----------|-------|------|
| ⭐ Ego4D | 2022 | ~3,670 h | AR, VQA, forecasting, many | [Paper](https://arxiv.org/abs/2110.07058) | [Site](https://ego4d-data.org/) |
| ⭐ EPIC-KITCHENS-100 | 2021 | 100 h / 90K segments | Action recognition, many | [Paper](https://epic-kitchens.github.io/public/ek100.pdf) | [Site](https://epic-kitchens.github.io/) |
| EgoScale | 2026 | 20k+ h labeled manipulation (paper) | Action, dexterous transfer | [Paper](https://arxiv.org/abs/2602.16710) | N/A |
| EgoCampus | 2025 | ~32 h / campus paths (paper) | Gaze, pedestrian ego | [Paper](https://arxiv.org/abs/2512.07668) | [GitHub](https://github.com/ComputerVisionRutgers/EgoCampus) |
| AEA | 2024 | 143 seq. / ~7.3 h | Everyday activities, Aria | [Paper](https://arxiv.org/abs/2402.13349) | [Site](https://www.projectaria.com/datasets/aea/) |
| EgoSurgery (Phase / Tool / HTS) | 2024 | Open-surgery ego video | Phase, tools, segmentation | [Paper](https://arxiv.org/abs/2405.19644) | [GitHub](https://github.com/Fujiry0/EgoSurgery) |
| E³ (Exploring Embodied Emotion) | 2024 | 50+ h | Emotion, multimodal ego | N/A | [GitHub](https://github.com/Exploring-Embodied-Emotion-official/E3) |
| EGOFALLS | 2023 | Fall samples / AV | Fall detection | N/A | [Site](https://www.dataverse.nl/dataset.xhtml?persistentId=doi:10.34894/HO5GE3) |
| Epic-Sounding-Object | 2023 | 3.2K short clips | Audio-visual localization | N/A | [GitHub](https://github.com/WikiChao/Ego-AV-Loc) |
| HoloAssist | 2023 | 169 h | Interactive assistants | [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Wang_HoloAssist_an_Egocentric_Human_Interaction_Dataset_for_Interactive_AI_Assistants_ICCV_2023_paper.html) | [Site](https://holoassist.github.io/) |
| WEAR | 2023 | ~19 h outdoor sports | Activity + IMU | N/A | [Site](https://mariusbock.github.io/wear/) |
| N-EPIC-KITCHENS | 2022 | Event + RGB subset | Action, neuromorphic | [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Plizzari_E2GOMOTION_Motion_Augmented_Event_Stream_for_Egocentric_Action_Recognition_CVPR_2022_paper.html) | [GitHub](https://github.com/EgocentricVision/N-EPIC-Kitchens) |
| Ego-Deliver | 2021 | 5,360 videos | Delivery ego analysis | N/A | [Site](https://egodeliver.github.io/EgoDeliver_Dataset/) |
| HOMAGE | 2021 | 30 h / compositional | Home activities | [Paper](https://openaccess.thecvf.com/content/CVPR2021/html/Rai_Home_Action_Genome_Cooperative_Compositional_Action_Understanding_CVPR_2021_paper.html) | [Site](https://homeactiongenome.org/) |
| MECCANO | 2021 | ~55 h industrial | HOI, ego | N/A | [Site](https://iplab.dmi.unict.it/MECCANO/) |
| EGO-CH | 2020 | 27+ h, cultural sites | Visitor behavior, POI tasks | N/A | N/A |
| EgoCom | 2020 | 38.5 h conversation | Multiperson ego dialog | N/A | [GitHub](https://github.com/facebookresearch/EgoCom-Dataset) |
| LEMMA | 2020 | Multi-view activities | Multi-agent tasks | N/A | [Site](https://sites.google.com/view/lemma-activity) |
| Charades-Ego | 2018 | Paired ego / exo | Alignment, actions | [Paper](https://arxiv.org/abs/1804.09626) | [Site](https://prior.allenai.org/projects/charades-ego) |
| EGTEA Gaze+ | 2018 | 28 h cooking | Gaze + action recognition | N/A | [Site](https://cbs.ic.gatech.edu/fpv/) |
| EgoGesture | 2017 | 2K+ videos / 24K samples | Gesture recognition | N/A | [Site](https://nlpr.ia.ac.cn/iva/yfzhang/datasets/egogesture.html) |
| Stanford ECM | 2017 | 31 hours, augmented with heart rate and accelerometer, 23–24 daily activity categories | action & activity recognition | N/A | N/A |
| THU-READ | 2017 | 1,920 clips (8 subjects × 40 actions × 3 reps × 2 modalities), RGB-D from helmet-mounted sensor | action & activity recognition | N/A | [Site](https://ivg.au.tsinghua.edu.cn/dataset/THU_READ.php) |
| PEV (UTokyo Paired Ego-Video) | 2016 | 1,226 pairs of first-person clips, synchronous dyadic conversations, 8 interaction categories, 6 subjects | action & activity recognition | N/A | N/A |
| FPPA | 2015 | 5 subjects, 5 daily actions, egocentric video with hand and gaze cues | action & activity recognition | N/A | N/A |
| JPL-Interaction | 2013 | 84 videos, 7 activity types (4 positive, 1 neutral, 2 negative interactions), 320×240@30 fps | action & activity recognition | N/A | [Site](http://michaelryoo.com/jpl-interaction.html) |
| ADL | 2012 | ~10 h, 20 participants | ADL recognition, objects | N/A | [Site](https://www.csee.umbc.edu/~hpirsiav/papers/ADLdataset/) |
| Social Interactions | 2012 | 8 social events, ~60 hours, head-mounted cameras, multiple participants per event | action & activity recognition | N/A | [Site](https://cbs.ic.gatech.edu/fpv/) |
| EgoAction | 2011 | First-person sports videos (skateboarding, skiing, cycling, etc | action & activity recognition | N/A | N/A |

### Entries

- [⭐️] **Ego4D** (2022) — ~3,670 h; AR, VQA, forecasting, many.
  [![arXiv](https://img.shields.io/badge/arXiv-2110.07058-b31b1b.svg)](https://arxiv.org/abs/2110.07058) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2110.07058) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/facebookresearch/Ego4d)

- [⭐️] **EPIC-KITCHENS-100** (2021) — 100 h of unscripted kitchen activity with 90K segments; the canonical egocentric action-recognition and anticipation benchmark.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://epic-kitchens.github.io/public/ek100.pdf) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://epic-kitchens.github.io/public/ek100.pdf) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/epic-kitchens/epic-kitchens-100-annotations)

- **EgoScale** (2026) — 20k+ h labeled manipulation (paper); Action, dexterous transfer.
  [![arXiv](https://img.shields.io/badge/arXiv-2602.16710-b31b1b.svg)](https://arxiv.org/abs/2602.16710) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2602.16710)

- **EgoCampus** (2025) — ~32 h / campus paths (paper); Gaze, pedestrian ego.
  [![arXiv](https://img.shields.io/badge/arXiv-2512.07668-b31b1b.svg)](https://arxiv.org/abs/2512.07668) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2512.07668) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/ComputerVisionRutgers/EgoCampus)

- **AEA** (2024) — 143 seq. / ~7.3 h; Everyday activities, Aria.
  [![arXiv](https://img.shields.io/badge/arXiv-2402.13349-b31b1b.svg)](https://arxiv.org/abs/2402.13349) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2402.13349) [![🤗](https://img.shields.io/badge/%F0%9F%A4%97-Dataset-yellow.svg)](https://huggingface.co/datasets/projectaria/aria-everyday-activities)

- **EgoSurgery (Phase / Tool / HTS)** (2024) — Open-surgery ego video with companion phase, tool, and hand-tool segmentation releases for phase recognition, instrument analysis, and dense surgical interaction understanding.
  [![arXiv](https://img.shields.io/badge/arXiv-2405.19644-b31b1b.svg)](https://arxiv.org/abs/2405.19644) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2405.19644) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/Fujiry0/EgoSurgery)

- **E³ (Exploring Embodied Emotion)** (2024) — 50+ h; Emotion, multimodal ego.
  [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/Exploring-Embodied-Emotion-official/E3)

- **EGOFALLS** (2023) — Fall samples / AV; Fall detection.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://www.dataverse.nl/dataset.xhtml?persistentId=doi:10.34894/HO5GE3)

- **Epic-Sounding-Object** (2023) — 3.2K short clips; Audio-visual localization.
  [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/WikiChao/Ego-AV-Loc)

- **HoloAssist** (2023) — 169 h; Interactive assistants.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://openaccess.thecvf.com/content/ICCV2023/html/Wang_HoloAssist_an_Egocentric_Human_Interaction_Dataset_for_Interactive_AI_Assistants_ICCV_2023_paper.html) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://openaccess.thecvf.com/content/ICCV2023/html/Wang_HoloAssist_an_Egocentric_Human_Interaction_Dataset_for_Interactive_AI_Assistants_ICCV_2023_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/Ember-HoloAssist/holoassist-release)

- **WEAR** (2023) — ~19 h outdoor sports; Activity + IMU.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://mariusbock.github.io/wear/)

- **N-EPIC-KITCHENS** (2022) — Event + RGB subset; Action, neuromorphic.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Plizzari_E2GOMOTION_Motion_Augmented_Event_Stream_for_Egocentric_Action_Recognition_CVPR_2022_paper.html) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Plizzari_E2GOMOTION_Motion_Augmented_Event_Stream_for_Egocentric_Action_Recognition_CVPR_2022_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/EgocentricVision/N-EPIC-Kitchens)

- **Ego-Deliver** (2021) — 5,360 videos; Delivery ego analysis.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://egodeliver.github.io/EgoDeliver_Dataset/)

- **HOMAGE** (2021) — 30 h / compositional; Home activities.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2021/html/Rai_Home_Action_Genome_Cooperative_Compositional_Action_Understanding_CVPR_2021_paper.html) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://openaccess.thecvf.com/content/CVPR2021/html/Rai_Home_Action_Genome_Cooperative_Compositional_Action_Understanding_CVPR_2021_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/nishantrai18/homage)

- **MECCANO** (2021) — ~55 h industrial; HOI, ego.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://iplab.dmi.unict.it/MECCANO/) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/fpv-iplab/MECCANO)

- **EGO-CH** (2020) — 27+ h, cultural sites; Visitor behavior, POI tasks.

- **EgoCom** (2020) — 38.5 h conversation; Multiperson ego dialog.
  [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/facebookresearch/EgoCom-Dataset)

- **LEMMA** (2020) — Multi-view activities; Multi-agent tasks.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://sites.google.com/view/lemma-activity) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/Buzz-Beater/LEMMA)

- **Charades-Ego** (2018) — Paired ego / exo; Alignment, actions.
  [![arXiv](https://img.shields.io/badge/arXiv-1804.09626-b31b1b.svg)](https://arxiv.org/abs/1804.09626) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/1804.09626)

- **EGTEA Gaze+** (2018) — 28 h cooking; Gaze + action recognition.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://cbs.ic.gatech.edu/fpv/)

- **EgoGesture** (2017) — 2K+ videos / 24K samples; Gesture recognition.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://nlpr.ia.ac.cn/iva/yfzhang/datasets/egogesture.html)

- **Stanford ECM** (2017) — 31 hours, augmented with heart rate and accelerometer, 23–24 daily activity categories; action & activity recognition.

- **THU-READ** (2017) — 1,920 clips (8 subjects × 40 actions × 3 reps × 2 modalities), RGB-D from helmet-mounted sensor; action & activity recognition.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://ivg.au.tsinghua.edu.cn/dataset/THU_READ.php)

- **PEV (UTokyo Paired Ego-Video)** (2016) — 1,226 pairs of first-person clips, synchronous dyadic conversations, 8 interaction categories, 6 subjects; action & activity recognition.

- **FPPA** (2015) — 5 subjects, 5 daily actions, egocentric video with hand and gaze cues; action & activity recognition.

- **JPL-Interaction** (2013) — 84 videos, 7 activity types (4 positive, 1 neutral, 2 negative interactions), 320×240@30 fps; action & activity recognition.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](http://michaelryoo.com/jpl-interaction.html)

- **ADL** (2012) — ~10 h, 20 participants; ADL recognition, objects.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://www.csee.umbc.edu/~hpirsiav/papers/ADLdataset/)

- **Social Interactions** (2012) — 8 social events, ~60 hours, head-mounted cameras, multiple participants per event; action & activity recognition.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://cbs.ic.gatech.edu/fpv/)

- **EgoAction** (2011) — First-person sports videos (skateboarding, skiing, cycling, etc; action & activity recognition.

- *Ego-Exo4D — see [3D Scene Understanding & Localization](#-3d-scene-understanding--localization)*
- *EgoExoLearn — see [Procedural Activities & Skill Learning](#-procedural-activities--skill-learning)*

### Benchmarks built on these datasets

| Benchmark | Capability | Primary data | Official link | Notes |
|-----------|------------|--------------|---------------|-------|
| E³ (Exploring Embodied Emotion) | Emotion recognition, classification, localization, reasoning | E³ | [GitHub](https://github.com/Exploring-Embodied-Emotion-official/E3) | Standalone |
| EGOFALLS | Fall detection (visual + audio) | EGOFALLS | [Dataverse](https://www.dataverse.nl/dataset.xhtml?persistentId=doi:10.34894/HO5GE3) | Standalone |
| Ego4D | Action, forecasting, VQA, narration, … | Ego4D | [Site](https://ego4d-data.org/) | Suite |
| EPIC-KITCHENS-100 | Action recognition, detection, anticipation, … | EPIC-KITCHENS-100 | [Site](https://epic-kitchens.github.io/) | Suite |
| EgoGesture | Egocentric hand gesture recognition | EgoGesture | [Site](https://nlpr.ia.ac.cn/iva/yfzhang/datasets/egogesture.html) | Standalone |

## ✋ Hand–Object Interaction, Dexterity & 3D

> This section focuses on egocentric hands, dexterous manipulation, object interaction, tracking, and dense 3D understanding around the body and manipulated objects.

### Datasets at a glance

| Name | Year | Scale | Key tasks | Paper | Link |
|------|------|-------|-----------|-------|------|
| ⭐ AssemblyHands | 2023 | 3M images / hands | 3D hand pose, assembly | [Paper](https://openaccess.thecvf.com/content/CVPR2023/html/Ohkawa_AssemblyHands_Towards_Egocentric_Activity_Understanding_via_3D_Hand_Pose_Estimation_CVPR_2023_paper.html) | [Site](https://assemblyhands.github.io/) |
| ⭐ HOI4D | 2022 | 2.4M frames / 4K seq. | 4D HOI | [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Liu_HOI4D_A_4D_Egocentric_Dataset_for_Category-Level_Human-Object_Interaction_CVPR_2022_paper.html) | [Site](https://hoi4d.github.io/) |
| ⭐ FPHA | 2018 | 1.2K seq. hand action | Hand pose + action | [Paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Garcia-Hernando_First-Person_Hand_Action_CVPR_2018_paper.html) | [Site](https://guiggh.github.io/publications/first-person-hands/) |
| FEEL | 2026 | Force-sync kitchen ego video | Physical action understanding | [Paper](https://arxiv.org/abs/2603.15847) | [Site](https://www.cs.umd.edu/~edessale/feel) |
| EgoDex | 2025 | 829 h / 30K trajectories | Dexterous manipulation, pose | [Paper](https://arxiv.org/abs/2505.11709) | [GitHub](https://github.com/apple/ml-egodex) |
| EgoPoints | 2025 | Point tracks + synthetic | Tracking in ego video | [Paper](https://arxiv.org/abs/2412.04592) | [GitHub](https://github.com/AhmadDarKhalil/EgoPoints) |
| EgoObjects | 2023 | 9.2K+ videos | Detection, instance seg | [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Zhu_EgoObjects_A_Large-Scale_Egocentric_Dataset_for_Object_Detection_and_Instance_ICCV_2023_paper.html) | [GitHub](https://github.com/facebookresearch/EgoObjects) |
| ENIGMA-51 | 2023 | 22 h industrial | Fine-grained behavior | N/A | [Site](https://fpv-iplab.github.io/ENIGMA-51/) |
| POV-Surgery | 2023 | ~88K frames, 53 seq. (synth.) | Surgical hand–tool pose, segmentation | N/A | [Site](https://batfacewayne.github.io/POV_Surgery_io/) |
| VOST | 2023 | 713 videos | VOS, transforming objects | N/A | [Site](https://www.vostdataset.org/) |
| EgoBody | 2022 | 125 seq. / multi-view | Body pose, interaction | N/A | [Site](https://egobody.ethz.ch/) |
| EgoHOS | 2022 | 11K+ images | Hand–object segmentation | N/A | [GitHub](https://github.com/owenzlz/EgoHOS) |
| EgoPAT3D | 2022 | 1M+ frames RGB-D | 3D action target prediction | [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Li_Egocentric_Prediction_of_Action_Target_in_3D_CVPR_2022_paper.html) | [Site](https://ai4ce.github.io/EgoPAT3D/) |
| Touch and Go | 2022 | 12K+ vis–tactile frames | Vision + touch | N/A | [Site](https://touch-and-go.github.io/) |
| VISOR | 2022 | EPIC + masks / relations | Segmentation, HOI | N/A | [Site](https://epic-kitchens.github.io/VISOR) |
| H2O | 2021 | 100K+ frames | Two-hand interaction | [Paper](https://openaccess.thecvf.com/content/ICCV2021/html/Kwon_H2O_Two_Hands_Manipulating_Objects_for_First_Person_Interaction_Recognition_ICCV_2021_paper.html) | [Site](https://h2odataset.ethz.ch/) |
| TREK-150 | 2021 | 150 EPIC seq. | Object tracking | N/A | [Site](https://machinelearning.uniud.it/datasets/trek150/) |
| You2Me | 2020 | 14 seq., chest-mounted GoPro | Body pose via ego–exo interaction | N/A | [GitHub](https://github.com/facebookresearch/you2me) |
| EgoDexter | 2017 | ~3.2K frames, 4 seq. | Hand tracking under occlusion | N/A | [Site](https://handtracker.mpi-inf.mpg.de/projects/OccludedHands/EgoDexter.htm) |
| EgoHands | 2015 | 4.8K labeled frames | Hand detection / boxes | N/A | [Site](http://vision.soic.indiana.edu/projects/egohands/) |
| BEOID | 2014 | 58 videos, 6 environments, 34 object interaction classes, ~30 fps | hand–object interaction, dexterity & 3d | N/A | [Site](https://data.bris.ac.uk/data/dataset/3wats8ruq1sp52hq3bo8dkzul3) |
| EDSH | 2013 | 2 videos (~5 min each), pixel-level hand segmentation, egocentric daily activities | hand–object interaction, dexterity & 3d | N/A | [Site](http://www.cs.cmu.edu/~kkitani/datasets/) |
| Handled Objects | 2009 | 11 object categories, multiple grasp sequences, RGB + depth from wearable camera | hand–object interaction, dexterity & 3d | N/A | N/A |

### Entries

- [⭐️] **AssemblyHands** (2023) — 3M egocentric hand images on top of Assembly101 for detailed 3D hand pose estimation during assembly.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2023/html/Ohkawa_AssemblyHands_Towards_Egocentric_Activity_Understanding_via_3D_Hand_Pose_Estimation_CVPR_2023_paper.html) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://openaccess.thecvf.com/content/CVPR2023/html/Ohkawa_AssemblyHands_Towards_Egocentric_Activity_Understanding_via_3D_Hand_Pose_Estimation_CVPR_2023_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/facebookresearch/assemblyhands-toolkit)

- [⭐️] **HOI4D** (2022) — 2.4M RGB-D frames with object poses, hand poses, interaction regions, and motion segmentation for category-level 4D HOI.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Liu_HOI4D_A_4D_Egocentric_Dataset_for_Category-Level_Human-Object_Interaction_CVPR_2022_paper.html) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Liu_HOI4D_A_4D_Egocentric_Dataset_for_Category-Level_Human-Object_Interaction_CVPR_2022_paper.html)

- [⭐️] **FPHA** (2018) — 1,175 RGB-D sequences with 3D hand pose and action labels; a foundational first-person hand-action benchmark.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://openaccess.thecvf.com/content_cvpr_2018/html/Garcia-Hernando_First-Person_Hand_Action_CVPR_2018_paper.html) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://openaccess.thecvf.com/content_cvpr_2018/html/Garcia-Hernando_First-Person_Hand_Action_CVPR_2018_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/guiggh/hand_pose_action)

- **FEEL** (2026) — Force-sync kitchen ego video; Physical action understanding.
  [![arXiv](https://img.shields.io/badge/arXiv-2603.15847-b31b1b.svg)](https://arxiv.org/abs/2603.15847) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2603.15847)

- **EgoDex** (2025) — 829 h / 30K trajectories; Dexterous manipulation, pose.
  [![arXiv](https://img.shields.io/badge/arXiv-2505.11709-b31b1b.svg)](https://arxiv.org/abs/2505.11709) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2505.11709) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/apple/ml-egodex)

- **EgoPoints** (2025) — Point tracks + synthetic; Tracking in ego video.
  [![arXiv](https://img.shields.io/badge/arXiv-2412.04592-b31b1b.svg)](https://arxiv.org/abs/2412.04592) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2412.04592) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/AhmadDarKhalil/EgoPoints)

- **EgoObjects** (2023) — 9.2K+ videos; Detection, instance seg.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://openaccess.thecvf.com/content/ICCV2023/html/Zhu_EgoObjects_A_Large-Scale_Egocentric_Dataset_for_Object_Detection_and_Instance_ICCV_2023_paper.html) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://openaccess.thecvf.com/content/ICCV2023/html/Zhu_EgoObjects_A_Large-Scale_Egocentric_Dataset_for_Object_Detection_and_Instance_ICCV_2023_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/facebookresearch/EgoObjects)

- **ENIGMA-51** (2023) — 22 h industrial; Fine-grained behavior.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://fpv-iplab.github.io/ENIGMA-51/) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/fpv-iplab/ENIGMA-51)

- **POV-Surgery** (2023) — ~88K frames, 53 seq. (synth.); Surgical hand–tool pose, segmentation.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://batfacewayne.github.io/POV_Surgery_io/) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/BatFaceWayne/POV_Surgery)

- **VOST** (2023) — 713 videos; VOS, transforming objects.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://www.vostdataset.org/) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/yka-dl/VOST)

- **EgoBody** (2022) — 125 seq. / multi-view; Body pose, interaction.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://egobody.ethz.ch/)

- **EgoHOS** (2022) — 11K+ images; Hand–object segmentation.
  [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/owenzlz/EgoHOS)

- **EgoPAT3D** (2022) — 1M+ frames RGB-D; 3D action target prediction.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Li_Egocentric_Prediction_of_Action_Target_in_3D_CVPR_2022_paper.html) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Li_Egocentric_Prediction_of_Action_Target_in_3D_CVPR_2022_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/ai4ce/EgoPAT3D)

- **Touch and Go** (2022) — 12K+ vis–tactile frames; Vision + touch.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://touch-and-go.github.io/) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/fredfyyang/Touch-and-Go)

- **VISOR** (2022) — EPIC + masks / relations; Segmentation, HOI.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://epic-kitchens.github.io/VISOR) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/epic-kitchens/VISOR)

- **H2O** (2021) — 100K+ frames; Two-hand interaction.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://openaccess.thecvf.com/content/ICCV2021/html/Kwon_H2O_Two_Hands_Manipulating_Objects_for_First_Person_Interaction_Recognition_ICCV_2021_paper.html) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://openaccess.thecvf.com/content/ICCV2021/html/Kwon_H2O_Two_Hands_Manipulating_Objects_for_First_Person_Interaction_Recognition_ICCV_2021_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/taeinkwon/h2odataset)

- **TREK-150** (2021) — 150 EPIC seq; Object tracking.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://machinelearning.uniud.it/datasets/trek150/) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/matteo-dunnhofer/TREK-150-toolkit)

- **You2Me** (2020) — 14 seq., chest-mounted GoPro; Body pose via ego–exo interaction.
  [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/facebookresearch/you2me)

- **EgoDexter** (2017) — ~3.2K frames, 4 seq; Hand tracking under occlusion.
  [![Project](https://img.shields.io/badge/Project-Link-blue.svg)](https://handtracker.mpi-inf.mpg.de/projects/OccludedHands/EgoDexter.htm)

- **EgoHands** (2015) — 4.8K labeled frames; Hand detection / boxes.
  [![Project](https://img.shields.io/badge/Project-Link-blue.svg)](http://vision.soic.indiana.edu/projects/egohands/)

- **BEOID** (2014) — 58 videos, 6 environments, 34 object interaction classes, ~30 fps; hand–object interaction, dexterity & 3d.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://data.bris.ac.uk/data/dataset/3wats8ruq1sp52hq3bo8dkzul3)

- **EDSH** (2013) — 2 videos (~5 min each), pixel-level hand segmentation, egocentric daily activities; hand–object interaction, dexterity & 3d.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](http://www.cs.cmu.edu/~kkitani/datasets/)

- **Handled Objects** (2009) — 11 object categories, multiple grasp sequences, RGB + depth from wearable camera; hand–object interaction, dexterity & 3d.

### Benchmarks built on these datasets

| Benchmark | Capability | Primary data | Official link | Notes |
|-----------|------------|--------------|---------------|-------|
| AssemblyHands | Egocentric 3D hand pose | Assembly101 | [Site](https://assemblyhands.github.io/) | Standalone |
| VISOR | Video object segmentation, hand–object relations | EPIC-KITCHENS | [Site](https://epic-kitchens.github.io/VISOR) | Standalone |
| TREK-150 | Egocentric single-object tracking | EPIC-KITCHENS | [Site](https://machinelearning.uniud.it/datasets/trek150/) | Standalone |
| FPHA | Hand action + 3D hand pose | FPHA | [Site](https://guiggh.github.io/publications/first-person-hands/) | Standalone |

## 📋 Procedural Activities & Skill Learning

> Datasets centered on step structure, instructional execution, assembly, or skill transfer from egocentric experience are grouped here.

### Datasets at a glance

| Name | Year | Scale | Key tasks | Paper | Link |
|------|------|-------|-----------|-------|------|
| EgoYC2 / Exo2EgoDVC | 2025 | ~43 h cooking | Dense captioning, procedural | [Paper](https://arxiv.org/abs/2311.16444) | [GitHub](https://github.com/ut-vision/Exo2EgoDVC) |
| EgoExoLearn | 2024 | 120 h ego+exo | Procedural, async views | [Paper](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_EgoExoLearn_A_Dataset_for_Bridging_Asynchronous_Ego-_and_Exo-centric_View_CVPR_2024_paper.html) | [GitHub](https://github.com/OpenGVLab/EgoExoLearn) |
| IndustReal | 2024 | ~6 h industrial | Procedure steps, errors | N/A | [Site](https://timschoonbeek.github.io/industreal.html) |
| Assembly101 | 2022 | 513 h multiview | Assembly, procedure | [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Sener_Assembly101_A_Large-Scale_Multi-View_Video_Dataset_for_Understanding_Procedural_Activities_CVPR_2022_paper.html) | [Site](https://assembly-101.github.io/) |
| EgoProceL | 2022 | 62 videos / 16 tasks | Procedure learning | N/A | [Site](https://sid2697.github.io/egoprocel/) |
| EPIC-Tent | 2019 | 7+ h, tent assembly | Procedural, dual HMD + gaze | N/A | [Site](https://data.bris.ac.uk/data/dataset/2ite3tu1u53n42hjfh3886sa86) |
| CMU-MMAC | 2011 | 25 subjects, 5 cooking recipes | procedural activities & skill learning | N/A | [Site](http://kitchen.cs.cmu.edu/) |
| GTEA Gaze | 2011 | 17 meal preparation sessions, 7 cooking activities, gaze tracking annotations | procedural activities & skill learning | N/A | [Site](https://cbs.ic.gatech.edu/fpv/) |

### Entries

- **EgoYC2 / Exo2EgoDVC** (2025) — ~43 h cooking; Dense captioning, procedural.
  [![arXiv](https://img.shields.io/badge/arXiv-2311.16444-b31b1b.svg)](https://arxiv.org/abs/2311.16444) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2311.16444) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/ut-vision/Exo2EgoDVC)

- **EgoExoLearn** (2024) — 120 h ego+exo; Procedural, async views.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_EgoExoLearn_A_Dataset_for_Bridging_Asynchronous_Ego-_and_Exo-centric_View_CVPR_2024_paper.html) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_EgoExoLearn_A_Dataset_for_Bridging_Asynchronous_Ego-_and_Exo-centric_View_CVPR_2024_paper.html) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/OpenGVLab/EgoExoLearn) [![🤗](https://img.shields.io/badge/%F0%9F%A4%97-Dataset-yellow.svg)](https://huggingface.co/datasets/hyf015/EgoExoLearn)

- **IndustReal** (2024) — ~6 h industrial; Procedure steps, errors.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://timschoonbeek.github.io/industreal.html)

- **Assembly101** (2022) — 513 h multiview; Assembly, procedure.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Sener_Assembly101_A_Large-Scale_Multi-View_Video_Dataset_for_Understanding_Procedural_Activities_CVPR_2022_paper.html) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://openaccess.thecvf.com/content/CVPR2022/html/Sener_Assembly101_A_Large-Scale_Multi-View_Video_Dataset_for_Understanding_Procedural_Activities_CVPR_2022_paper.html)

- **EgoProceL** (2022) — 62 videos / 16 tasks; Procedure learning.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://sid2697.github.io/egoprocel/) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/Sid2697/EgoProceL-egocentric-procedure-learning)

- **EPIC-Tent** (2019) — 7+ h, tent assembly; Procedural, dual HMD + gaze.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://data.bris.ac.uk/data/dataset/2ite3tu1u53n42hjfh3886sa86) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/youngkyoonjang/EPIC_Tent2019)

- **CMU-MMAC** (2011) — 25 subjects, 5 cooking recipes; procedural activities & skill learning.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](http://kitchen.cs.cmu.edu/)

- **GTEA Gaze** (2011) — 17 meal preparation sessions, 7 cooking activities, gaze tracking annotations; procedural activities & skill learning.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://cbs.ic.gatech.edu/fpv/)

- *Ego-Exo4D — see [3D Scene Understanding & Localization](#-3d-scene-understanding--localization)*
- *HowToDIV — see [VLMs, Instructions & QA](#-vlms-instructions--qa)*
- *ADT (Aria Digital Twin) — see [3D Scene Understanding & Localization](#-3d-scene-understanding--localization)*

### Benchmarks built on these datasets

| Benchmark | Capability | Primary data | Official link | Notes |
|-----------|------------|--------------|---------------|-------|
| None listed | — | — | — | — |

## 🗺️ 3D Scene Understanding & Localization

> These datasets emphasize geometry, localization, scene graphs, multiview capture, or machine-perception tasks grounded in ego video.

### Datasets at a glance

| Name | Year | Scale | Key tasks | Paper | Link |
|------|------|-------|-----------|-------|------|
| ⭐ Ego-Exo4D | 2024 | 1,286+ h ego+exo | Skilled activity, many tasks | [Paper](https://arxiv.org/abs/2311.18259) | [Site](https://ego-exo4d-data.org/) |
| ADT (Aria Digital Twin) | 2023 | 200 seq., 2 scenes | Egocentric 3D perception | [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Pan_Aria_Digital_Twin_A_New_Benchmark_Dataset_for_Egocentric_3D_Machine_ICCV_2023_paper.html) | [Site](https://www.projectaria.com/datasets/adt/) |
| PVSG | 2023 | 400 vids, ~150K frames | Panoptic video scene graph (ego + third-person) | N/A | [Site](https://jingkang50.github.io/PVSG/) |
| DR(eye)VE | 2018 | ~6 h driving, 555K frames | Gaze prediction, driving ego video | N/A | [Site](http://aimagelab.ing.unimore.it/dreyeve) |
| EgoCart | 2018 | Retail RGB-D, 9 videos | Indoor / cart localization | N/A | [Site](https://iplab.dmi.unict.it/EgocentricShoppingCartLocalization/) |
| IU ShareView | 2018 | 9 paired ego video sets | Person seg / ID across synchronized wearers | N/A | [Site](http://vision.soic.indiana.edu/firstthird-eccv2018/) |
| OST | 2017 | 57 sequences, 55 subjects, ~15 min/video, egocentric object search tasks, eye-tracking ground truth | 3d scene understanding & localization | N/A | [GitHub](https://github.com/Mengmi/deepfuturegaze_gan) |

### Entries

- [⭐️] **Ego-Exo4D** (2024) — 1,286+ h of paired first- and third-person skilled activity with multiview geometry and a broad benchmark suite.
  [![arXiv](https://img.shields.io/badge/arXiv-2311.18259-b31b1b.svg)](https://arxiv.org/abs/2311.18259) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://arxiv.org/abs/2311.18259)

- **ADT (Aria Digital Twin)** (2023) — 200 seq., 2 scenes; Egocentric 3D perception.
  [![Paper](https://img.shields.io/badge/Paper-Link-b31b1b.svg)](https://openaccess.thecvf.com/content/ICCV2023/html/Pan_Aria_Digital_Twin_A_New_Benchmark_Dataset_for_Egocentric_3D_Machine_ICCV_2023_paper.html) [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://openaccess.thecvf.com/content/ICCV2023/html/Pan_Aria_Digital_Twin_A_New_Benchmark_Dataset_for_Egocentric_3D_Machine_ICCV_2023_paper.html) [![🤗](https://img.shields.io/badge/%F0%9F%A4%97-Dataset-yellow.svg)](https://huggingface.co/datasets/projectaria/aria-digital-twin)

- **PVSG** (2023) — 400 vids, ~150K frames; Panoptic video scene graph (ego + third-person).
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://jingkang50.github.io/PVSG/) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/LilyDaytoy/OpenPVSG)

- **DR(eye)VE** (2018) — ~6 h driving, 555K frames; Gaze prediction, driving ego video.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](http://aimagelab.ing.unimore.it/dreyeve) [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/ndrplz/dreyeve)

- **EgoCart** (2018) — Retail RGB-D, 9 videos; Indoor / cart localization.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](https://iplab.dmi.unict.it/EgocentricShoppingCartLocalization/)

- **IU ShareView** (2018) — 9 paired ego video sets; Person seg / ID across synchronized wearers.
  [![Site](https://img.shields.io/badge/Site-Link-blue.svg)](http://vision.soic.indiana.edu/firstthird-eccv2018/)

- **OST** (2017) — 57 sequences, 55 subjects, ~15 min/video, egocentric object search tasks, eye-tracking ground truth; 3d scene understanding & localization.
  [![Code](https://img.shields.io/badge/Code-GitHub-black.svg)](https://github.com/Mengmi/deepfuturegaze_gan)

- *Ego-1K — see [Video Generation & World-Model Pretraining](#-video-generation--world-model-pretraining)*

### Benchmarks built on these datasets

| Benchmark | Capability | Primary data | Official link | Notes |
|-----------|------------|--------------|---------------|-------|
| Ego-Exo4D | Ego–exo skill understanding, many tasks | Ego-Exo4D | [Site](https://ego-exo4d-data.org/) | Suite |
| ADT (Aria Digital Twin) | Egocentric 3D machine perception | ADT | [Aria](https://www.projectaria.com/datasets/adt/) | Dataset+benchmark |

## 🛠️ Tools & Libraries

| Name | Description | Link |
|------|-------------|------|
| Ego4D CLI | Official downloader and tooling for accessing Ego4D releases. | [GitHub](https://github.com/facebookresearch/Ego4d) |
| HOMIE-toolkit | Toolkit released with Ropedia Xperience-10M for large-scale multimodal ego data. | [GitHub](https://github.com/Ropedia/HOMIE-toolkit) |
| AssemblyHands Toolkit | Official toolkit for the AssemblyHands benchmark. | [GitHub](https://github.com/facebookresearch/assemblyhands-toolkit) |
| TREK-150 Toolkit | Toolkit for the TREK-150 egocentric tracking benchmark. | [GitHub](https://github.com/matteo-dunnhofer/TREK-150-toolkit) |

## 🔗 Related Awesome Lists

- [Awesome-Egocentric](https://github.com/EgoAlpha/Awesome-Egocentric)
- [awesome-egocentric-vision](https://github.com/Sid2697/awesome-egocentric-vision)
- [Awesome-Egocentric-and-Exocentric-Vision](https://github.com/ayiyayi/Awesome-Egocentric-and-Exocentric-Vision)

## 🤝 Contributing

1. Add or update the dataset, benchmark, or survey directly in the matching section of `README.md`.
2. Keep primary entries unique: one full entry under one topic, cross-links everywhere else.
3. Preserve newest-to-oldest ordering inside each topic block, with flagship entries kept at the top.
4. Follow the detailed checklist in [CONTRIBUTING.md](CONTRIBUTING.md) before opening a PR.

## License

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). See [LICENSE](LICENSE).
