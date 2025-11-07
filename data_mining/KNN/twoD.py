"""
Run KNN with Three Dimension Dataset
"""
from knn import KNearestNeighbors
import matplotlib.pyplot as plt


points = {
    "blue": [[2, 4], [1, 3], [2, 3], [3, 2], [2, 1]],
    "orange": [[5, 6], [4, 5], [4, 6], [6, 6], [5, 4]],
}

new_point = [3, 3]

clf = KNearestNeighbors(k=3)
clf.fit(points)
print(clf.predict(new_point))

# Visualize KNN Distances

# 2D Example
ax = plt.subplot()
ax.grid(False, color="#000000")

ax.set_facecolor("black")
ax.figure.set_facecolor("#121212")
ax.tick_params(axis="x", colors="white")
ax.tick_params(axis="y", colors="white")

for point in points["blue"]:
    ax.scatter(point[0], point[1], color="#104DCA", s=60)

for point in points["orange"]:
    ax.scatter(point[0], point[1], color="#EF6C35", s=60)

new_class = clf.predict(new_point)
color = "#EF6C35" if new_class == "orange" else "#104DCA"
ax.scatter(new_point[0], new_point[1], color=color, marker="*", s=200, zorder=100)

for point in points["blue"]:
    ax.plot(
        [new_point[0], point[0]],
        [new_point[1], point[1]],
        color="#104DCA",
        linestyle="--",
        linewidth=1,
    )

for point in points["orange"]:
    ax.plot(
        [new_point[0], point[0]],
        [new_point[1], point[1]],
        color="#EF6C35",
        linestyle="--",
        linewidth=1,
    )

plt.show()