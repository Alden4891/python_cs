import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the normal distribution
mean = 0
std_dev = 1

# Create a range of x values
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)
y = norm.pdf(x, mean, std_dev)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='blue')

# Fill between the standard deviations
plt.fill_between(x, y, where=(x > mean - std_dev) & (x < mean + std_dev), color='blue', alpha=0.6, label='68.2%')
plt.fill_between(x, y, where=(x > mean - 2*std_dev) & (x < mean - std_dev), color='lightblue', alpha=0.6)
plt.fill_between(x, y, where=(x > mean + std_dev) & (x < mean + 2*std_dev), color='lightblue', alpha=0.6, label='95.4%')
plt.fill_between(x, y, where=(x > mean - 3*std_dev) & (x < mean - 2*std_dev), color='lightgray', alpha=0.6)
plt.fill_between(x, y, where=(x > mean + 2*std_dev) & (x < mean + 3*std_dev), color='lightgray', alpha=0.6, label='99.7%')

# Add annotations for the percentage areas
plt.text(mean, 0.05, '34.1%', ha='center', fontsize=12)
plt.text(mean - 1.5*std_dev, 0.02, '13.6%', ha='center', fontsize=12)
plt.text(mean + 1.5*std_dev, 0.02, '13.6%', ha='center', fontsize=12)
plt.text(mean - 2.5*std_dev, 0.005, '2.1%', ha='center', fontsize=12)
plt.text(mean + 2.5*std_dev, 0.005, '2.1%', ha='center', fontsize=12)

# Labels and title
plt.title('Normal Distribution with Standard Deviations')
plt.xlabel('X')
plt.ylabel('Probability Density')

# Show the grid
plt.grid(True)

# Show the legend
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()
