import os
import librosa
import numpy as np

# Set the path to the directory where your non-gun sound files are located
directory = r'C:\Users\vinee\PycharmProjects\SonicTrace\archive (2)'

# Set the threshold for white noise detection (lower values are more sensitive)
noise_threshold = 0.1


def is_white_noise(y, threshold=noise_threshold):
    # Compute the spectral flatness (ratio of geometric mean to arithmetic mean)
    S_flatness = librosa.feature.spectral_flatness(y=y)
    # Determine if the mean flatness exceeds the noise threshold
    return np.mean(S_flatness) > threshold


def process_files(directory):
    files = os.listdir(directory)
    for filename in files:
        if filename.endswith(".wav"):
            file_path = os.path.join(directory, filename)
            try:
                # Load the audio file
                y, sr = librosa.load(file_path, sr=None)

                # Check if the file is mostly white noise
                if is_white_noise(y):
                    print(f"File {filename} detected as white noise. Deleting...")
                    os.remove(file_path)
                else:
                    print(f"File {filename} retained.")
            except Exception as e:
                print(f"Error processing {filename}: {e}")


# Run the processing function
process_files(directory)
