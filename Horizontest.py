import matplotlib.pyplot as plt
import numpy as np

points = []
n = int(input("Enter number of points : "))
for i in range(n):
    x, y = map(float, input("Enter x and y coordinates : ").split())
    points.append((x, y))

xco, yco = zip(*points)

def dist(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

lines = []
connected = set()

for i, point in enumerate(points):
    nearest_neighbors = sorted([(dist(point, point2), point2) for j, point2 in enumerate(points) if i != j])
    for _, nearestp in nearest_neighbors:
        if (point, nearestp) not in connected and (nearestp, point) not in connected:
            lines.append((point, nearestp))
            connected.add((point, nearestp))
            connected.add((nearestp, point))
            break

plt.scatter(xco, yco)
for line in lines:
    xco2, yco2 = zip(*line)
    plt.plot(xco2, yco2, color='green')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Task 1")
plt.show()