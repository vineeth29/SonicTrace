import numpy as np

# Load the features and labels
features = np.load('features.npy')
labels = np.load('labels.npy')

# Print the shape of the features and labels arrays
print(f"Features shape: {features.shape}")
print(f"Labels shape: {labels.shape}")

# Optionally, print a few samples to verify content
print("Sample features:", features[:5])
print("Sample labels:", labels[:5])
