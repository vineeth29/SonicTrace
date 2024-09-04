# Split the data into 80% training and 20% testing sets
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

# Save the training and testing data to files
np.save('X_train.npy', X_train)
np.save('X_test.npy', X_test)
np.save('y_train.npy', y_train)
np.save('y_test.npy', y_test)

# Check the number of samples in each set
print(f"Training data: {len(X_train)} samples")
print(f"Testing data: {len(X_test)} samples")
