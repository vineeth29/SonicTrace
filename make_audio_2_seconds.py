import os
from pydub import AudioSegment

# Path to the directory containing the audio files
audio_dir = r"C:\Users\vinee\PycharmProjects\SonicTrace\archive (2)\Audio Wise V1.0-20220916T202003Z-001\Audio Wise V1.0"

# Target duration (2 seconds in milliseconds)
target_duration = 2 * 1000

# Loop through each file in the directory
for filename in os.listdir(audio_dir):
    if filename.endswith('.wav') or filename.endswith('.mp3'):  # Adjust depending on your file types
        file_path = os.path.join(audio_dir, filename)
        audio = AudioSegment.from_file(file_path)

        # Check the current duration
        current_duration = len(audio)

        if current_duration > target_duration:
            # Trim the audio
            trimmed_audio = audio[:target_duration]
            trimmed_audio.export(file_path, format="wav")
        elif current_duration < target_duration:
            # Pad the audio
            silence_duration = target_duration - current_duration
            silence = AudioSegment.silent(duration=silence_duration)
            padded_audio = audio + silence
            padded_audio.export(file_path, format="wav")
        else:
            print(f"{filename} is already 2 seconds long.")

        print(f"Processed {filename}")

print("All files processed.")
