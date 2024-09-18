# Plotly Cheat Sheet

# ------------------------------
# 1. Installing Plotly
# ------------------------------

# Install Plotly Package:
# Comment: Install the Plotly library from PyPI.
# Syntax: pip install plotly
pip install plotly

# ------------------------------
# 2. Importing Plotly
# ------------------------------

# Import Plotly Express:
# Comment: Plotly Express is a high-level interface for Plotly.
# Syntax: import plotly.express as alias
import plotly.express as px

# Import Plotly Graph Objects:
# Comment: Use for more detailed customizations.
# Syntax: import plotly.graph_objects as alias
import plotly.graph_objects as go

# ------------------------------
# 3. Basic Plotting with Plotly Express
# ------------------------------

# Scatter Plot:
# Comment: Creates a basic scatter plot.
# Syntax: px.scatter(data_frame, x, y, color, size, hover_data)
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", color="day", size="size", hover_data=["sex"])
fig.update_layout(title="Scatter Plot")
fig.show()

# Line Plot:
# Comment: Creates a basic line plot.
# Syntax: px.line(data_frame, x, y, color, line_dash)
fig = px.line(df, x="total_bill", y="tip", color="day", line_dash="sex")
fig.update_layout(title="Line Plot")
fig.show()

# Bar Plot:
# Comment: Creates a bar plot with grouped categories.
# Syntax: px.bar(data_frame, x, y, color, barmode)
fig = px.bar(df, x="day", y="total_bill", color="sex", barmode="group")
fig.update_layout(title="Bar Plot")
fig.show()

# Histogram:
# Comment: Creates a histogram with optional marginal plots.
# Syntax: px.histogram(data_frame, x, nbins, color, marginal)
fig = px.histogram(df, x="total_bill", nbins=20, color="sex", marginal="rug")
fig.update_layout(title="Histogram")
fig.show()

# Box Plot:
# Comment: Creates a box plot for showing distribution.
# Syntax: px.box(data_frame, x, y, color)
fig = px.box(df, x="day", y="total_bill", color="sex")
fig.update_layout(title="Box Plot")
fig.show()

# Violin Plot:
# Comment: Creates a violin plot to display data distribution.
# Syntax: px.violin(data_frame, x, y, color, box, points)
fig = px.violin(df, x="day", y="total_bill", color="sex", box=True, points="all")
fig.update_layout(title="Violin Plot")
fig.show()

# ------------------------------
# 4. Customizing Plotly Graphs
# ------------------------------

# Updating Titles:
# Comment: Add titles to the graph.
# Syntax: fig.update_layout(title="Title Name")
fig.update_layout(title="Customized Plot")

# Axis Labels:
# Comment: Set the axis labels.
# Syntax: fig.update_layout(xaxis_title="X-axis Label", yaxis_title="Y-axis Label")
fig.update_layout(xaxis_title="Total Bill", yaxis_title="Tip")

# Color Maps:
# Comment: Use different color maps for styling.
# Syntax: px.scatter(data_frame, x, y, color, color_continuous_scale="colormap")
fig = px.scatter(df, x="total_bill", y="tip", color="size", color_continuous_scale="Viridis")
fig.update_layout(title="Scatter Plot with Color Map")
fig.show()

# Save the Plot:
# Comment: Save the plot to a file.
# Syntax: fig.write_image("filename.png")
fig.write_image("plotly_scatter.png")

# ------------------------------
# 5. Advanced Plotting with Graph Objects
# ------------------------------

# Creating Subplots:
# Comment: Create subplots for more complex visualizations.
# Syntax: go.Figure(data=[go.Scatter(), go.Bar()])
fig = go.Figure()

fig.add_trace(go.Scatter(x=df["total_bill"], y=df["tip"], mode='markers', name="Scatter"))
fig.add_trace(go.Bar(x=df["day"], y=df["total_bill"], name="Bar Plot"))

# Customize Layout:
# Comment: Customize layout settings.
# Syntax: fig.update_layout(title="Title", xaxis_title="X Label", yaxis_title="Y Label")
fig.update_layout(title="Multiple Plots", xaxis_title="Day", yaxis_title="Total Bill")
fig.show()

# ------------------------------
# 6. Interactive Features
# ------------------------------

# Hover Data:
# Comment: Show additional data when hovering over points.
# Syntax: px.scatter(data_frame, x, y, hover_data=["column1", "column2"])
fig = px.scatter(df, x="total_bill", y="tip", hover_data=["day", "sex"])
fig.show()

# Adding Buttons for Interaction:
# Comment: Add buttons to switch between data views.
# Syntax: fig.update_layout(updatemenus=[...])
fig.update_layout(
    updatemenus=[
        dict(
            buttons=[
                dict(label="Scatter", method="update", args=[{"visible": [True, False]}]),
                dict(label="Bar", method="update", args=[{"visible": [False, True]}]),
            ]
        )
    ]
)
fig.show()

# ------------------------------
# 7. 3D Plots (with Plotly Express)
# ------------------------------

# 3D Scatter Plot:
# Comment: Create a 3D scatter plot.
# Syntax: px.scatter_3d(data_frame, x, y, z, color)
fig = px.scatter_3d(df, x="total_bill", y="tip", z="size", color="day")
fig.update_layout(title="3D Scatter Plot")
fig.show()
