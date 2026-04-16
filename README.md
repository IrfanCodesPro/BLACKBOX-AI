# Reality-Aware Camera System
### The Camera That Understands What Should NOT Be Seen

**Developed by ShaTech**

---

## Project Overview
Standard surveillance systems blindly record everything, creating massive privacy liabilities and data storage overhead. The **Reality-Aware Camera System** creates a paradigm shift by introducing a **Pre-Recording Decision Engine**. 

It utilizes Computer Vision and Machine Learning to analyze the "Ethical Context" of a scene in real-time. Based on this analysis, it chooses one of four actions:
1. **FULL_RECORD**: High-priority security event.
2. **BLUR_SENSITIVE**: Privacy risk detected; recording proceeds with obfuscation.
3. **TEXT_SUMMARY**: Visuals are unnecessary or intrusive; a generative text log is created instead.
4. **IGNORE**: No relevant activity; saves storage and processing power.

## System Architecture
- **Vision Layer**: OpenCV-based feature extraction (Motion, Entropy, Contour Density).
- **ML Core**: Scikit-Learn Random Forest Classifier for activity recognition.
- **Decision Engine**: ShaTech Proprietary Logic for sensitivity scoring.
- **GenAI Module**: Dynamic natural language generation for human-readable context logs.
- **Web Interface**: Flask-based real-time dashboard.

## Deployment & Usage
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
