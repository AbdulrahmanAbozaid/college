"""
KNN Classifier Implementaion
"""
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def euclidean_distance(p, q):
    """Euclidean distance between two points"""
    return np.sqrt(np.sum((np.array(p) - np.array(q)) ** 2))


class KNearestNeighbors:
    """The k-nearest neighbors algorithm"""

    def __init__(self, k=3):
        """Initialize the algo"""
        self.k = k
        self.points = None

    def fit(self, points):
        """Setting the DataSet"""
        self.points = points

    def predict(self, new_point):
        """Predict the Class"""
        distances = []

        for category in self.points:
            for point in self.points[category]:
                distance = euclidean_distance(point, new_point)
                distances.append([distance, category])

        categories = [category[1] for category in sorted(distances)[: self.k]]
        result = Counter(categories).most_common(1)[0][0]
        return result


if __name__ == "__main__":
    points = {
        "blue": [[2, 4], [1, 3], [2, 3], [3, 2], [2, 1]],
        "orange": [[5, 6], [4, 5], [4, 6], [6, 6], [5, 4]],
    }
    new_point = [3, 3]

    clf = KNearestNeighbors(k=3)
    clf.fit(points)
    print(clf.predict(new_point))
