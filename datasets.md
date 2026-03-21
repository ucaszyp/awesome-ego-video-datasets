# Egocentric Video Datasets — Detailed Entries

All datasets sorted **newest → oldest**. Each entry uses the same `| Field | Detail |` table for consistency.

---

### 1. Ropedia Xperience-10M (2026)

| Field | Detail |
|-------|--------|
| **Scale** | 10M experiences, ~10K h ego; 6 RGB streams, audio, stereo depth, pose/SLAM, hand + body mocap, IMU; ~2.88B RGB / 720M depth / 576M mocap frames, ~7.2B IMU samples; English captions; ~1 PB |
| **Paper** | Ropedia, 2026 (Hugging Face dataset card). [ropedia.com](https://ropedia.com/) |
| **Download** | [Hugging Face](https://huggingface.co/datasets/ropedia-ai/xperience-10m) · [Sample](https://huggingface.co/datasets/ropedia-ai/xperience-10m-sample) · [HOMIE-toolkit](https://github.com/Ropedia/HOMIE-toolkit) |

### 2. In-lab (2026)

| Field | Detail |
|-------|--------|
| **Scale** | 55 hours, 13.9K trajectories, 35 skills, 1 scene. First-person human video collected in a laboratory tabletop setting. |
| **Paper** | Gao, S. et al. "DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos." [arXiv:2602.06949](https://arxiv.org/abs/2602.06949), 2026 (Table 1) |
| **Download** | N/A |

### 3. FEEL — Force-Enhanced Egocentric Learning (2026)

| Field | Detail |
|-------|--------|
| **Scale** | ~3M force-synchronized egocentric frames from kitchen manipulation; custom piezoresistive gloves + Meta Aria video/audio; ~45% of frames with hand–object contact |
| **Paper** | Dessalene, E. et al. "FEEL: A Dataset for Physical Action Understanding." [arXiv:2603.15847](https://arxiv.org/abs/2603.15847), 2026 |
| **Download** | [Project page](https://www.cs.umd.edu/~edessale/feel) |

### 4. EgoScale (2026)

| Field | Detail |
|-------|--------|
| **Scale** | 20,854 hours of action-labeled egocentric human video — 20× larger than prior efforts for dexterous manipulation transfer |
| **Paper** | NVIDIA GEAR Lab. "EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data." [arXiv:2602.16710](https://arxiv.org/abs/2602.16710), 2026 |
| **Download** | N/A |

### 5. EgoEMS (2025 / AAAI 2026)

| Field | Detail |
|-------|--------|
| **Scale** | 20+ hours, 233 simulated EMS scenarios, 62 participants (46 EMS professionals); keysteps, diarized transcripts, action-quality metrics, bounding boxes + masks, synchronized video/audio/IMU |
| **Paper** | Weerasinghe, K. et al. [arXiv:2511.09894](https://arxiv.org/abs/2511.09894), 2025; AAAI 2026 |
| **Download** | [GitHub](https://github.com/UVA-DSA/EgoEMS) · [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/XT51K7) |

### 6. Ego-1K (2026)

| Field | Detail |
|-------|--------|
| **Scale** | 956 short clips (~1,000); 12-camera rig around a 4-sensor VR HMD — multiview egocentric video for neural 3D/4D synthesis (~491K frames / ~5.9M images) |
| **Paper** | Lee, J.Y. et al. "Ego-1K: A Large-Scale Multiview Video Dataset for Egocentric Vision." [arXiv:2603.13741](https://arxiv.org/abs/2603.13741), 2026 |
| **Download** | [Hugging Face](https://huggingface.co/datasets/facebook/ego-1k) |

### 7. DreamDojo-HV (2026)

| Field | Detail |
|-------|--------|
| **Scale** | 43,827 hours (~44K h), 1,135K trajectories, 6,015 skills, 1,135K scenes. Largest crowdsourced first-person human video dataset for world-model pretraining at time of publication. |
| **Paper** | Gao, S. et al. "DreamDojo: A Generalist Robot World Model from Large-Scale Human Videos." [arXiv:2602.06949](https://arxiv.org/abs/2602.06949), 2026 (Table 1) |
| **Download** | N/A |

### 8. InterVLA (2025)

| Field | Detail |
|-------|--------|
| **Scale** | 3.9K sequences, 11.4 hours, ~1.2M frames; egocentric human–object–human interactions with paired ego + multi-view exo RGB, spoken commands, and high-precision motion capture |
| **Paper** | Xu, L. et al. ICCV 2025. [arXiv:2508.04681](https://arxiv.org/abs/2508.04681) |
| **Download** | [Project page](https://liangxuy.github.io/InterVLA/) |

### 9. HowToDIV (2025)

| Field | Detail |
|-------|--------|
| **Scale** | 507 multi-turn expert–novice conversations, 6,636 QA pairs, ~24 hours of instructional egocentric video (cooking, mechanics, planting) |
| **Paper** | Aggarwal, L. et al. [arXiv:2508.11192](https://arxiv.org/abs/2508.11192), 2025 |
| **Download** | [GitHub](https://github.com/google/howtodiv) |

### 10. HD-EPIC (2025)

| Field | Detail |
|-------|--------|
| **Scale** | 156 videos, ~41.3 hours, ~4.46M frames, 9 participants, 69 recipes; dense multimodal labels (recipe steps, fine-grained actions, ingredients, nutrition, audio events, 3D grounding, gaze, VQA) |
| **Paper** | Perrett, T. et al. "HD-EPIC: A Highly-Detailed Egocentric Video Dataset." CVPR 2025. [arXiv:2502.04144](https://arxiv.org/abs/2502.04144) |
| **Download** | [hd-epic.github.io](https://hd-epic.github.io/) · [GitHub](https://github.com/hd-epic/hd-epic-annotations) |

### 11. EgoSurgery-HTS (2025)

| Field | Detail |
|-------|--------|
| **Scale** | Pixel-wise open-surgery annotations: 14 surgical tool classes, hand instance segmentation, hand–tool interaction masks (built atop the EgoSurgery release) |
| **Paper** | Darjana, N. et al. "EgoSurgery-HTS: A Dataset for Egocentric Hand-Tool Segmentation in Open Surgery Videos." [arXiv:2503.18755](https://arxiv.org/abs/2503.18755), 2025 |
| **Download** | [GitHub](https://github.com/Fujiry0/EgoSurgery) |

### 12. EgoPoints (2025)

| Field | Detail |
|-------|--------|
| **Scale** | 4.7K human point tracks in real egocentric video (out-of-view + re-ID); ~11K semi-real synthetic training sequences (K-EPIC pipeline: Kubric + EPIC Fields) |
| **Paper** | Darkhalil, A. et al. "EgoPoints: Advancing Point Tracking for Egocentric Videos." WACV 2025. [arXiv:2412.04592](https://arxiv.org/abs/2412.04592) |
| **Download** | [GitHub](https://github.com/AhmadDarKhalil/EgoPoints) |

### 13. EgoLife (2025)

| Field | Detail |
|-------|--------|
| **Scale** | ~300 hours (~266 h retained) of egocentric multimodal daily-life recording, 6 participants, 7 days in EgoHouse, Meta Aria + 15 third-person cameras + 2 mmWave devices |
| **Paper** | Yang, J. et al. "EgoLife: Towards Egocentric Life Assistant." CVPR 2025. [arXiv](https://arxiv.org/abs/2503.01773) |
| **Download** | [egolife-ai.github.io](https://egolife-ai.github.io/) · [Hugging Face](https://huggingface.co/datasets/lmms-lab/EgoLife) · [GitHub](https://github.com/EvolvingLMMs-Lab/EgoLife) |

### 14. EgoEdit / EgoEditData (2025)

| Field | Detail |
|-------|--------|
| **Scale** | 100K curated egocentric video editing pairs (object swap/removal, heavy occlusion & hand interaction, large ego motion) |
| **Paper** | Snap Research. "EgoEdit: Dataset, Real-Time Streaming Model, and Benchmark for Egocentric Video Editing." [arXiv:2512.06065](https://arxiv.org/abs/2512.06065), 2025 |
| **Download** | [Project page](https://snap-research.github.io/EgoEdit) |

### 15. EgoDex (2025)

| Field | Detail |
|-------|--------|
| **Scale** | 829 hours, 30K trajectories, 194 tasks, 5 scenes. Recorded with Apple Vision Pro (ARKit, 30 Hz, 1080p + 3D hand/body pose). |
| **Paper** | Hoque, R. et al. [arXiv:2505.11709](https://arxiv.org/abs/2505.11709), 2025 |
| **Download** | [GitHub](https://github.com/apple/ml-egodex) |

### 16. EgoCampus (2025)

| Field | Detail |
|-------|--------|
| **Scale** | 25 outdoor campus paths (~6 km); 80+ pedestrians, ~32 h multimodal data / ~3.5M frames; Project Aria egocentric RGB + eye tracking + IMU/GPS |
| **Paper** | John, R. et al. "EgoCampus: Egocentric Pedestrian Eye Gaze Model and Dataset." [arXiv:2512.07668](https://arxiv.org/abs/2512.07668), 2025 |
| **Download** | [GitHub](https://github.com/ComputerVisionRutgers/EgoCampus) |

### 17. IndustReal (2024)

| Field | Detail |
|-------|--------|
| **Scale** | 84 videos, ~6 hours, 27 participants, egocentric video + hand joint detection + gaze tracking, 3 annotation types (action recognition, assembly state, procedure step) |
| **Paper** | Schoonbeek, T. et al. "IndustReal: A Dataset for Procedure Step Recognition Handling Execution Errors in Egocentric Videos in an Industrial-Like Setting." WACV 2024 |
| **Download** | [Project page](https://timschoonbeek.github.io/industreal.html) · [4TU](https://data.4tu.nl/datasets/b008dd74-020d-4ea4-a8ba-7bb60769d224) |

### 18. E³ — Exploring Embodied Emotion (2024)

| Field | Detail |
|-------|--------|
| **Scale** | 50+ hours of first-person video, 8 emotion categories, 4 benchmark tasks (recognition, classification, localization, reasoning), 80K+ annotations; multimodal (visual + audio + text) |
| **Paper** | Wang, L. et al. NeurIPS 2024 Datasets & Benchmarks |
| **Download** | [GitHub](https://github.com/Exploring-Embodied-Emotion-official/E3) |

### 19. EgoVid-5M (2024)

| Field | Detail |
|-------|--------|
| **Scale** | 5M egocentric video clips at 1080p, enriched with fine-grained kinematic control and high-level textual action descriptions |
| **Paper** | Wang, X. et al. "EgoVid-5M: A Large-Scale Video-Action Dataset for Egocentric Video Generation." [arXiv:2411.08380](https://arxiv.org/abs/2411.08380), 2024; NeurIPS 2025 |
| **Download** | [egovid.github.io](https://egovid.github.io/) · [GitHub](https://github.com/JeffWang987/EgoVid) |

### 20. EgoSurgery-Tool (2024)

| Field | Detail |
|-------|--------|
| **Scale** | 49K+ surgical-tool boxes (15 tool classes), 46K+ hand boxes, dense detection annotations in open-surgery egocentric video |
| **Paper** | Fujii, R. et al. "EgoSurgery-Tool: A Dataset of Surgical Tool and Hand Detection from Egocentric Open Surgery Videos." [arXiv:2406.03095](https://arxiv.org/abs/2406.03095), 2024 |
| **Download** | [GitHub](https://github.com/Fujiry0/EgoSurgery) |

### 21. EgoSurgery-Phase (2024)

| Field | Detail |
|-------|--------|
| **Scale** | ~15 hours of real open-surgery egocentric video, 21 videos / 10 procedure types, 9 surgical phases, 8 surgeons; includes surgeon eye-gaze |
| **Paper** | Fujii, R. et al. "EgoSurgery-Phase: A Dataset of Surgical Phase Recognition from Egocentric Open Surgery Videos." MICCAI 2024. [arXiv:2405.19644](https://arxiv.org/abs/2405.19644) |
| **Download** | [GitHub](https://github.com/Fujiry0/EgoSurgery) |

### 22. EgoExoLearn (2024)

| Field | Detail |
|-------|--------|
| **Scale** | 120 hours total (96.5 h / 432 ego + 23.5 h / 315 exo videos), multimodal annotations (temporal language, gaze) |
| **Paper** | Huang, Y. et al. "EgoExoLearn: A Dataset for Bridging Asynchronous Ego- and Exo-centric View of Procedural Activities in Real World." CVPR 2024 |
| **Download** | [GitHub](https://github.com/OpenGVLab/EgoExoLearn) · [Hugging Face](https://huggingface.co/datasets/hyf015/EgoExoLearn) |

### 23. AEA — Aria Everyday Activities (2024)

| Field | Detail |
|-------|--------|
| **Scale** | 143 daily activity sequences, 5 indoor locations, 1M+ frames, 7.3 hours; multimodal (RGB, mono cameras, IMU), 3D trajectories, scene point clouds, 3D eye gaze, speech transcription |
| **Paper** | Lv, Z. et al. "Aria Everyday Activities Dataset." [arXiv:2402.13349](https://arxiv.org/abs/2402.13349), 2024 |
| **Download** | [Project Aria](https://www.projectaria.com/datasets/aea/) · [Hugging Face](https://huggingface.co/datasets/projectaria/aria-everyday-activities) |

### 24. WEAR (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 22 participants, 18 outdoor workout activities, ~19 hours, 11 locations; egocentric video (GoPro 1080p@60fps) + 4 smartwatch IMUs (50 Hz) |
| **Paper** | Bock, M. et al. "WEAR: An Outdoor Sports Dataset for Wearable and Egocentric Activity Recognition." ACM IMWUT 2024 (arXiv 2023) |
| **Download** | [Project page](https://mariusbock.github.io/wear/). CC BY-NC-SA 4.0 |

### 25. VidChapters-7M (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 817K user-chaptered videos, 7M chapters; includes ASR transcripts (Whisper) and CLIP features. **Note:** general video, not exclusively egocentric. |
| **Paper** | Yang, A. et al. "VidChapters-7M: Video Chapters at Scale." NeurIPS 2023 D&B |
| **Download** | [Project page](https://antoyang.github.io/vidchapters.html) · [GitHub](https://github.com/antoyang/VidChapters) |

### 26. VOST (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 713 videos, 155 object categories, objects undergoing complex transformations (breaking, deforming, mixing, etc.) |
| **Paper** | Tokmakov, P. et al. "Breaking the 'Object' in Video Object Segmentation." CVPR 2023 |
| **Download** | [vostdataset.org](https://www.vostdataset.org/) · [GitHub](https://github.com/yka-dl/VOST) |

### 27. PVSG (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 400 videos (289 third-person + 111 egocentric), ~150K annotated frames, 126 object classes, 57 relation classes. Videos from Ego4D, EPIC-Kitchens, VidOR. |
| **Paper** | Yang, J. et al. "Panoptic Video Scene Graph Generation." CVPR 2023 |
| **Download** | [Project page](https://jingkang50.github.io/PVSG/) · [GitHub](https://github.com/LilyDaytoy/OpenPVSG) |

### 28. POV-Surgery (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 53 sequences, 88,329 frames, synthetic egocentric surgical data, 3 surgical tools, RGB-D with 3D/2D hand-object pose + segmentation + activity labels |
| **Paper** | Wang, R. et al. "POV-Surgery: A Dataset for Egocentric Hand and Tool Pose Estimation During Surgical Activities." MICCAI 2023 (Oral) |
| **Download** | [Project page](https://batfacewayne.github.io/POV_Surgery_io/) · [GitHub](https://github.com/BatFaceWayne/POV_Surgery) |

### 29. HoloAssist (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 169 hours, 222 participants / 350 instructor-performer pairs, 20 manipulation tasks, 7 synchronized streams (RGB, depth, eye gaze, hand pose, head pose, IMU, audio) |
| **Paper** | Wang, X. et al. "HoloAssist: an Egocentric Human Interaction Dataset for Interactive AI Assistants in the Real World." ICCV 2023 |
| **Download** | [holoassist.github.io](https://holoassist.github.io/) · [GitHub](https://github.com/Ember-HoloAssist/holoassist-release) |

### 30. Epic-Sounding-Object (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 3,172 video clips (avg <3 s) for egocentric audio-visual sounding-object localization, derived from EPIC-KITCHENS |
| **Paper** | Huang, C. et al. "Egocentric Audio-Visual Object Localization." CVPR 2023 |
| **Download** | [GitHub](https://github.com/WikiChao/Ego-AV-Loc) |

### 31. EgoYC2 (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 226 egocentric cooking videos from 44 users, ~43 hours, recorded in real home kitchens |
| **Paper** | Ohkawa, T. et al. "Exo2EgoDVC: Dense Video Captioning of Egocentric Procedural Activities Using Web Instructional Videos." WACV 2025. [arXiv:2311.16444](https://arxiv.org/abs/2311.16444) |
| **Download** | [GitHub](https://github.com/ut-vision/Exo2EgoDVC) |

### 32. EgoSchema (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 5,031 human-curated multiple-choice QA pairs, 250+ hours of egocentric video (from Ego4D), each question based on a 3-min clip, 5 answer options |
| **Paper** | Mangalam, K. et al. "EgoSchema: A Diagnostic Benchmark for Very Long-form Video Language Understanding." NeurIPS 2023 D&B. [arXiv:2308.09126](https://arxiv.org/abs/2308.09126) |
| **Download** | [egoschema.github.io](https://egoschema.github.io/) · [GitHub](https://github.com/egoschema/EgoSchema) |

### 33. EgoObjects (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 9,200+ egocentric videos, 654K+ frames, 14,145 main objects from 368 categories, bounding box + instance segmentation, captured with Aria glasses |
| **Paper** | Zhu, C. et al. "EgoObjects: A Large-Scale Egocentric Dataset for Object Detection and Instance Segmentation." ICCV 2023 |
| **Download** | [GitHub](https://github.com/facebookresearch/EgoObjects) · [Project Aria](https://www.projectaria.com/datasets/) |

### 34. Ego-Exo4D (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 5,035 takes from 740 wearers, 13 cities, 1,286+ hours ego+exo video, 123 scene contexts, 43 tasks across 8 domains; multimodal (audio, gaze, 3D point clouds, IMU) |
| **Paper** | Grauman, K. et al. "Ego-Exo4D: Understanding Skilled Human Activity from First- and Third-Person Perspectives." CVPR 2024. [arXiv:2311.18259](https://arxiv.org/abs/2311.18259) |
| **Download** | [ego-exo4d-data.org](https://ego-exo4d-data.org/) (license required) |

### 35. ENIGMA-51 (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 51 video sequences, 22 hours, 19 subjects, 45,505 RGB frames (2272×1278, 30 fps), 275K+ object boxes, 56K+ hand annotations, 3D environment models |
| **Paper** | Ragusa, F. et al. "ENIGMA-51: Towards a Fine-Grained Understanding of Human Behavior in Industrial Scenarios." WACV 2024 |
| **Download** | [Project page](https://fpv-iplab.github.io/ENIGMA-51/) · [GitHub](https://github.com/fpv-iplab/ENIGMA-51) |

### 36. EGOFALLS (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 10,948 video samples, 14 subjects, visual-audio multimodal, up to 1080p@30 fps, ~200 GB |
| **Paper** | Wang, X. "EGOFALLS: A Visual-Audio Dataset and Benchmark for Fall Detection Using Egocentric Cameras." ICPR 2024 |
| **Download** | [DataverseNL](https://www.dataverse.nl/dataset.xhtml?persistentId=doi:10.34894/HO5GE3) |

### 37. AssemblyHands (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 3.0M annotated images (490K egocentric), largest egocentric 3D hand pose benchmark, derived from Assembly101, avg keypoint error 4.20 mm |
| **Paper** | Ohkawa, T. et al. "AssemblyHands: Towards Egocentric Activity Understanding via 3D Hand Pose Estimation." CVPR 2023 |
| **Download** | [assemblyhands.github.io](https://assemblyhands.github.io/) · [Toolkit](https://github.com/facebookresearch/assemblyhands-toolkit). CC BY-NC 4.0 |

### 38. ADT — Aria Digital Twin (2023)

| Field | Detail |
|-------|--------|
| **Scale** | 200 sequences, 2 real indoor scenes, 398 object instances, multi-sensor (2 mono + 1 RGB + 2 IMU), ground-truth 6DoF poses, 3D eye gaze, depth maps, segmentations |
| **Paper** | Pan, X. et al. "Aria Digital Twin: A New Benchmark Dataset for Egocentric 3D Machine Perception." ICCV 2023 |
| **Download** | [Project Aria ADT](https://www.projectaria.com/datasets/adt/) · [Hugging Face](https://huggingface.co/datasets/projectaria/aria-digital-twin) |

### 39. VISOR (2022)

| Field | Detail |
|-------|--------|
| **Scale** | 271K manual masks, 9.9M dense masks, 257 object types, 67K hand-object relations. Built on EPIC-KITCHENS. |
| **Paper** | Darkhalil, A. et al. "EPIC-KITCHENS VISOR Benchmark: VIdeo Segmentations and Object Relations." NeurIPS 2022 D&B |
| **Download** | [EPIC VISOR](https://epic-kitchens.github.io/VISOR) · [GitHub](https://github.com/epic-kitchens/VISOR) |

### 40. Touch and Go (2022)

| Field | Detail |
|-------|--------|
| **Scale** | 12K+ paired visual-tactile frames, egocentric video paired with GelSight tactile sensor, diverse indoor/outdoor surfaces |
| **Paper** | Yang, F. et al. "Touch and Go: Learning from Human-Collected Vision and Touch." NeurIPS 2022 D&B |
| **Download** | [touch-and-go.github.io](https://touch-and-go.github.io/) · [GitHub](https://github.com/fredfyyang/Touch-and-Go) |

### 41. N-EPIC-KITCHENS (2022)

| Field | Detail |
|-------|--------|
| **Scale** | Neuromorphic (event camera) version of EPIC-KITCHENS. Three largest kitchens of EPIC-KITCHENS-55 enhanced with synthetic event streams. Synchronized event + RGB modalities. |
| **Paper** | Plizzari, C. et al. "E2(GO)MOTION: Motion Augmented Event Stream for Egocentric Action Recognition." CVPR 2022 |
| **Download** | [GitHub](https://github.com/EgocentricVision/N-EPIC-Kitchens) |

### 42. Multi-Ego (2022)

| Field | Detail |
|-------|--------|
| **Scale** | 41 sequences (3–7 min each), 12 hours total, 3 simultaneous camera wearers per sequence, indoor + outdoor |
| **Paper** | Elfeki, M. et al. "Multi-Stream Dynamic Video Summarization." WACV 2022 |
| **Download** | [GitHub](https://github.com/M-Elfeki/Multi-DPP) |

### 43. HOI4D (2022)

| Field | Detail |
|-------|--------|
| **Scale** | 2.4M RGB-D egocentric frames, 4,000 sequences, 9 participants, 800 object instances, 16 categories, rich 3D annotations (object poses, hand poses, interaction region, motion segmentation) |
| **Paper** | Liu, Y. et al. "HOI4D: A 4D Egocentric Dataset for Category-Level Human-Object Interaction." CVPR 2022 |
| **Download** | [hoi4d.github.io](https://hoi4d.github.io/) |

### 44. EgoTaskQA (2022)

| Field | Detail |
|-------|--------|
| **Scale** | 40K balanced QA pairs (from 368K), ~2,000 videos, 4 question types (descriptive, predictive, explanatory, counterfactual) |
| **Paper** | Jia, B. et al. "EgoTaskQA: Understanding Human Tasks in Egocentric Videos." NeurIPS 2022 D&B |
| **Download** | [Project page](https://sites.google.com/view/egotaskqa) · [GitHub](https://github.com/Buzz-Beater/EgoTaskQA) |

### 45. EgoProceL (2022)

| Field | Detail |
|-------|--------|
| **Scale** | 62 egocentric videos of 16 diverse tasks, key-step annotations for procedural learning |
| **Paper** | Bansal, S. et al. "My View is the Best View: Procedure Learning from Egocentric Videos." ECCV 2022 |
| **Download** | [Project page](https://sid2697.github.io/egoprocel/) · [GitHub](https://github.com/Sid2697/EgoProceL-egocentric-procedure-learning) |

### 46. EgoPAT3D (2022)

| Field | Detail |
|-------|--------|
| **Scale** | 1M+ frames of RGB-D and IMU, 15 indoor scenes, 3D action target prediction annotations, scene point clouds, hand pose results |
| **Paper** | Li, Y. et al. "Egocentric Prediction of Action Target in 3D." CVPR 2022 |
| **Download** | [Project page](https://ai4ce.github.io/EgoPAT3D/) · [GitHub](https://github.com/ai4ce/EgoPAT3D) |

### 47. EgoHOS (2022)

| Field | Detail |
|-------|--------|
| **Scale** | 11,243 egocentric images with pixel-level hand-object segmentation, contact boundary annotations, 1st/2nd order object labels |
| **Paper** | Zhang, L. et al. "Fine-Grained Egocentric Hand-Object Segmentation: Dataset, Model, and Applications." ECCV 2022 |
| **Download** | [GitHub](https://github.com/owenzlz/EgoHOS) |

### 48. EgoClip (2022)

| Field | Detail |
|-------|--------|
| **Scale** | 3.8M clip-text pairs curated from Ego4D, paired with temporal narration text |
| **Paper** | Lin, K.Q. et al. "Egocentric Video-Language Pretraining" (EgoVLP). NeurIPS 2022 |
| **Download** | [GitHub](https://github.com/showlab/EgoVLP) (requires Ego4D video access) |

### 49. EgoBody (2022)

| Field | Detail |
|-------|--------|
| **Scale** | 125 sequences, 36 subjects, 15 indoor 3D environments, 219K synchronized multi-view RGBD frames, 199K egocentric RGB frames (HoloLens 2), SMPL-X body annotations |
| **Paper** | Zhang, S. et al. "EgoBody: Human Body Shape and Motion of Interacting People from Head-Mounted Devices." ECCV 2022 |
| **Download** | [egobody.ethz.ch](https://egobody.ethz.ch/) (license required) |

### 50. AssistQ (2022)

| Field | Detail |
|-------|--------|
| **Scale** | 529 QA samples, 100 long egocentric videos (avg ~5 min), 31 scenes, multi-step instructional QA for device assistance |
| **Paper** | Wong, M. et al. "AssistQ: Affordance-Centric Question-Driven Task Completion for Egocentric Assistant." ECCV 2022 |
| **Download** | [GitHub](https://github.com/showlab/AssistQ) |

### 51. Assembly101 (2022)

| Field | Detail |
|-------|--------|
| **Scale** | 4,321 videos, 513 hours, 53 participants, 1,380 fine-grained / 202 coarse action classes, 100K+ coarse & 1M+ fine annotations, 18M 3D hand poses, 12 synchronized views (8 fixed + 4 ego) |
| **Paper** | Sener, F. et al. "Assembly101: A Large-Scale Multi-View Video Dataset for Understanding Procedural Activities." CVPR 2022 |
| **Download** | [assembly-101.github.io](https://assembly-101.github.io/) |

### 52. TREK-150 (2021)

| Field | Detail |
|-------|--------|
| **Scale** | 150 densely annotated video sequences from EPIC-KITCHENS, single-target object tracking with bounding boxes, hand-object interaction annotations |
| **Paper** | Dunnhofer, M. et al. "Is First Person Vision Challenging for Object Tracking?" ICCVW 2021; extended in IJCV 2023 |
| **Download** | [TREK-150](https://machinelearning.uniud.it/datasets/trek150/) · [Toolkit](https://github.com/matteo-dunnhofer/TREK-150-toolkit) |

### 53. MECCANO (2021)

| Field | Detail |
|-------|--------|
| **Scale** | 20 videos, 20 participants, ~55 hours, ~11.5M frames, RGB + Depth + Gaze, 8,857 action segments, 64K+ object boxes, 12 verb / 20 object / 61 action classes |
| **Paper** | Ragusa, F. et al. "The MECCANO Dataset: Understanding Human-Object Interactions from Egocentric Videos in an Industrial-like Domain." WACV 2021 |
| **Download** | [MECCANO](https://iplab.dmi.unict.it/MECCANO/) · [GitHub](https://github.com/fpv-iplab/MECCANO) |

### 54. HOMAGE (2021)

| Field | Detail |
|-------|--------|
| **Scale** | 30 hours, 1,752 synchronized sequences, 27 participants, 12 sensor types, 75 activities, 453 atomic action classes, 86 object categories, 497K+ bounding boxes |
| **Paper** | Rai, N. et al. "Home Action Genome: Cooperative Compositional Action Understanding." CVPR 2021 |
| **Download** | [homeactiongenome.org](https://homeactiongenome.org/) · [GitHub](https://github.com/nishantrai18/homage) |

### 55. H2O (2021)

| Field | Detail |
|-------|--------|
| **Scale** | 100K+ frames, 45 hand action categories, 26 object types, 4 subjects, synchronized multi-view RGB-D, 3D hand + 6D object pose annotations |
| **Paper** | Kwon, T. et al. "H2O: Two Hands Manipulating Objects for First Person Interaction Recognition." ICCV 2021 |
| **Download** | [h2odataset.ethz.ch](https://h2odataset.ethz.ch/) · [GitHub](https://github.com/taeinkwon/h2odataset) |

### 56. Ego4D (2021)

| Field | Detail |
|-------|--------|
| **Scale** | 3,670 hours, 931 wearers, 74 locations across 9 countries; multimodal (audio, 3D meshes, eye gaze, stereo, multi-camera). 20× larger than any prior egocentric dataset at release. |
| **Paper** | Grauman, K. et al. "Ego4D: Around the World in 3,000 Hours of Egocentric Video." CVPR 2022. [arXiv:2110.07058](https://arxiv.org/abs/2110.07058) |
| **Download** | [ego4d-data.org](https://ego4d-data.org/) (license required). CLI: [GitHub](https://github.com/facebookresearch/Ego4d) |

### 57. Ego-Deliver (2021)

| Field | Detail |
|-------|--------|
| **Scale** | 5,360 videos, 139K+ multi-track annotations, 45 attributes, recorded by takeaway delivery riders |
| **Paper** | Qiu, H. et al. "Ego-Deliver: A Large-Scale Dataset For Egocentric Video Analysis." ACM MM 2021 |
| **Download** | [Project page](https://egodeliver.github.io/EgoDeliver_Dataset/) |

### 58. EPIC-KITCHENS-100 (2021)

| Field | Detail |
|-------|--------|
| **Scale** | 100 hours, 20M frames, 90K action segments, 700 videos, 45 kitchens, 97 verb / 300 noun classes |
| **Paper** | Damen, D. et al. "Rescaling Egocentric Vision: Collection, Pipeline and Challenges for EPIC-KITCHENS-100." IJCV 2021 |
| **Download** | [epic-kitchens.github.io](https://epic-kitchens.github.io/) · [Annotations](https://github.com/epic-kitchens/epic-kitchens-100-annotations) |

### 59. You2Me (2020)

| Field | Detail |
|-------|--------|
| **Scale** | 14 sequences, 6 participants, 4 interaction domains, 1920×1080@30 fps, chest-mounted GoPro |
| **Paper** | Ng, E. et al. "You2Me: Inferring Body Pose in Egocentric Video via First and Second Person Interactions." CVPR 2020 |
| **Download** | [GitHub](https://github.com/facebookresearch/you2me) (archived) |

### 60. LEMMA (2020)

| Field | Detail |
|-------|--------|
| **Scale** | 7 houses, 14 kitchens/living rooms, 8 participants, 641 action classes, 11,781 action segments, ~4.6M frames, multi-view (first + third person) |
| **Paper** | Jia, B. et al. "LEMMA: A Multi-view Dataset for LEarning Multi-agent Multi-task Activities." ECCV 2020 |
| **Download** | [Project page](https://sites.google.com/view/lemma-activity) · [GitHub](https://github.com/Buzz-Beater/LEMMA) |

### 61. EgoCom (2020)

| Field | Detail |
|-------|--------|
| **Scale** | 38.5 hours, 39 conversations (175 files), 34 speakers, 240K time-stamped word-level transcriptions |
| **Paper** | Northcutt, C.G. et al. "EgoCom: A Multi-Person Multi-Modal Egocentric Communications Dataset." IEEE TPAMI 2020 |
| **Download** | [GitHub](https://github.com/facebookresearch/EgoCom-Dataset) |

### 62. EGO-CH (2020)

| Field | Detail |
|-------|--------|
| **Scale** | 27+ hours, 70 visits/subjects, 26 environments across 2 cultural sites in Sicily, 200+ Points of Interest |
| **Paper** | Ragusa, F. et al. "EGO-CH: Dataset and Fundamental Tasks for Visitors Behavioral Understanding using Egocentric Vision." Pattern Recognition Letters 2020 |
| **Download** | N/A |

### 63. EgoVQA (2019)

| Field | Detail |
|-------|--------|
| **Scale** | 600+ QA pairs, 600+ video clips (20–100 s), ~5,000 frames, 16 egocentric videos from 8 scenarios |
| **Paper** | Fan, C. "EgoVQA — An Egocentric Video Question Answering Benchmark Dataset." ICCV 2019 Workshop (EPIC) |
| **Download** | N/A |

### 64. EPIC-Tent (2019)

| Field | Detail |
|-------|--------|
| **Scale** | 29 participants, 7+ hours, 2 synchronized head-mounted cameras (GoPro + SMI eye tracker), tent assembly task |
| **Paper** | Jang, Y. et al. "EPIC-Tent: An Egocentric Video Dataset for Camping Tent Assembly." ICCV 2019 Workshop |
| **Download** | [Data](https://data.bris.ac.uk/data/dataset/2ite3tu1u53n42hjfh3886sa86) · [Annotations](https://github.com/youngkyoonjang/EPIC_Tent2019) |

### 65. IU ShareView (2018)

| Field | Detail |
|-------|--------|
| **Scale** | 9 sets of paired first-person videos (5–10 min), 3–4 participants per set, 6 indoor environments, 1,277 frames with pixel-level person segmentation |
| **Paper** | Xu, M. et al. "Joint Person Segmentation and Identification in Synchronized First- and Third-person Videos." ECCV 2018 |
| **Download** | [Project page](http://vision.soic.indiana.edu/firstthird-eccv2018/) |

### 66. FPHA (2018)

| Field | Detail |
|-------|--------|
| **Scale** | 1,175 sequences, 100K+ frames, 6 subjects, 45 hand action categories, 26 objects, 21 hand joints via magnetic mocap, RGB-D |
| **Paper** | Garcia-Hernando, G. et al. "First-Person Hand Action Benchmark with RGB-D Videos and 3D Hand Pose Annotations." CVPR 2018 |
| **Download** | [Project page](https://guiggh.github.io/publications/first-person-hands/) · [GitHub](https://github.com/guiggh/hand_pose_action) |

### 67. EgoCart (2018)

| Field | Detail |
|-------|--------|
| **Scale** | 19,531 RGB images with depth maps and camera poses, 9 videos in a retail store (782 m²) |
| **Paper** | Spera, E. et al. "Egocentric Shopping Cart Localization." ICPR 2018; extended IEEE TCSVT 2019 |
| **Download** | [Project page](https://iplab.dmi.unict.it/EgocentricShoppingCartLocalization/) |

### 68. EGTEA Gaze+ (2018)

| Field | Detail |
|-------|--------|
| **Scale** | 28 hours of cooking, 86 sessions / 32 subjects, 10,325 action instances, 106 action classes, 15,176 hand masks, gaze at 30 Hz |
| **Paper** | Li, Y. et al. "In the Eye of Beholder: Joint Learning of Gaze and Actions in First Person Video." ECCV 2018 |
| **Download** | [Project page](https://cbs.ic.gatech.edu/fpv/) |

### 69. DoMSEV (2018)

| Field | Detail |
|-------|--------|
| **Scale** | 80 hours, 48 sequences, multimodal (RGB-D, IMU, GPS), 640×480 to 1920×1080 at 30–60 fps |
| **Paper** | Silva, M. et al. "A Weighted Sparse Sampling and Smoothing Frame Transition Approach for Semantic Fast-Forward First-Person Videos." CVPR 2018 |
| **Download** | [UFMG](https://www.verlab.dcc.ufmg.br/semantic-hyperlapse/cvpr2018-dataset/). CC BY-NC 4.0 |

### 70. DR(eye)VE (2018)

| Field | Detail |
|-------|--------|
| **Scale** | 555K frames (~6 h driving), 74 sequences, 8 drivers, dual views (ego eye-tracking 720p/30 fps + roof 1080p/25 fps), GPS/accelerometer/gyroscope |
| **Paper** | Palazzi, A. et al. "Predicting the Driver's Focus of Attention: the DR(eye)VE Project." IEEE TPAMI 2018 |
| **Download** | [Project page](http://aimagelab.ing.unimore.it/dreyeve) · [GitHub](https://github.com/ndrplz/dreyeve) |

### 71. Charades-Ego (2018)

| Field | Detail |
|-------|--------|
| **Scale** | 7,860 paired first-person and third-person videos, 68,536 activity instances, 157 action classes, 68.8 hours total |
| **Paper** | Sigurdsson, G.A. et al. "Charades-Ego: A Large-Scale Dataset of Paired Third and First Person Videos." [arXiv:1804.09626](https://arxiv.org/abs/1804.09626), 2018 |
| **Download** | [AllenAI](https://prior.allenai.org/projects/charades-ego) (480p 11 GB, original 47 GB, RGB frames 53 GB) |

### 72. THU-READ (2017)

| Field | Detail |
|-------|--------|
| **Scale** | 1,920 clips (8 subjects × 40 actions × 3 reps × 2 modalities), RGB-D from helmet-mounted sensor |
| **Paper** | Tang, Y. et al. "Action Recognition in RGB-D Egocentric Videos." ICIP 2017 |
| **Download** | [THU-READ](https://ivg.au.tsinghua.edu.cn/dataset/THU_READ.php) |

### 73. Stanford ECM (2017)

| Field | Detail |
|-------|--------|
| **Scale** | 31 hours, augmented with heart rate and accelerometer, 23–24 daily activity categories |
| **Paper** | Nakamura, K. et al. "Jointly Learning Energy Expenditures and Activities Using Egocentric Multimodal Signals." CVPR 2017 |
| **Download** | N/A |

### 74. OST (2017)

| Field | Detail |
|-------|--------|
| **Scale** | 57 sequences, 55 subjects, ~15 min/video, egocentric object search tasks, eye-tracking ground truth |
| **Paper** | Zhang, M. et al. "Deep Future Gaze: Gaze Anticipation on Egocentric Videos Using Adversarial Networks." CVPR 2017 |
| **Download** | [GitHub](https://github.com/Mengmi/deepfuturegaze_gan) |

### 75. EgoGesture (2017)

| Field | Detail |
|-------|--------|
| **Scale** | 2,081 RGB-D videos, 24,161 gesture samples, 2,953,224 frames, 50 subjects, 83 gesture classes, 6 scenes |
| **Paper** | Zhang, Y. et al. "EgoGesture: A New Dataset and Benchmark for Egocentric Hand Gesture Recognition." IEEE TMM 2018 (ICCV 2017 Workshop) |
| **Download** | [Dataset page](https://nlpr.ia.ac.cn/iva/yfzhang/datasets/egogesture.html) (application required) |

### 76. EgoDexter (2017)

| Field | Detail |
|-------|--------|
| **Scale** | 4 sequences, 3,190 frames, 1,485 frames with manual fingertip annotations, 4 actors, RGB-D |
| **Paper** | Mueller, F. et al. "Real-time Hand Tracking under Occlusion from an Egocentric RGB-D Sensor." ICCV 2017 |
| **Download** | [MPI](https://handtracker.mpi-inf.mpg.de/projects/OccludedHands/EgoDexter.htm) (1.99 GB ZIP) |

### 77. PEV — UTokyo Paired Ego-Video (2016)

| Field | Detail |
|-------|--------|
| **Scale** | 1,226 pairs of first-person clips, synchronous dyadic conversations, 8 interaction categories, 6 subjects |
| **Paper** | Yonetani, R. et al. "Recognizing Micro-Actions and Reactions from Paired Egocentric Videos." CVPR 2016 |
| **Download** | N/A |

### 78. FPPA (2015)

| Field | Detail |
|-------|--------|
| **Scale** | 5 subjects, 5 daily actions, egocentric video with hand and gaze cues |
| **Paper** | Li, Y. et al. "Delving into Egocentric Actions." CVPR 2015 |
| **Download** | N/A |

### 79. EgoHands (2015)

| Field | Detail |
|-------|--------|
| **Scale** | 4,800 labeled frames, 15,053 hand instances with bounding boxes, 48 Google Glass videos, 4 participants |
| **Paper** | Bambach, S. et al. "Lending A Hand: Detecting Hands and Recognizing Activities in Complex Egocentric Interactions." ICCV 2015 |
| **Download** | [Project page](http://vision.soic.indiana.edu/projects/egohands/) |

### 80. HUJI-EgoSeg (2014)

| Field | Detail |
|-------|--------|
| **Scale** | 29 long egocentric videos (~1–5 h each), pixel-level temporal segmentation annotations |
| **Paper** | Poleg, Y. et al. "Temporal Segmentation of Egocentric Videos." CVPR 2014 |
| **Download** | [HUJI](http://www.cs.huji.ac.il/~yedMDpid/egoseg/) |

### 81. BEOID (2014)

| Field | Detail |
|-------|--------|
| **Scale** | 58 videos, 6 environments, 34 object interaction classes, ~30 fps |
| **Paper** | Damen, D. et al. "You-Do, I-Learn: Discovering Task Relevant Objects and their Modes of Interaction from Multi-User Egocentric Video." BMVC 2014 |
| **Download** | [Bristol](https://data.bris.ac.uk/data/dataset/3wats8ruq1sp52hq3bo8dkzul3) |

### 82. JPL-Interaction (2013)

| Field | Detail |
|-------|--------|
| **Scale** | 84 videos, 7 activity types (4 positive, 1 neutral, 2 negative interactions), 320×240@30 fps |
| **Paper** | Ryoo, M.S. & Matthies, L. "First-Person Activity Recognition: What Are They Doing to Me?" CVPR 2013 |
| **Download** | [Project page](http://michaelryoo.com/jpl-interaction.html) |

### 83. EDSH (2013)

| Field | Detail |
|-------|--------|
| **Scale** | 2 videos (~5 min each), pixel-level hand segmentation, egocentric daily activities |
| **Paper** | Li, C. & Kitani, K. "Pixel-Level Hand Detection in Ego-Centric Videos." CVPR 2013 |
| **Download** | [CMU](http://www.cs.cmu.edu/~kkitani/datasets/) |

### 84. UT Ego (2012)

| Field | Detail |
|-------|--------|
| **Scale** | 4 videos of ~3–5 h each (~17 h total), head-mounted cameras, daily activities |
| **Paper** | Lee, Y.J. et al. "Discovering Important People and Objects for Egocentric Video Summarization." CVPR 2012 |
| **Download** | [UT Austin](http://vision.cs.utexas.edu/projects/egocentric_data/UT_Egocentric_Dataset.html) |

### 85. Social Interactions (2012)

| Field | Detail |
|-------|--------|
| **Scale** | 8 social events, ~60 hours, head-mounted cameras, multiple participants per event |
| **Paper** | Fathi, A. et al. "Social Interactions: A First-Person Perspective." CVPR 2012 |
| **Download** | [Georgia Tech](https://cbs.ic.gatech.edu/fpv/) or contact authors |

### 86. ADL (2012)

| Field | Detail |
|-------|--------|
| **Scale** | 20 people, unscripted daily activities in their own homes, ~10 hours, 18 activity categories, 44 object classes with bounding boxes |
| **Paper** | Pirsiavash, H. & Ramanan, D. "Detecting Activities of Daily Living in First-Person Camera Views." CVPR 2012 |
| **Download** | [UMBC](https://www.csee.umbc.edu/~hpirsiav/papers/ADLdataset/) |

### 87. VINST / Visual Diaries (2011)

| Field | Detail |
|-------|--------|
| **Scale** | 31 egocentric videos capturing daily commutes; used for temporal segmentation and video summarization |
| **Paper** | Referenced in multiple egocentric vision surveys (circa 2011) |
| **Download** | N/A |

### 88. GTEA Gaze (2011)

| Field | Detail |
|-------|--------|
| **Scale** | 17 meal preparation sessions, 7 cooking activities, gaze tracking annotations |
| **Paper** | Fathi, A. et al. "Learning to Recognize Objects in Egocentric Activities." CVPR 2011 |
| **Download** | [Georgia Tech](https://cbs.ic.gatech.edu/fpv/) |

### 89. EgoAction (2011)

| Field | Detail |
|-------|--------|
| **Scale** | First-person sports videos (skateboarding, skiing, cycling, etc.), unsupervised ego-action categorization |
| **Paper** | Kitani, K.M. et al. "Fast Unsupervised Ego-Action Learning for First-Person Sports Videos." CVPR 2011 |
| **Download** | N/A |

### 90. CMU-MMAC (2009/2011)

| Field | Detail |
|-------|--------|
| **Scale** | 25 subjects, 5 cooking recipes. Multimodal: video (multiple views incl. egocentric), audio, IMU, motion capture. ~12 hours total. |
| **Paper** | De la Torre, F. et al. "Guide to the Carnegie Mellon University Multimodal Activity (CMU-MMAC) Database." CMU Tech Report, 2009/2011 |
| **Download** | [CMU Kitchen](http://kitchen.cs.cmu.edu/) (registration + license) |

### 91. Handled Objects (2009)

| Field | Detail |
|-------|--------|
| **Scale** | 11 object categories, multiple grasp sequences, RGB + depth from wearable camera |
| **Paper** | Ren, X. & Philipose, M. "Egocentric Recognition of Handled Objects: Benchmark and Analysis." CVPR Workshop 2009 |
| **Download** | N/A |

---

*Last updated 2026-03-21.*
