import os

# Path to the non-gunshot folder
non_gunshot_folder = r'C:\Users\vinee\PycharmProjects\SonicTrace\converted_non_gunshots'

# Desired prefix for the renamed files
new_prefix = 'non_gunshot_'

# Get all files in the non-gunshot folder
files = os.listdir(non_gunshot_folder)

# Filter only .wav files (assuming all files are .wav)
wav_files = [f for f in files if f.endswith('.wav')]

# Sort the files to maintain order
wav_files.sort()

# Renaming the files, starting from 0
for i, file_name in enumerate(wav_files):
    # Construct the old and new file paths
    old_file_path = os.path.join(non_gunshot_folder, file_name)
    new_file_name = f'{new_prefix}{i}.wav'
    new_file_path = os.path.join(non_gunshot_folder, new_file_name)

    # Rename the file
    os.rename(old_file_path, new_file_path)
    print(f'Renamed: {file_name} -> {new_file_name}')

print("Renaming complete!")
