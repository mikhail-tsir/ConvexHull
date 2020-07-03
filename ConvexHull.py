import numpy as np
import matplotlib.pyplot as plt

height = 600
width = 600
points = []
num_points = 25
hull = []

for point in range(num_points):
    points.append((np.random.uniform(0, width), np.random.uniform(0, height)))

    # points = [(1, 10), (2, 3), (3, 7), (5, 3), (5, 11), (9, 5)]

min_y = points[0]

# finds the lowest leftmost point
for p in points:
    if p[1] < min_y[1]:
        min_y = p
    elif p[1] == min_y[1]:
        if p[0] < min_y[0]:
            min_y = p


def heapify(arr, n, i, cur):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and get_cos(cur, arr[i]) < get_cos(cur, arr[l]):
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and get_cos(cur, arr[largest]) < get_cos(cur, arr[r]):
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest, cur)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i, min_y)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0, min_y)

# cosine between two points and the origin
def get_cos(p1, p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    mag = np.sqrt(x ** 2 + y ** 2)
    if mag == 0:
        return -1
    else:
        return float(-x / mag)

# < 0 if points are ccw, > 0 if clockwise
def ccw(p1, p2, p3):
    a12 = np.subtract(p2, p1)
    a13 = np.subtract(p3, p1)
    return np.cross(a12, a13)

# adds points to the hull
def get_hull():
    heapSort(points)

    for pt in points:
        while len(hull) > 1 and ccw(hull[-2], hull[-1], pt) < 0:
            hull.pop()
        hull.append(pt)

# plots the hull
def plot():
    for i in range(len(hull) - 1, -1, -1):
        plt.plot([hull[i][0], hull[i - 1][0]], [hull[i][1], hull[i - 1][1]],
                 marker='o', markersize=5, c='red', markerfacecolor='blue')
    plt.scatter([i_x[0] for i_x in points], [i_y[1] for i_y in points], s=10, c='blue')

    plt.show()


get_hull()
plot()

print(hull)
