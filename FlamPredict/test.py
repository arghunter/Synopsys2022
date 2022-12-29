from scipy.spatial import ConvexHull, convex_hull_plot_2d
import numpy as np;
# points=[(15,120),(15,290),(200,290),(100,130),(200,150),(200,120)];
points= np.array([[15,120],[15,290],[200,290],[100,130],[200,150],[200,120]])
# hull=ConvexHull(points);
rng = np.random.default_rng()
# points = rng.random((30, 2))
hull=ConvexHull(points)
print(hull.points[hull.vertices])
# print(points)
