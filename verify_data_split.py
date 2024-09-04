import numpy as np

# Load the training and testing data
X_train = np.load('X_train.npy')
X_test = np.load('X_test.npy')
y_train = np.load('y_train.npy')
y_test = np.load('y_test.npy')

# Print out the shapes of the arrays to check the sizes
print(f"X_train shape: {X_train.shape}")  # Expected: (number of training samples, number of features)
print(f"X_test shape: {X_test.shape}")    # Expected: (number of testing samples, number of features)
print(f"y_train shape: {y_train.shape}")  # Expected: (number of training samples,)
print(f"y_test shape: {y_test.shape}")    # Expected: (number of testing samples,)
