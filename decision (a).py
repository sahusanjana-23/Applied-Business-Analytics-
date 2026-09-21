print("T110,SANJANA SAHU")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Create figure
fig, ax = plt.subplots(figsize=(12, 7))

ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis("off")

# Decision box
decision = FancyBboxPatch(
    (4.5, 6.5), 3, 1,
    boxstyle="round,pad=0.1",
    edgecolor="black",
    facecolor="lightblue"
)

ax.add_patch(decision)
ax.text(6, 7, "Business Decision", ha="center", va="center", fontsize=14)

# Launch Product
launch = FancyBboxPatch(
    (1, 4.5), 3, 1,
    boxstyle="round,pad=0.1",
    edgecolor="black",
    facecolor="lightgreen"
)

ax.add_patch(launch)
ax.text(2.5, 5, "Launch Product", ha="center", va="center", fontsize=12)

# Do not launch
no_launch = FancyBboxPatch(
    (8, 4.5), 3, 1,
    boxstyle="round,pad=0.1",
    edgecolor="black",
    facecolor="lightyellow"
)

ax.add_patch(no_launch)
ax.text(9.5, 5, "Do Not Launch", ha="center", va="center", fontsize=12)

# High demand
high = FancyBboxPatch(
    (0, 2), 3, 1,
    boxstyle="round,pad=0.1",
    edgecolor="black",
    facecolor="lightgreen"
)

ax.add_patch(high)
ax.text(
    1.5, 2.5,
    "High Demand\nP = 0.6\nProfit = ₹1,00,000",
    ha="center", va="center"
)

# Low demand
low = FancyBboxPatch(
    (3.5, 2), 3, 1,
    boxstyle="round,pad=0.1",
    edgecolor="black",
    facecolor="lightcoral"
)

ax.add_patch(low)
ax.text(
    5, 2.5,
    "Low Demand\nP = 0.4\nLoss = ₹30,000",
    ha="center", va="center"
)

# No launch outcome
certain = FancyBboxPatch(
    (8, 2), 3, 1,
    boxstyle="round,pad=0.1",
    edgecolor="black",
    facecolor="lightyellow"
)

ax.add_patch(certain)
ax.text(
    9.5, 2.5,
    "Certain Outcome\nProfit = ₹20,000",
    ha="center", va="center"
)

# Lines
ax.plot([6, 2.5], [6.5, 5.5], "k-")
ax.plot([6, 9.5], [6.5, 5.5], "k-")

ax.plot([2.5, 1.5], [4.5, 3], "k-")
ax.plot([2.5, 5], [4.5, 3], "k-")

ax.plot([9.5, 9.5], [4.5, 3], "k-")

# Labels
ax.text(3.8, 5.8, "Decision 1", fontsize=10)
ax.text(7.2, 5.8, "Decision 2", fontsize=10)

plt.title(
    "Decision Tree for Business Decision Making",
    fontsize=16
)

plt.show()
