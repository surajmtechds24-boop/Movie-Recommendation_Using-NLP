# Movie-Recommendation_Using-NLP

# PCB Defect Inspection System

**Automated optical inspection for printed circuit boards — detect, localize, and classify six manufacturing defects.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Demo: `[add Streamlit / Hugging Face Space URL]`  
> Report: `[add link to your PDF / PPT]`

---

## Why this exists

Manual PCB inspection is slow, inconsistent, and misses fine defects as board density increases. This project is an end-to-end **computer vision inspection pipeline** for six common bare-board defects used in academic and industrial AOI research:

| Class | What it looks like on the board |
|---|---|
| **Missing hole** | Drill hole absent where a via / pad should exist |
| **Mouse bite** | Small semi-circular nicks on a copper trace edge |
| **Open circuit** | Broken trace — electrical discontinuity |
| **Short** | Unintended copper bridge between nets |
| **Spur** | Unwanted protrusion from a trace |
| **Spurious copper** | Isolated extra copper island |

The system follows the industrial pattern: **reference comparison → defect localization → classification → annotated evidence**.

---

## Results at a glance

> Fill these from your notebooks before you publish. Do not invent numbers.

| Metric | Value | Notes |
|---|---|---|
| Task | 6-class defect classification after ROI crop | Plus localization via subtraction + contours |
| Dataset | `[PKU-Market-PCB / DeepPCB / other]` | `[N]` images, 6 classes |
| Train / val / test split | `[e.g. 70 / 15 / 15]` | Stratified by class |
| Backbone | `[EfficientNet-Bx / ResNet-50 / custom CNN]` | ImageNet init: `[yes/no]` |
| Validation accuracy | `[xx.x%]` | Best checkpoint |
| Test accuracy | `[xx.x%]` | Held-out only |
| Weighted F1 | `[0.xx]` | Use this if classes are uneven |
| Inference latency | `[xx ms / image]` | Hardware: `[CPU / GPU model]` |

**Per-class test metrics**

| Defect | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| Missing hole | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Mouse bite | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Open circuit | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Short | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Spur | `[ ]` | `[ ]` | `[ ]` | `[ ]` |
| Spurious copper | `[ ]` | `[ ]` | `[ ]` | `[ ]` |

**Error notes for interviews:** spur vs spurious copper and open vs mouse bite are the usual confusions because the local texture looks similar after a tight crop. `[Write 2–3 sentences from your confusion matrix.]`

Sample outputs are in [`Results/`](Results/).

---

## Pipeline

```text
Input board image
        │
        ▼
┌───────────────────────┐
│ 1. Preprocess         │  grayscale / CLAHE / align to template
└───────────┬───────────┘
            ▼
┌───────────────────────┐
│ 2. Localize           │  template match + image subtraction
│                       │  adaptive threshold + morphology
│                       │  contours → padded ROIs
└───────────┬───────────┘
            ▼
┌───────────────────────┐
│ 3. Classify           │  CNN on each ROI (6 classes)
└───────────┬───────────┘
            ▼
┌───────────────────────┐
│ 4. Report             │  boxes + labels + confidence
│                       │  JSON / CSV evidence pack
└───────────────────────┘
