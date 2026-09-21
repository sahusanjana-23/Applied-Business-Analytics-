print("T110,SANJANA SAHU")
import numpy as np
import matplotlib.pyplot as plt

# Population
population = np.array([
    2, 3, 4, 2, 5, 3, 4, 6, 3, 2,
    4, 5, 3, 4, 2, 6, 5, 3, 4, 2,
    3, 5, 4, 6, 3, 2, 4, 5, 3, 4
])

# Generate sample means
sample_means = []

for i in range(1000):
    sample = np.random.choice(population, size=10, replace=True)
    sample_means.append(np.mean(sample))

# Mean of sampling distribution
mean_of_means = np.mean(sample_means)
std_of_means = np.std(sample_means)

print("Mean of Sampling Distribution:", mean_of_means)
print("Standard Deviation of Sampling Distribution:", std_of_means)

# Plot
plt.hist(sample_means, bins=30, edgecolor='black')
plt.xlabel("Sample Means")
plt.ylabel("Frequency")
plt.title("Sampling Distribution of Sample Mean")
plt.show()
