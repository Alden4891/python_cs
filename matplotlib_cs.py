# Matplotlib Cheat Sheet

import matplotlib.pyplot as plt

# Basic Plotting
# Line Plot:
# Comment: Creates a simple line plot.
# Syntax: plt.plot(x, y)
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Scatter Plot:
# Comment: Creates a scatter plot with points.
# Syntax: plt.scatter(x, y)
plt.scatter(x, y, color='red', marker='o')
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Bar Plot:
# Comment: Creates a bar plot.
# Syntax: plt.bar(x, height)
x = ['A', 'B', 'C', 'D', 'E']
height = [[3], [7], [5], [2], [6]]
plt.bar(x, height, color='blue')
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()


# Bar Plot (2 series):
# Comment: Creates a bar plot.
# Syntax: plt.bar(x, height)
import matplotlib.pyplot as plt
import numpy as np
categories = ['A', 'B', 'C', 'D']
series1 = [10, 20, 15, 25]
series2 = [12, 18, 20, 22]
bar_width = 0.35
index = np.arange(len(categories))
fig, ax = plt.subplots()
bar1 = ax.bar(index, series1, bar_width, label='Series 1') # use ax.barh to make it horizontal; 
bar2 = ax.bar(index + bar_width, series2, bar_width, label='Series 2') #add bottom=series1 before the label to make it stakable (left=series1 for barh)

ax.set_xlabel('Category')
ax.set_ylabel('Values')
ax.set_title('Bar Chart with Two Series')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(categories)
ax.legend()
plt.tight_layout()
plt.show()


# Histogram:
# Comment: Creates a histogram.
# Syntax: plt.hist(data, bins)
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=30, color='green', edgecolor='black')
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Pie Chart:
# Comment: Creates a pie chart.
# Syntax: plt.pie(sizes, labels)
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

# Subplots:
# Comment: Creates multiple plots in one figure.
# Syntax: plt.subplot(rows, cols, index)
plt.subplot(2, 1, 1)  # (2 rows, 1 column, 1st plot)
plt.plot(x, y, 'r-')
plt.title("Subplot 1")

plt.subplot(2, 1, 2)  # (2 rows, 1 column, 2nd plot)
plt.scatter(x, y, c='blue')
plt.title("Subplot 2")

plt.tight_layout()  # Adjust layout
plt.show()

# Customizing Plots
# Adding Legends:
# Comment: Adds a legend to the plot.
# Syntax: plt.legend([label1, label2])
plt.plot(x, y, label='Line')
plt.scatter(x, y, label='Scatter', color='red')
plt.legend()
plt.show()

# Customizing Colors and Styles:
# Comment: Change line color and style.
# Syntax: plt.plot(x, y, color='color_name', linestyle='style')
plt.plot(x, y, color='green', linestyle='--', marker='o')
plt.show()

# Adding Grid:
# Comment: Adds grid lines to the plot.
# Syntax: plt.grid(True)
plt.plot(x, y)
plt.grid(True)
plt.show()

# Saving Plots:
# Comment: Saves the current figure to a file.
# Syntax: plt.savefig(filename)
plt.plot(x, y)
plt.title("Saved Plot")
plt.savefig("plot.png")

# Formatting Dates:
# Comment: Format x-axis for dates.
# Syntax: plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
import matplotlib.dates as mdates
import pandas as pd
dates = pd.date_range('2023-01-01', periods=5)
values = [1, 2, 3, 4, 5]
plt.plot(dates, values)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.title("Date Formatting")
plt.show()

# 3D Plotting:
# Comment: Creates a 3D plot.
# Syntax: from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
ax.plot_surface(x, y, z, cmap='viridis')
plt.title("3D Surface Plot")
plt.show()

# Annotations:
# Comment: Adds annotations to the plot.
# Syntax: plt.annotate(text, xy)
plt.plot(x, y)
plt.annotate('Max value', xy=(x[3], y[3]), xytext=(x[3]+1, y[3]+1),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()

# Tight Layout:
# Comment: Automatically adjust subplot parameters to give specified padding.
# Syntax: plt.tight_layout()
plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.subplot(2, 2, 2)
plt.scatter(x, y)
plt.tight_layout()
plt.show()

# Plotting with Seaborn:
# Comment: Use Seaborn for advanced statistical plots.
# Syntax: import seaborn as sns
# Example:
import seaborn as sns
import pandas as pd
df = pd.DataFrame({
    "x": np.linspace(0, 10, 100),
    "y": np.sin(np.linspace(0, 10, 100))
})
sns.lineplot(data=df, x='x', y='y')
plt.title("Seaborn Line Plot")
plt.show()
