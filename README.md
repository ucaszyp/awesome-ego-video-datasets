# Awesome Egocentric Video Datasets 🎥

> A curated list of high-quality egocentric (first-person) video datasets, associated papers, benchmarks, tools and resources.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) <!-- Optional: badge is standard for lists submitted to the main Awesome repo -->

## Table of Contents

- [Datasets](#datasets)
- [Datasets by Downstream Task](#datasets-by-downstream-task)
- [Papers & Surveys](#papers--surveys)
- [Benchmarks & Challenges](#benchmarks--challenges)
- [Tools & Libraries](#tools--libraries)
- [Related Awesome Lists](#related-awesome-lists)
- [Contributing](#contributing)
- [License](#license)

## Datasets

Entries use a single table, sorted by **year (newest first)**, then **name**. Scale and tasks are short summaries; see [`datasets.md`](datasets.md) for full per-dataset detail (paper references, exact scale, download links).

| Name | Year | Hours / clips (short) | Key tasks | Paper | Link |
|------|------|------------------------|-----------|-------|------|
| DreamDojo-HV | 2026 | Very large FP video (see paper) | World models, pretraining | [arXiv](https://arxiv.org/abs/2602.06949) | See paper / project |
| Ego-1K | 2026 | Multiview clips (~1K takes) | Neural 3D/4D synthesis | [arXiv](https://arxiv.org/abs/2603.13741) | [Hugging Face](https://huggingface.co/datasets/facebook/ego-1k) |
| EgoScale | 2026 | 20k+ h labeled manipulation (paper) | Action, dexterous transfer | [arXiv](https://arxiv.org/abs/2602.16710) | See paper |
| FEEL | 2026 | Force-sync kitchen ego video | Physical action understanding | [arXiv](https://arxiv.org/abs/2603.15847) | [Project](https://www.cs.umd.edu/~edessale/feel) |
| In-lab | 2026 | Lab tabletop trajectories | Skills, world models (w/ DreamDojo) | [arXiv](https://arxiv.org/abs/2602.06949) | See paper |
| Ropedia Xperience-10M | 2026 | Large multi-stream experiences | Multimodal ego learning | Dataset card | [Hugging Face](https://huggingface.co/datasets/ropedia-ai/xperience-10m) |
| EgoCampus | 2025 | ~32 h / campus paths (paper) | Gaze, pedestrian ego | [arXiv](https://arxiv.org/abs/2512.07668) | [GitHub](https://github.com/ComputerVisionRutgers/EgoCampus) |
| EgoDex | 2025 | 829 h / 30K trajectories | Dexterous manipulation, pose | [arXiv](https://arxiv.org/abs/2505.11709) | [GitHub](https://github.com/apple/ml-egodex) |
| EgoEdit | 2025 | 100K editing pairs | Egocentric video editing | [arXiv](https://arxiv.org/abs/2512.06065) | [Project](https://snap-research.github.io/EgoEdit) |
| EgoEMS | 2025 | 20+ h emergency scenarios | EMS QA, multimodal | [arXiv](https://arxiv.org/abs/2511.09894) | [GitHub](https://github.com/UVA-DSA/EgoEMS) |
| EgoLife | 2025 | ~266–300 h daily life | Long-form assistants, memory | [arXiv](https://arxiv.org/abs/2503.01773) | [Site](https://egolife-ai.github.io/) |
| EgoPoints | 2025 | Point tracks + synthetic | Tracking in ego video | [arXiv](https://arxiv.org/abs/2412.04592) | [GitHub](https://github.com/AhmadDarKhalil/EgoPoints) |
| EgoYC2 / Exo2EgoDVC | 2025 | ~43 h cooking | Dense captioning, procedural | [arXiv](https://arxiv.org/abs/2311.16444) | [GitHub](https://github.com/ut-vision/Exo2EgoDVC) |
| HD-EPIC | 2025 | ~41 h / dense labels | Fine-grained kitchen, VQA | [arXiv](https://arxiv.org/abs/2502.04144) | [Site](https://hd-epic.github.io/) |
| HowToDIV | 2025 | ~24 h instructional | Dialog, procedural QA | [arXiv](https://arxiv.org/abs/2508.11192) | [GitHub](https://github.com/google/howtodiv) |
| InterVLA | 2025 | 11.4 h interactions | Instruction, ego–exo mocap | [arXiv](https://arxiv.org/abs/2508.04681) | [Site](https://liangxuy.github.io/InterVLA/) |
| AEA | 2024 | 143 seq. / ~7.3 h | Everyday activities, Aria | [arXiv](https://arxiv.org/abs/2402.13349) | [Aria](https://www.projectaria.com/datasets/aea/) |
| E³ (Exploring Embodied Emotion) | 2024 | 50+ h | Emotion, multimodal ego | NeurIPS 2024 D&B | [GitHub](https://github.com/Exploring-Embodied-Emotion-official/E3) |
| EgoExoLearn | 2024 | 120 h ego+exo | Procedural, async views | [CVPR 2024](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_EgoExoLearn_A_Dataset_for_Bridging_Asynchronous_Ego-_and_Exo-centric_View_CVPR_2024_paper.html) | [GitHub](https://github.com/OpenGVLab/EgoExoLearn) |
| Ego-Exo4D | 2024 | 1,286+ h ego+exo | Skilled activity, many tasks | [arXiv](https://arxiv.org/abs/2311.18259) | [Site](https://ego-exo4d-data.org/) |
| EgoSurgery (Phase / Tool / HTS) | 2024 | Open-surgery ego video | Phase, tools, segmentation | MICCAI / arXiv (see repo) | [GitHub](https://github.com/Fujiry0/EgoSurgery) |
| EgoVid-5M | 2024 | 5M clips | Video generation, motion+text | [arXiv](https://arxiv.org/abs/2411.08380) | [Site](https://egovid.github.io/) |
| IndustReal | 2024 | ~6 h industrial | Procedure steps, errors | WACV 2024 | [Site](https://timschoonbeek.github.io/industreal.html) |
| ADT (Aria Digital Twin) | 2023 | 200 seq., 2 scenes | Egocentric 3D perception | [OpenAccess](https://openaccess.thecvf.com/content/ICCV2023/html/Pan_Aria_Digital_Twin_A_New_Benchmark_Dataset_for_Egocentric_3D_Machine_ICCV_2023_paper.html) | [Aria](https://www.projectaria.com/datasets/adt/) |
| AssemblyHands | 2023 | 3M images / hands | 3D hand pose, assembly | [CVPR 2023](https://openaccess.thecvf.com/content/CVPR2023/html/Ohkawa_AssemblyHands_Towards_Egocentric_Activity_Understanding_via_3D_Hand_Pose_Estimation_CVPR_2023_paper.html) | [Site](https://assemblyhands.github.io/) |
| ENIGMA-51 | 2023 | 22 h industrial | Fine-grained behavior | WACV 2024 / arXiv | [Site](https://fpv-iplab.github.io/ENIGMA-51/) |
| Epic-Sounding-Object | 2023 | 3.2K short clips | Audio-visual localization | CVPR 2023 | [GitHub](https://github.com/WikiChao/Ego-AV-Loc) |
| EGOFALLS | 2023 | Fall samples / AV | Fall detection | ICPR 2024 / arXiv | [Dataverse](https://www.dataverse.nl/dataset.xhtml?persistentId=doi:10.34894/HO5GE3) |
| EgoObjects | 2023 | 9.2K+ videos | Detection, instance seg | [OpenAccess](https://openaccess.thecvf.com/content/ICCV2023/html/Zhu_EgoObjects_A_Large-Scale_Egocentric_Dataset_for_Object_Detection_and_Instance_ICCV_2023_paper.html) | [GitHub](https://github.com/facebookresearch/EgoObjects) |
| EgoSchema | 2023 | 250+ h / 5K QA | Long-form video QA | NeurIPS 2023 D&B | [Site](https://egoschema.github.io/) |
| HoloAssist | 2023 | 169 h | Interactive assistants | [OpenAccess](https://openaccess.thecvf.com/content/ICCV2023/html/Wang_HoloAssist_an_Egocentric_Human_Interaction_Dataset_for_Interactive_AI_Assistants_ICCV_2023_paper.html) | [Site](https://holoassist.github.io/) |
| VidChapters-7M | 2023 | 817K videos / 7M chapters | Chaptering (not ego-only) | NeurIPS 2023 D&B | [Site](https://antoyang.github.io/vidchapters.html) |
| WEAR | 2023 | ~19 h outdoor sports | Activity + IMU | IMWUT / arXiv | [Site](https://mariusbock.github.io/wear/) |
| Assembly101 | 2022 | 513 h multiview | Assembly, procedure | [CVPR 2022](https://openaccess.thecvf.com/content/CVPR2022/html/Sener_Assembly101_A_Large-Scale_Multi-View_Video_Dataset_for_Understanding_Procedural_Activities_CVPR_2022_paper.html) | [Site](https://assembly-101.github.io/) |
| AssistQ | 2022 | 100 long videos / 529 QA | Instructional QA | ECCV 2022 | [GitHub](https://github.com/showlab/AssistQ) |
| Ego4D | 2022 | ~3,670 h | AR, VQA, forecasting, many | [arXiv](https://arxiv.org/abs/2110.07058) | [Site](https://ego4d-data.org/) |
| EgoBody | 2022 | 125 seq. / multi-view | Body pose, interaction | ECCV 2022 | [Site](https://egobody.ethz.ch/) |
| EgoClip | 2022 | 3.8M clip–text pairs | Video-language pretraining | NeurIPS 2022 (EgoVLP) | [GitHub](https://github.com/showlab/EgoVLP) |
| EgoHOS | 2022 | 11K+ images | Hand–object segmentation | ECCV 2022 | [GitHub](https://github.com/owenzlz/EgoHOS) |
| EgoPAT3D | 2022 | 1M+ frames RGB-D | 3D action target prediction | [CVPR 2022](https://openaccess.thecvf.com/content/CVPR2022/html/Li_Egocentric_Prediction_of_Action_Target_in_3D_CVPR_2022_paper.html) | [Site](https://ai4ce.github.io/EgoPAT3D/) |
| EgoProceL | 2022 | 62 videos / 16 tasks | Procedure learning | ECCV 2022 | [Site](https://sid2697.github.io/egoprocel/) |
| EgoTaskQA | 2022 | ~2K videos / 40K QA | Causal & task QA | NeurIPS 2022 D&B | [Site](https://sites.google.com/view/egotaskqa) |
| HOI4D | 2022 | 2.4M frames / 4K seq. | 4D HOI | [CVPR 2022](https://openaccess.thecvf.com/content/CVPR2022/html/Liu_HOI4D_A_4D_Egocentric_Dataset_for_Category-Level_Human-Object_Interaction_CVPR_2022_paper.html) | [Site](https://hoi4d.github.io/) |
| Multi-Ego | 2022 | ~12 h / 41 seq. | Multi-wearer, summarization | WACV 2022 | [GitHub](https://github.com/M-Elfeki/Multi-DPP) |
| N-EPIC-KITCHENS | 2022 | Event + RGB subset | Action, neuromorphic | [CVPR 2022](https://openaccess.thecvf.com/content/CVPR2022/html/Plizzari_E2GOMOTION_Motion_Augmented_Event_Stream_for_Egocentric_Action_Recognition_CVPR_2022_paper.html) | [GitHub](https://github.com/EgocentricVision/N-EPIC-Kitchens) |
| Touch and Go | 2022 | 12K+ vis–tactile frames | Vision + touch | NeurIPS 2022 D&B | [Site](https://touch-and-go.github.io/) |
| VISOR | 2022 | EPIC + masks / relations | Segmentation, HOI | NeurIPS 2022 D&B | [Site](https://epic-kitchens.github.io/VISOR) |
| Ego-Deliver | 2021 | 5,360 videos | Delivery ego analysis | ACM MM 2021 | [Site](https://egodeliver.github.io/EgoDeliver_Dataset/) |
| EPIC-KITCHENS-100 | 2021 | 100 h / 90K segments | Action recognition, many | [IJCV PDF](https://epic-kitchens.github.io/public/ek100.pdf) | [Site](https://epic-kitchens.github.io/) |
| HOMAGE | 2021 | 30 h / compositional | Home activities | [CVPR 2021](https://openaccess.thecvf.com/content/CVPR2021/html/Rai_Home_Action_Genome_Cooperative_Compositional_Action_Understanding_CVPR_2021_paper.html) | [Site](https://homeactiongenome.org/) |
| H2O | 2021 | 100K+ frames | Two-hand interaction | [ICCV 2021](https://openaccess.thecvf.com/content/ICCV2021/html/Kwon_H2O_Two_Hands_Manipulating_Objects_for_First_Person_Interaction_Recognition_ICCV_2021_paper.html) | [Site](https://h2odataset.ethz.ch/) |
| MECCANO | 2021 | ~55 h industrial | HOI, ego | WACV 2021 | [Site](https://iplab.dmi.unict.it/MECCANO/) |
| TREK-150 | 2021 | 150 EPIC seq. | Object tracking | ICCVW / IJCV | [Site](https://machinelearning.uniud.it/datasets/trek150/) |
| EgoCom | 2020 | 38.5 h conversation | Multiperson ego dialog | IEEE TPAMI 2020 | [GitHub](https://github.com/facebookresearch/EgoCom-Dataset) |
| LEMMA | 2020 | Multi-view activities | Multi-agent tasks | ECCV 2020 | [Site](https://sites.google.com/view/lemma-activity) |
| EgoVQA | 2019 | 600+ QAs | Video QA | ICCV 2019 Workshop | See workshop / authors |
| Charades-Ego | 2018 | Paired ego / exo | Alignment, actions | [arXiv](https://arxiv.org/abs/1804.09626) | See paper |
| FPHA | 2018 | 1.2K seq. hand action | Hand pose + action | [CVPR 2018](https://openaccess.thecvf.com/content_cvpr_2018/html/Garcia-Hernando_First-Person_Hand_Action_CVPR_2018_paper.html) | [Site](https://guiggh.github.io/publications/first-person-hands/) |
| EgoGesture | 2017 | 2K+ videos / 24K samples | Gesture recognition | IEEE TMM 2018 | [Site](https://nlpr.ia.ac.cn/iva/yfzhang/datasets/egogesture.html) |

## Datasets by Downstream Task

Many egocentric datasets serve multiple purposes. The per-task lists below group the **same datasets** by the downstream tasks they are most commonly used for, so you can quickly find what you need for a specific research direction. A dataset may appear under more than one category. For full detail on any entry, see [`datasets.md`](datasets.md).

### Video Generation & World-Model Pretraining

- **DreamDojo-HV** (2026) — [arXiv](https://arxiv.org/abs/2602.06949)
- **In-lab** (2026) — [arXiv](https://arxiv.org/abs/2602.06949)
- **Ego-1K** (2026) — [Hugging Face](https://huggingface.co/datasets/facebook/ego-1k)
- **Ropedia Xperience-10M** (2026) — [Hugging Face](https://huggingface.co/datasets/ropedia-ai/xperience-10m)
- **EgoEdit** (2025) — [Project](https://snap-research.github.io/EgoEdit)
- **EgoVid-5M** (2024) — [Site](https://egovid.github.io/)

### Memory, Summarization & Long-Form Understanding

- **EgoLife** (2025) — [Site](https://egolife-ai.github.io/)
- **VidChapters-7M** (2023) — [Site](https://antoyang.github.io/vidchapters.html) *(not egocentric-only)*
- **Multi-Ego** (2022) — [GitHub](https://github.com/M-Elfeki/Multi-DPP)
- **UT Ego** (2012) — [UT Austin](http://vision.cs.utexas.edu/projects/egocentric_data/UT_Egocentric_Dataset.html)

### VLMs, Instructions & QA

- **HowToDIV** (2025) — [GitHub](https://github.com/google/howtodiv)
- **InterVLA** (2025) — [Site](https://liangxuy.github.io/InterVLA/)
- **HD-EPIC** (2025) — [Site](https://hd-epic.github.io/)
- **EgoEMS** (2025) — [GitHub](https://github.com/UVA-DSA/EgoEMS)
- **EgoSchema** (2023) — [Site](https://egoschema.github.io/)
- **EgoTaskQA** (2022) — [Site](https://sites.google.com/view/egotaskqa)
- **AssistQ** (2022) — [GitHub](https://github.com/showlab/AssistQ)
- **EgoClip** (2022) — [GitHub](https://github.com/showlab/EgoVLP)
- **EgoVQA** (2019)

### Action & Activity Recognition

- **EgoScale** (2026) — [arXiv](https://arxiv.org/abs/2602.16710)
- **EgoCampus** (2025) — [GitHub](https://github.com/ComputerVisionRutgers/EgoCampus)
- **EgoExoLearn** (2024) — [GitHub](https://github.com/OpenGVLab/EgoExoLearn)
- **AEA** (2024) — [Aria](https://www.projectaria.com/datasets/aea/)
- **E³** (2024) — [GitHub](https://github.com/Exploring-Embodied-Emotion-official/E3)
- **EgoSurgery** (2024) — [GitHub](https://github.com/Fujiry0/EgoSurgery)
- **HoloAssist** (2023) — [Site](https://holoassist.github.io/)
- **WEAR** (2023) — [Site](https://mariusbock.github.io/wear/)
- **EGOFALLS** (2023) — [Dataverse](https://www.dataverse.nl/dataset.xhtml?persistentId=doi:10.34894/HO5GE3)
- **Epic-Sounding-Object** (2023) — [GitHub](https://github.com/WikiChao/Ego-AV-Loc)
- **N-EPIC-KITCHENS** (2022) — [GitHub](https://github.com/EgocentricVision/N-EPIC-Kitchens)
- **Ego4D** (2022) — [Site](https://ego4d-data.org/)
- **EPIC-KITCHENS-100** (2021) — [Site](https://epic-kitchens.github.io/)
- **Ego-Deliver** (2021) — [Site](https://egodeliver.github.io/EgoDeliver_Dataset/)
- **HOMAGE** (2021) — [Site](https://homeactiongenome.org/)
- **MECCANO** (2021) — [Site](https://iplab.dmi.unict.it/MECCANO/)
- **LEMMA** (2020) — [Site](https://sites.google.com/view/lemma-activity)
- **EgoCom** (2020) — [GitHub](https://github.com/facebookresearch/EgoCom-Dataset)
- **Charades-Ego** (2018) — [AllenAI](https://prior.allenai.org/projects/charades-ego)
- **EGTEA Gaze+** (2018) — [Georgia Tech](https://cbs.ic.gatech.edu/fpv/)
- **EgoGesture** (2017) — [Site](https://nlpr.ia.ac.cn/iva/yfzhang/datasets/egogesture.html)
- **ADL** (2012) — [UMBC](https://www.csee.umbc.edu/~hpirsiav/papers/ADLdataset/)

### Hand–Object Interaction, Dexterity & 3D

- **FEEL** (2026) — [Project](https://www.cs.umd.edu/~edessale/feel)
- **EgoDex** (2025) — [GitHub](https://github.com/apple/ml-egodex)
- **EgoPoints** (2025) — [GitHub](https://github.com/AhmadDarKhalil/EgoPoints)
- **AssemblyHands** (2023) — [Site](https://assemblyhands.github.io/)
- **EgoObjects** (2023) — [GitHub](https://github.com/facebookresearch/EgoObjects)
- **ENIGMA-51** (2023) — [Site](https://fpv-iplab.github.io/ENIGMA-51/)
- **HOI4D** (2022) — [Site](https://hoi4d.github.io/)
- **EgoHOS** (2022) — [GitHub](https://github.com/owenzlz/EgoHOS)
- **EgoBody** (2022) — [Site](https://egobody.ethz.ch/)
- **Touch and Go** (2022) — [Site](https://touch-and-go.github.io/)
- **VISOR** (2022) — [Site](https://epic-kitchens.github.io/VISOR)
- **EgoPAT3D** (2022) — [Site](https://ai4ce.github.io/EgoPAT3D/)
- **H2O** (2021) — [Site](https://h2odataset.ethz.ch/)
- **TREK-150** (2021) — [Site](https://machinelearning.uniud.it/datasets/trek150/)
- **FPHA** (2018) — [Site](https://guiggh.github.io/publications/first-person-hands/)
- **EgoDexter** (2017) — [MPI](https://handtracker.mpi-inf.mpg.de/projects/OccludedHands/EgoDexter.htm)
- **EgoHands** (2015) — [IU](http://vision.soic.indiana.edu/projects/egohands/)

### Procedural Activities & Skill Learning

- **EgoYC2 / Exo2EgoDVC** (2025) — [GitHub](https://github.com/ut-vision/Exo2EgoDVC)
- **HowToDIV** (2025) — [GitHub](https://github.com/google/howtodiv)
- **EgoExoLearn** (2024) — [GitHub](https://github.com/OpenGVLab/EgoExoLearn)
- **IndustReal** (2024) — [Site](https://timschoonbeek.github.io/industreal.html)
- **ADT (Aria Digital Twin)** (2023) — [Aria](https://www.projectaria.com/datasets/adt/)
- **Assembly101** (2022) — [Site](https://assembly-101.github.io/)
- **EgoProceL** (2022) — [Site](https://sid2697.github.io/egoprocel/)
- **EPIC-Tent** (2019) — [Data](https://data.bris.ac.uk/data/dataset/2ite3tu1u53n42hjfh3886sa86)

### Egocentric 3D Scene Understanding & Localization

- **Ego-1K** (2026) — [Hugging Face](https://huggingface.co/datasets/facebook/ego-1k)
- **ADT (Aria Digital Twin)** (2023) — [Aria](https://www.projectaria.com/datasets/adt/)
- **Ego-Exo4D** (2024) — [Site](https://ego-exo4d-data.org/)
- **EgoCart** (2018) — [Site](https://iplab.dmi.unict.it/EgocentricShoppingCartLocalization/)
- **DR(eye)VE** (2018) — [Site](http://aimagelab.ing.unimore.it/dreyeve)

## Papers & Surveys

Sorted by **year (newest first)**. Includes flagship dataset papers and selected surveys; expand freely via PR.

- [Challenges and Trends in Egocentric Vision: A Survey](https://arxiv.org/abs/2503.15275) — Li et al., 2025 (MIR / arXiv).
- [Bridging Perspectives: A Survey on Cross-view Collaborative Intelligence with Egocentric-Exocentric Vision](https://arxiv.org/abs/2506.06253) — 2025 / IJCV 2026.
- [Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives](https://arxiv.org/abs/2311.18259) — Grauman et al., CVPR 2024.
- [EgoExoLearn: A Dataset for Bridging Asynchronous Ego- and Exo-centric View of Procedural Activities in Real World](https://openaccess.thecvf.com/content/CVPR2024/html/Huang_EgoExoLearn_A_Dataset_for_Bridging_Asynchronous_Ego-_and_Exo-centric_View_CVPR_2024_paper.html) — Huang et al., CVPR 2024.
- [HD-EPIC: A Highly-Detailed Egocentric Video Dataset](https://arxiv.org/abs/2502.04144) — Perrett et al., CVPR 2025.
- [EgoSchema: A Diagnostic Benchmark for Very Long-form Video Language Understanding](https://arxiv.org/abs/2308.09126) — Mangalam et al., NeurIPS 2023 (Datasets & Benchmarks).
- [Ego4D: Around the World in 3,000 Hours of Egocentric Video](https://arxiv.org/abs/2110.07058) — Grauman et al., CVPR 2022.
- [Rescaling Egocentric Vision: Collection, Pipeline and Challenges for EPIC-KITCHENS-100](https://epic-kitchens.github.io/public/ek100.pdf) — Damen et al., IJCV 2021.
- [Charades-Ego: A Large-Scale Dataset of Paired Third and First Person Videos](https://arxiv.org/abs/1804.09626) — Sigurdsson et al., 2018.

## Benchmarks & Challenges

Structured benchmark and challenge entries (leaderboards, codalab, standardized splits) will be added here. Contributions welcome.

| Name | Year | Focus | Paper / site | Notes |
|------|------|-------|--------------|-------|
| *TBD* | — | — | — | *Placeholder — add rows via PR.* |

## Tools & Libraries

Codebases, CLIs, and libraries for working with egocentric video (e.g. Ego4D CLI, visualization) will be listed here.

| Name | Description | Link |
|------|-------------|------|
| *TBD* | *Placeholder — add rows via PR.* | — |

## Related Awesome Lists

- [Awesome-Egocentric](https://github.com/EgoAlpha/Awesome-Egocentric) — Papers and resources across egocentric tasks.
- [awesome-egocentric-vision](https://github.com/Sid2697/awesome-egocentric-vision) — Problem-centric paper and dataset links.
- [Awesome-Egocentric-and-Exocentric-Vision](https://github.com/ayiyayi/Awesome-Egocentric-and-Exocentric-Vision) — Egocentric and exocentric vision.

## Contributing

Pull requests are welcome. Please:

1. Prefer **high-quality, publicly accessible** datasets, papers, benchmarks, or tools with clear citations and official links.
2. Keep **datasets** in the main table sorted by **year (newest first)**, then name; keep **papers & surveys** sorted by **year (newest first)**.
3. Update the **Table of Contents** if you add new top-level sections.

Full guidelines: [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). See [LICENSE](LICENSE).
