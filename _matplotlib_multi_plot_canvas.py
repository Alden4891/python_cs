import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x / 3)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2x2 grid of subplots

# First subplot
axs[0, 0].plot(x, y1, 'r-')
axs[0, 0].set_title('Sine')

# Second subplot
axs[0, 1].plot(x, y2, 'g-')
axs[0, 1].set_title('Cosine')

# Third subplot
axs[1, 0].plot(x, y3, 'b-')
axs[1, 0].set_title('Tangent')
axs[1, 0].set_ylim(-10, 10)  # Limiting y-axis to avoid very large values

# Fourth subplot
axs[1, 1].plot(x, y4, 'm-')
axs[1, 1].set_title('Exponential')

plt.tight_layout()  # Adjust layout to prevent overlap
plt.show()
