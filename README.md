<!-- RAASC — Reality-Aware Camera System | ShaTech Systems Division -->

<div align="center">

```
██████╗  █████╗  █████╗ ███████╗ ██████╗
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝███████║███████║███████╗██║
██╔══██╗██╔══██║██╔══██║╚════██║██║
██║  ██║██║  ██║██║  ██║███████║╚██████╗
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝
```

**`REALITY-AWARE CAMERA SYSTEM`** &nbsp;·&nbsp; `v2.0` &nbsp;·&nbsp; `ShaTech Systems Division`

*The camera that understands what should **not** be seen.*

---

![Python](https://img.shields.io/badge/Python-3.10+-00deb4?style=flat-square&logo=python&logoColor=white&labelColor=0d1318)
![Flask](https://img.shields.io/badge/Flask-2.x-00a8ff?style=flat-square&logo=flask&logoColor=white&labelColor=0d1318)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-00deb4?style=flat-square&logo=opencv&logoColor=white&labelColor=0d1318)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-RF_Classifier-00a8ff?style=flat-square&logo=scikitlearn&logoColor=white&labelColor=0d1318)
![License](https://img.shields.io/badge/License-MIT-b0a0ff?style=flat-square&labelColor=0d1318)

</div>

---

## `[01]` — Overview

Standard surveillance systems **blindly record everything** — creating massive privacy liabilities, storage overhead, and ethical blind spots.

**RAASC** introduces a paradigm shift: a **Pre-Recording Decision Engine** that analyzes the *Ethical Context* of a scene in real-time using Computer Vision and Machine Learning. Before a single frame is committed to disk, RAASC determines the most appropriate action.

> *"Don't record what doesn't need to be recorded."*

---

## `[02]` — Decision Engine

The core of RAASC. Every scene is evaluated and routed to one of four actions:

| ID | Action | Trigger | Behavior |
|:--:|--------|---------|----------|
| `01` | **`FULL_RECORD`** | High-priority security event | Full video capture initiated |
| `02` | **`BLUR_SENSITIVE`** | Privacy risk detected | Recording proceeds with real-time obfuscation |
| `03` | **`TEXT_SUMMARY`** | Visual recording unnecessary/intrusive | GenAI produces a human-readable context log |
| `04` | **`IGNORE`** | No relevant activity | Storage and processing cycles preserved |

---

## `[03]` — System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    RAASC PIPELINE                        │
├──────────┬──────────────────────────────────────────────┤
│  L1      │  Vision Layer                                 │
│          │  OpenCV · Motion · Entropy · Contour Density  │
├──────────┼──────────────────────────────────────────────┤
│  L2      │  ML Core                                      │
│          │  Scikit-Learn Random Forest Classifier        │
├──────────┼──────────────────────────────────────────────┤
│  L3      │  Decision Engine                              │
│          │  ShaTech Proprietary Sensitivity Scoring      │
├──────────┼──────────────────────────────────────────────┤
│  L4      │  GenAI Module                                 │
│          │  Dynamic NL Generation · Context Logs         │
├──────────┼──────────────────────────────────────────────┤
│  L5      │  Web Interface                                │
│          │  Flask Dashboard · Real-Time Feed · Overlay   │
└──────────┴──────────────────────────────────────────────┘
```

---

## `[04]` — Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Vision | `OpenCV 4.x` | Frame capture, motion detection, feature extraction |
| ML | `Scikit-Learn` | Random Forest scene classification |
| Backend | `Flask 2.x` | API server, decision routing, WebSocket feed |
| GenAI | `Groq / OpenAI API` | Natural language context log generation |
| Frontend | `HTML · CSS · JS` | Real-time dashboard with live decision overlay |
| Storage | `SQLite` | Lightweight event and log persistence |

---

## `[05]` — Project Structure

```
RAASC/
├── app.py                  # Flask entry point & routing
├── camera.py               # OpenCV capture & feature extraction
├── model/
│   ├── train_model.py      # RF Classifier training script
│   └── model.pkl           # Trained model artifact
├── engine/
│   ├── decision.py         # ShaTech Decision Engine logic
│   └── sensitivity.py      # Sensitivity scoring module
├── genai/
│   └── summarizer.py       # GenAI context log generator
├── templates/
│   └── dashboard.html      # Real-time web interface
├── static/                 # CSS, JS, assets
├── config.py               # System configuration
├── requirements.txt        # Python dependencies
└── README.md
```

---

## `[06]` — Installation & Deployment

### Prerequisites

- Python `3.10+`
- Webcam or RTSP IP camera
- API key for GenAI module (Groq / OpenAI)

---

### Step 01 — Clone & Install

```bash
git clone https://github.com/ShaTech/RAASC.git
cd RAASC
pip install -r requirements.txt
```

---

### Step 02 — Configure

Edit `config.py` to match your environment:

```python
# Camera source
CAMERA_SOURCE = 0              # 0 = default webcam
CAMERA_SOURCE = "rtsp://..."   # IP / CCTV camera stream

# Decision thresholds
SENSITIVITY   = 0.75           # Float 0.0–1.0 (higher = stricter)
BLUR_STRENGTH = 25             # Gaussian blur kernel size

# GenAI
GENAI_PROVIDER = "groq"        # "groq" | "openai"
GENAI_API_KEY  = "sk-..."      # Your API key
```

---

### Step 03 — Train the Classifier

```bash
python model/train_model.py
# Output: model/model.pkl
```

> The training script uses OpenCV-extracted features (motion delta, entropy, contour density) labeled across four activity classes. Swap in your own dataset via `data/training_scenes/` for domain-specific accuracy.

---

### Step 04 — Launch

```bash
python app.py
```

Open the dashboard at **`http://localhost:5000`**

---

## `[07]` — Dashboard Interface

The real-time Flask dashboard provides:

- **Live camera feed** with decision overlay (`FULL_RECORD` / `BLUR_SENSITIVE` / `TEXT_SUMMARY` / `IGNORE`)
- **Event log panel** — timestamped decisions with confidence scores
- **Context log viewer** — GenAI-generated text summaries for `TEXT_SUMMARY` events
- **Sensitivity slider** — adjust the decision threshold live without restarting

---

## `[08]` — How the Decision Engine Works

```
Frame Captured
      │
      ▼
Feature Extraction (OpenCV)
  · Motion delta
  · Entropy score
  · Contour density
      │
      ▼
Random Forest Classifier
  → Predicts: activity class + confidence
      │
      ▼
ShaTech Sensitivity Scoring
  · Weights: activity class × scene entropy × motion magnitude
      │
      ├──[score ≥ 0.90]──→ FULL_RECORD
      ├──[score ≥ 0.65]──→ BLUR_SENSITIVE
      ├──[score ≥ 0.35]──→ TEXT_SUMMARY
      └──[score < 0.35]──→ IGNORE
```

---

## `[09]` — Example Output

**`TEXT_SUMMARY` log entry (GenAI-generated):**

```
[2026-04-21 | 14:32:07] · ACTION: TEXT_SUMMARY · CONFIDENCE: 0.71
────────────────────────────────────────────────────────────
Two individuals observed in corridor near Room 204. Low motion
activity detected. No security-relevant behaviour identified.
Privacy preservation enforced. No visual record retained.
────────────────────────────────────────────────────────────
```

---

## `[10]` — Configuration Reference

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `CAMERA_SOURCE` | `int / str` | `0` | Webcam index or RTSP URL |
| `SENSITIVITY` | `float` | `0.75` | Decision threshold (0.0–1.0) |
| `BLUR_STRENGTH` | `int` | `25` | Gaussian blur kernel for `BLUR_SENSITIVE` |
| `GENAI_PROVIDER` | `str` | `"groq"` | AI provider for text summaries |
| `LOG_RETENTION_DAYS` | `int` | `30` | Days to retain event logs |
| `DASHBOARD_PORT` | `int` | `5000` | Flask server port |

---

## `[11]` — Requirements

```
opencv-python>=4.8.0
scikit-learn>=1.3.0
flask>=2.3.0
numpy>=1.24.0
groq>=0.4.0          # or openai>=1.0.0
pillow>=9.5.0
```

---

## `[12]` — Team

<div align="center">

**Developed under** &nbsp;`ShaTech Systems Division`

| Role | Contributor |
|------|------------|
| Project Lead | — |
| ML / Vision | — |
| Backend / API | — |
| Frontend / UI | — |

</div>

---

## `[13]` — License

```
MIT License · ShaTech Systems Division · 2026
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software to use, copy, modify, merge, and distribute,
subject to the conditions of the MIT License.
```

---

<div align="center">

`RAASC` &nbsp;·&nbsp; `ShaTech Systems Division` &nbsp;·&nbsp; `BUILD 2026`

*Intelligence before the record. Ethics before the lens.*

</div>
