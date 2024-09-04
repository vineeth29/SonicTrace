import os
import librosa
import numpy as np

# Paths to your folders
gunshot_folder = r"C:\Users\vinee\PycharmProjects\SonicTrace\gunshots"
non_gunshot_folder = r"C:\Users\vinee\PycharmProjects\SonicTrace\converted_non_gunshots"

# Function to extract features from an audio file
def extract_features(file_path):
    try:
        y, sr = librosa.load(file_path, sr=44100)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        mfccs_mean = np.mean(mfccs.T, axis=0)
        return mfccs_mean
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return None

# Prepare lists to store features and labels
features = []
labels = []

# Process gunshot files
folders = {
    'AK-12': 1,
    'AK-47': 2,
    'IMI Desert Eagle': 3,
    'M4': 4,
    'M16': 5,
    'M249': 6,
    'MG-42': 7,
    'MP5': 8,
    'Zastava M92': 9,
}

for folder_name, label in folders.items():
    folder_path = os.path.join(gunshot_folder, folder_name)
    if os.path.exists(folder_path):
        print(f"Processing gunshot folder: {folder_name}")
        for file_name in os.listdir(folder_path):
            if file_name.endswith(".wav"):
                file_path = os.path.join(folder_path, file_name)
                print(f"Processing file: {file_path}")
                mfccs_mean = extract_features(file_path)
                if mfccs_mean is not None:
                    features.append(mfccs_mean)
                    labels.append(label)

# Process non-gunshot files
print("Processing non-gunshot files...")
for file_name in os.listdir(non_gunshot_folder):
    if file_name.endswith(".wav"):
        file_path = os.path.join(non_gunshot_folder, file_name)
        print(f"Processing non-gunshot file: {file_path}")
        mfccs_mean = extract_features(file_path)
        if mfccs_mean is not None:
            features.append(mfccs_mean)
            labels.append(0)  # Label for non-gunshots

# Convert lists to numpy arrays for use in machine learning models
features = np.array(features)
labels = np.array(labels)

print(f"Extracted features from {len(features)} files.")

# Save the features and labels to a file
np.save('features.npy', features)
np.save('labels.npy', labels)
