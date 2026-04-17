# Single-README Refactor Design

**Date:** 2026-04-17
**Scope:** Collapse the multi-file repo into one README, restyled in the
[`DravenALG/awesome-vla-wam`](https://github.com/DravenALG/awesome-vla-wam)
visual style while preserving the existing 7-task taxonomy and dataset content.

---

## Goals

1. **Single source of truth.** All content lives in `README.md`. No `tasks/`
   subdirectory, no `datasets.md`, no `benchmarks.md`.
2. **Topic-first navigation.** The 7 existing task categories become the
   primary axis; chronological ordering is preserved *within* each section.
3. **Visual upgrade.** Hero banner, centered title, emoji topic headers,
   shield badges per entry, ⭐ markers on flagship datasets.

## Non-goals

- Adding new datasets or benchmarks. This refactor is structural.
- Changing the taxonomy itself. Keep the current 7 task categories.
- Inventing analytics, leaderboards, or scripts.

---

## File layout (after refactor)

```
README.md                          ← single source of truth
banner.png                         ← hero image (already in repo)
LICENSE                            ← keep (CC0-1.0)
CONTRIBUTING.md                    ← keep, updated to point at README sections
.github/PULL_REQUEST_TEMPLATE.md   ← keep
docs/plans/2026-04-17-...md        ← this design doc
```

**Removed:** `datasets.md`, `benchmarks.md`, `tasks/` (7 files).

---

## README skeleton

```markdown
<div align="center">

# 🎥 Awesome Egocentric Video Datasets

**📜 A Curated List of Egocentric (First-Person) Video Datasets, Benchmarks, and Tools**

<p align="center">
  <img src="banner.png" alt="Awesome Egocentric Video Datasets" width="100%"
       style="border-radius: 15px; box-shadow: 0 4px 24px rgba(0,0,0,.1); margin: 5px 0;">
</p>

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)

</div>

## Overview

- 🎯 [Aim](#aim) | 📚 [Papers & Surveys](#papers--surveys)

**Datasets by Task**
- 🎬 [Video Generation & World-Model Pretraining](#-video-generation--world-model-pretraining)
- 🧠 [Memory, Summarization & Long-form Understanding](#-memory-summarization--long-form-understanding)
- 💬 [VLMs, Instructions & QA](#-vlms-instructions--qa)
- 🏃 [Action & Activity Recognition](#-action--activity-recognition)
- ✋ [Hand–Object Interaction, Dexterity & 3D](#-handobject-interaction-dexterity--3d)
- 📋 [Procedural Activities & Skill Learning](#-procedural-activities--skill-learning)
- 🗺️ [3D Scene Understanding & Localization](#-3d-scene-understanding--localization)

**Resources**
- 🛠️ [Tools & Libraries](#-tools--libraries) | 🔗 [Related Lists](#-related-awesome-lists) | 🤝 [Contributing](#-contributing) | 📄 [License](#license)

## Aim
... 1 short paragraph ...

## Papers & Surveys
... 8–10 entries, newest → oldest, ⭐ on flagship surveys, badge style ...

## 🎬 Video Generation & World-Model Pretraining
... topic block (template below) ...

## 🧠 Memory, Summarization & Long-form Understanding
...

## 💬 VLMs, Instructions & QA
...

## 🏃 Action & Activity Recognition
...

## ✋ Hand–Object Interaction, Dexterity & 3D
...

## 📋 Procedural Activities & Skill Learning
...

## 🗺️ 3D Scene Understanding & Localization
...

## 🛠️ Tools & Libraries
... table ...

## 🔗 Related Awesome Lists
... bullet list ...

## 🤝 Contributing
... 4-step instructions + link to CONTRIBUTING.md ...

## License
... CC0 ...
```

---

## Topic section template

Each of the 7 topic sections follows this exact 3-block layout:

```markdown
## 🏃 Action & Activity Recognition

> One-sentence framing of what belongs in this section.

### Datasets at a glance

| Name | Year | Scale | Key tasks | Paper | Link |
|------|------|-------|-----------|-------|------|
| ⭐ EPIC-KITCHENS-100 | 2021 | 100 h / 90K segments | recognition, detection, anticipation | [arXiv](…) | [Site](…) |
| ⭐ Ego4D | 2022 | ~3,670 h | many | [arXiv](…) | [Site](…) |
| EgoDex | 2025 | 829 h / 30K traj. | dexterous manipulation | [arXiv](…) | [GitHub](…) |
| ... newest → oldest within section ...

### Entries

- [⭐️] **EPIC-KITCHENS-100** (2021) — 100 hours of unscripted kitchen activity; canonical action-recognition benchmark in egocentric vision.
  [![Paper](https://img.shields.io/badge/IJCV-2021-b31b1b.svg)](…) [![Site](https://img.shields.io/badge/Site-Link-blue)](…) [![Code](https://img.shields.io/badge/Code-GitHub-black)](…)

- [⭐️] **Ego4D** (2022) — 3,670 h, 9 countries; AR / VQA / forecasting suite.
  [![arXiv](https://img.shields.io/badge/arXiv-2110.07058-b31b1b.svg)](https://arxiv.org/abs/2110.07058) [![Site](https://img.shields.io/badge/Site-Link-blue)](https://ego4d-data.org/)

- *AssemblyHands — see [Hand–Object Interaction](#-handobject-interaction-dexterity--3d)*  ← cross-link, no duplicate

### Benchmarks built on these datasets

| Benchmark | Capability | Primary data | Official link | Notes |
|-----------|------------|--------------|---------------|-------|
| EPIC-KITCHENS-100 | recognition, detection, anticipation | EPIC-KITCHENS-100 | [Site](…) | Suite |
| Ego4D | many | Ego4D | [Site](…) | Suite |
```

**Within each block, ordering:** ⭐ flagship first, then newest → oldest.

---

## Per-entry conventions

- **Bullet line:** `- [⭐️] **Name** (Year) — one-sentence description. <badges>`
- **Cross-link line:** `- *Name — see [Topic](#anchor)*` (no badges, italic).
- **Badges (max 4 per entry, in this order):**
  - `arXiv` (red) — `https://img.shields.io/badge/arXiv-<id>-b31b1b.svg`
  - `Site` / `Project` (blue) — `https://img.shields.io/badge/Site-Link-blue`
  - `Code` (black) — `https://img.shields.io/badge/Code-GitHub-black`
  - `HuggingFace` (yellow) — `https://img.shields.io/badge/🤗-Dataset-yellow`
- **Flagship criteria (⭐):** widely cited, shipped a recognized benchmark, or
  set the scale frontier for its topic. Initial set: Ego4D, Ego-Exo4D,
  EPIC-KITCHENS-100, EgoSchema, HD-EPIC, AssemblyHands, HOI4D, FPHA,
  EgoVid-5M, Ropedia Xperience-10M, EgoLife.

---

## Cross-listing policy

A dataset belongs to **exactly one primary topic** (full row + full bullet).
In every other topic it touches, it appears **only** as a one-line cross-link.

### Multi-listed datasets — primary assignment

| Dataset | Currently in | Primary | Cross-linked from |
|---|---|---|---|
| EgoExoLearn | Action + Procedural | Procedural | Action |
| ADT | Procedural + Scene | 3D Scene | Procedural |
| Ego-1K | Scene + Generation | Generation | 3D Scene |
| HowToDIV | Procedural + VLM/QA | VLM/QA | Procedural |
| Ego-Exo4D | (Scene only today) | 3D Scene | Procedural, Action |

### Currently un-binned in `tasks/` — primary assignment

| Dataset | Year | Primary |
|---|---|---|
| EGO-CH | 2020 | Action & Activity |
| POV-Surgery | 2023 | Hand–Object |
| PVSG | 2023 | 3D Scene |
| VOST | 2023 | Hand–Object |
| DoMSEV | 2018 | Memory / Long-form |
| IU ShareView | 2018 | 3D Scene |
| You2Me | 2020 | Hand–Object |

### Per-topic counts (entries with full bullet)

| Topic | # Primary entries |
|---|---:|
| 🎬 Generation & World-Models | 7 |
| 🧠 Memory & Long-form | 5 |
| 💬 VLMs, Instructions & QA | 10 |
| 🏃 Action & Activity | 22 |
| ✋ Hand–Object & 3D HOI | 19 |
| 📋 Procedural & Skill | 8 |
| 🗺️ 3D Scene & Localization | 8 |

---

## Migration plan

1. **Branch:** `git checkout -b refactor/single-readme`.
2. **Build new `README.md` from scratch** using the templates above. Source:
   - `datasets.md` summary table → topic-level "Datasets at a glance" tables.
   - `datasets.md` detailed entries → compressed into one-line bullet
     descriptions.
   - `benchmarks.md` year tables → per-topic "Benchmarks" tables.
   - `tasks/*.md` → already a clean primary-topic mapping (with the
     reassignments in the table above applied).
3. **Promote ⭐ flagships** per the criteria above; reorder each block so
   flagships come first.
4. **Compress detail blocks.** The `datasets.md` rich blocks (Scale / Paper /
   Download multi-line tables) collapse into one descriptive sentence + 2–4
   shield badges per bullet. Where modality data is critical (e.g. 6 RGB
   streams + IMU + mocap for Ropedia Xperience-10M), keep one extra phrase in
   the description.
5. **Cross-links.** Every multi-topic dataset gets a one-line italic cross-link
   in non-primary topics. Verify GitHub auto-anchors (lowercase, hyphen-joined,
   punctuation stripped except `-`).
6. **`git rm`** legacy files: `datasets.md`, `benchmarks.md`, `tasks/`.
7. **Update `CONTRIBUTING.md`** to drop references to the removed files and
   point at the README sections instead.
8. **Verification pass:**
   - Every URL from the old files is preserved in `README.md` (or
     intentionally dropped — list the drops in the PR description).
   - Every dataset has exactly one primary entry.
   - Every cross-link resolves to an existing anchor.
   - Banner image renders.
9. **Commit + PR.**

---

## Risks

- **Information loss.** Per-dataset detailed tables (frame counts, modality
  breakdown) get compressed. Mitigation: keep one detail-rich line per bullet;
  link out to the project page for full specs.
- **Anchor stability.** GitHub auto-anchors are sensitive to header
  punctuation. Cross-links must be verified after the README is built.
- **Badge volume.** ~84 datasets × 2–4 badges = ~250 shield URLs to construct.
  Scriptable but tedious. Spot-check rendered output on GitHub before merging.
- **PR review surface.** A single ~1500-line README diff is hard to review.
  Mitigation: commit the design doc first (this file), then split the
  refactor into 2 commits — (a) build new README in a new path, (b) `git mv`
  + delete legacy files.

---

## Acceptance criteria

- `README.md` exists and renders correctly on GitHub with banner.
- `datasets.md`, `benchmarks.md`, `tasks/` no longer exist.
- All 7 topic sections present, each with the 3-block layout.
- Every dataset listed in the old `datasets.md` summary table is reachable
  from at least one topic section in the new README.
- Every benchmark listed in the old `benchmarks.md` is reachable from the
  benchmark table inside its topic.
- ⭐ flagships appear at the top of their respective tables / bullet lists.
- `CONTRIBUTING.md` describes the new 4-step PR flow.
