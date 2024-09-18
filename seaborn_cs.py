# Seaborn Cheat Sheet

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set the default style and palette
sns.set(style="whitegrid")
sns.set_palette("pastel")

# Load example datasets
# Comment: Load built-in datasets for demonstration.
# Syntax: sns.load_dataset(name)
df = sns.load_dataset("tips")

# Basic Plotting
# Scatter Plot:
# Comment: Create a scatter plot.
# Syntax: sns.scatterplot(data, x, y)
sns.scatterplot(data=df, x="total_bill", y="tip", hue="day")
plt.title("Scatter Plot")
plt.show()

# Line Plot:
# Comment: Create a line plot.
# Syntax: sns.lineplot(data, x, y)
sns.lineplot(data=df, x="total_bill", y="tip", hue="day", style="day")
plt.title("Line Plot")
plt.show()

# Bar Plot:
# Comment: Create a bar plot.
# Syntax: sns.barplot(data, x, y)
sns.barplot(data=df, x="day", y="total_bill", hue="sex")
plt.title("Bar Plot")
plt.show()

# Histogram:
# Comment: Create a histogram.
# Syntax: sns.histplot(data, x)
sns.histplot(df["total_bill"], bins=20, kde=True)
plt.title("Histogram")
plt.show()

# Box Plot:
# Comment: Create a box plot.
# Syntax: sns.boxplot(data, x, y)
sns.boxplot(data=df, x="day", y="total_bill", hue="sex")
plt.title("Box Plot")
plt.show()

# Violin Plot:
# Comment: Create a violin plot.
# Syntax: sns.violinplot(data, x, y)
sns.violinplot(data=df, x="day", y="total_bill", hue="sex", split=True)
plt.title("Violin Plot")
plt.show()

# Heatmap:
# Comment: Create a heatmap.
# Syntax: sns.heatmap(data)
pivot_table = df.pivot_table(index="day", columns="sex", values="total_bill", aggfunc=np.mean)
sns.heatmap(pivot_table, annot=True, cmap="coolwarm")
plt.title("Heatmap")
plt.show()

# Pair Plot:
# Comment: Create a pair plot.
# Syntax: sns.pairplot(data)
sns.pairplot(df, hue="sex", vars=["total_bill", "tip"])
plt.title("Pair Plot")
plt.show()

# FacetGrid:
# Comment: Create a grid of subplots based on categories.
# Syntax: sns.FacetGrid(data, col, row)
g = sns.FacetGrid(df, col="day", row="time", margin_titles=True)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.set_axis_labels("Total Bill", "Tip")
g.add_legend()
plt.show()

# Joint Plot:
# Comment: Create a plot that combines scatter plot and marginal histograms.
# Syntax: sns.jointplot(data, x, y, kind)
sns.jointplot(data=df, x="total_bill", y="tip", kind="hex")
plt.title("Joint Plot")
plt.show()

# Regression Plot:
# Comment: Plot data and fit a regression model.
# Syntax: sns.regplot(data, x, y)
sns.regplot(data=df, x="total_bill", y="tip", scatter_kws={'s':50}, line_kws={'color':'red'})
plt.title("Regression Plot")
plt.show()

# Pair Plot with KDE:
# Comment: Create pair plot with kernel density estimates.
# Syntax: sns.pairplot(data, kind="kde")
sns.pairplot(df, hue="sex", kind="kde", diag_kind="kde")
plt.title("Pair Plot with KDE")
plt.show()

# Customizing Plots
# Set Style:
# Comment: Set the style of the plots.
# Syntax: sns.set_style("style")
sns.set_style("darkgrid")

# Set Palette:
# Comment: Set the color palette of the plots.
# Syntax: sns.set_palette("palette_name")
sns.set_palette("husl")

# Add Titles and Labels:
# Comment: Set the title and labels of the plot.
plt.title("Customized Plot")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")

# Saving Plots:
# Comment: Save the current figure to a file.
# Syntax: plt.savefig(filename)
plt.savefig("seaborn_plot.png")

# Example with Customizations
sns.set(style="darkgrid", palette="muted")
sns.scatterplot(data=df, x="total_bill", y="tip", hue="day", size="size", sizes=(20, 200))
plt.title("Customized Scatter Plot")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()
