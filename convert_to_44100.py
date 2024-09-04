import os
import librosa
import soundfile as sf

# Path to your non-gunshot folder
non_gunshot_folder = r"C:\Users\vinee\PycharmProjects\SonicTrace\archive (2)\Audio Wise V1.0-20220916T202003Z-001\Audio Wise V1.0"
output_folder = r"C:\Users\vinee\PycharmProjects\SonicTrace\converted_non_gunshots"

# Create the output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Function to convert audio files to 44100 Hz
def convert_to_44100(file_path, output_path):
    y, sr = librosa.load(file_path, sr=44100)
    sf.write(output_path, y, sr)

# Loop through all files in the non-gunshot folder
for file_name in os.listdir(non_gunshot_folder):
    if file_name.endswith(".wav"):
        file_path = os.path.join(non_gunshot_folder, file_name)
        output_path = os.path.join(output_folder, file_name)
        convert_to_44100(file_path, output_path)
        print(f"Converted {file_name} to 44100 Hz")

print("Conversion completed!")
