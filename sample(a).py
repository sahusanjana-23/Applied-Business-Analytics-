print("T110 SANJANA SAHU")
#(a) Conduct a Survey and Collect Sample Data
import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = [2, 3, 4, 2, 5, 3, 4, 6, 3, 2,
        4, 5, 3, 4, 2, 6, 5, 3, 4, 2,
        3, 5, 4, 6, 3, 2, 4, 5, 3, 4]


# Calculate sample mean
sample_mean = np.mean(data)

print("Sample Size:", len(data))
print("Sample Mean:", sample_mean)

plt.hist(data, bins=range(2, 8), edgecolor='black')
plt.xlabel("Daily Study Hours")
plt.ylabel("Number of Students")
plt.title("Survey Data")
plt.show()
