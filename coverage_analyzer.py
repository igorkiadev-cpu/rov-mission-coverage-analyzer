import pandas as pd
import plotly.express as px
import math

# Load mission data
data = pd.read_csv("mission_data.csv")

# Calculate distance traveled
total_distance = 0

for i in range(1, len(data)):
    x1, y1 = data.loc[i-1, ["x", "y"]]
    x2, y2 = data.loc[i, ["x", "y"]]

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    total_distance += distance

# Mission stats
max_depth = data["depth"].max()
avg_depth = data["depth"].mean()

print("ROV Mission Coverage Analysis")
print("----------------------------")
print(f"Total distance traveled: {total_distance:.2f} meters")
print(f"Maximum depth: {max_depth:.2f} m")
print(f"Average depth: {avg_depth:.2f} m")

# Plot trajectory
fig = px.line(
    data,
    x="x",
    y="y",
    title="ROV Inspection Trajectory"
)

fig.show()
