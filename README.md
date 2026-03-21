# Awesome Ego Video Datasets

以**第一人称（egocentric）视频**为中心的公开数据集索引。每条目仅关联**数据集官方说明与配套论文**；按**下游任务**分子页面维护，任务列表内**非代表性**数据集按**发布年份从新到旧**排列。

## 元数据字段（条目模板）

新增数据集时请尽量补齐下表字段，便于长期维护与检索。

| 字段 | 说明 |
|------|------|
| **Year** | 数据集或配套论文首次公开发表年份 |
| **Scale** | 时长、片段数、参与者数等（与论文一致） |
| **Video** | 分辨率、帧率、机位数量等 |
| **Other modalities** | 音频、深度、IMU、眼动、语言转写等（无则写「—」） |
| **Benchmark / task** | 该条目主要服务的评测或任务类型 |
| **Paper** | 数据集主论文（bib 或官方引用页） |
| **Official** | 项目页、下载入口或申请说明 |

---

## 代表性数据集与配套论文

下列为社区常用**综合基准或历史代表性**工作，单独列出，**不参与**各任务页中的时间线排序。

### Ego4D (2021 / CVPR 2022)

| 字段 | 内容 |
|------|------|
| **Scale** | 约 3,670 小时日常活动视频，931 名佩戴者，多国多场景 |
| **Other modalities** | 音频、3D、眼动、多机位等（以官方说明为准） |
| **Paper** | Grauman, K. et al. [Ego4D: Around the World in 3,000 Hours of Egocentric Video](https://arxiv.org/abs/2110.07058). CVPR 2022 |
| **Official** | [ego4d-data.org](https://ego4d-data.org/) · [Ego4d (GitHub)](https://github.com/facebookresearch/Ego4d) |

### Ego-Exo4D (CVPR 2024)

| 字段 | 内容 |
|------|------|
| **Scale** | 千级小时级 ego + exo 同步视频，多技能、多场景（以官方统计为准） |
| **Other modalities** | 音频、眼动、点云、IMU 等 |
| **Paper** | Grauman, K. et al. [Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives](https://arxiv.org/abs/2311.18259). CVPR 2024 |
| **Official** | [ego-exo4d-data.org](https://ego-exo4d-data.org/) |

### EPIC-KITCHENS-100 (2021)

| 字段 | 内容 |
|------|------|
| **Scale** | 100 小时、约 90K 动作片段、多厨房场景 |
| **Paper** | Damen, D. et al. [Rescaling Egocentric Vision: Collection, Pipeline and Challenges for EPIC-KITCHENS-100](https://epic-kitchens.github.io/public/ek100.pdf). IJCV 2021 |
| **Official** | [epic-kitchens.github.io](https://epic-kitchens.github.io/) · [Annotations](https://github.com/epic-kitchens/epic-kitchens-100-annotations) |

### Charades-Ego (2018)

| 字段 | 内容 |
|------|------|
| **Scale** | 大规模配对第三人称与第一人称视频 |
| **Paper** | Sigurdsson, G.A. et al. [Charades-Ego: A Large-Scale Dataset of Paired Third and First Person Videos](https://arxiv.org/abs/1804.09626) |
| **Official** | 见论文与项目页（历史数据请以作者说明为准） |

---

## 按下游任务浏览

| 任务方向 | 文件 |
|----------|------|
| 视频生成与世界模型预训练 | [tasks/video-generation.md](tasks/video-generation.md) |
| 视频记忆、摘要与长时序理解 | [tasks/video-memory.md](tasks/video-memory.md) |
| VLM、指令与问答 | [tasks/vlm-instruction-and-qa.md](tasks/vlm-instruction-and-qa.md) |
| 动作 / 活动识别与检测 | [tasks/action-and-activity.md](tasks/action-and-activity.md) |
| 手–物交互、灵巧操作与 3D | [tasks/hand-object-and-dexterity.md](tasks/hand-object-and-dexterity.md) |
| 程序性活动与技能学习 | [tasks/procedural-and-skill-learning.md](tasks/procedural-and-skill-learning.md) |

---

## 维护说明

- **排序**：各 `tasks/*.md` 内条目为**非代表性**数据集，按 **Year 降序**；同年份可再按 arXiv / 会议公开时间微调。
- **收录范围**：以**可指向的公开论文 + 官方获取渠道**（或明确申请流程）为准。
- **更新方式**：直接提交 PR 修改对应任务文件，或开 Issue 说明数据集名称与论文链接。
