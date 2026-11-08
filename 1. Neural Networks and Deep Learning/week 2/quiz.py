import numpy as np

# Generate a random 32x32 RGB image (pixel values from 0 to 255)
img = np.random.randint(0, 256, size=(32, 32, 3), dtype=np.uint8)

print("Original image shape:", img.shape)
print("Original image shape:", img)

# Reshape the image into a column vector
img_vector = img.reshape(-1, 1)

print("Reshaped vector shape:", img_vector.shape)

# Display the first 12 elements
print("\nFirst 12 elements:")
print(img_vector[:12])

# Verify that the values are preserved
assert np.array_equal(img_vector.flatten(), img.flatten())


a = np.random.randint(1, 12, size = (3, 4))
b = np.random.randint(1, 4, size=(1, 2))

print(a*b)