# SonicTrace — Gunshot Detection & Localization

CNN-based gunshot detection trained on mel-spectrograms across ~3,000 audio clips spanning 9 firearm types.

## Results
- 92% training accuracy / 88% validation accuracy
- Sub-500ms inference
- GCC-PHAT TDOA localization via 4-microphone array

## Stack
- Python, PyTorch, librosa
- CNN on mel-spectrograms
- MFCC feature extraction
- 4-mic array signal processing

## Structure
- `gunshots/` — gunshot audio samples
- `converted_non_gunshots/` — non-gunshot samples
- `src/` — model training and inference scripts
