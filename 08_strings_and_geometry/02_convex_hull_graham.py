"""
ALGORITHM: Computational Geometry (Graham Scan Convex Hull)

WHAT IT DOES (SIMPLY):
Imagine you hammer 100 nails into a flat wooden board. Then, you stretch a rubber band
around all of them and let it snap tight. The outer boundary formed by that rubber band
is the "Convex Hull". The Graham Scan algorithm finds this boundary efficiently by walking
around the outer perimeter and discarding any point that makes an "inward" (concave) dent.

REAL-LIFE USE CASES:
- Video Game Collision Detection: Enclosing complex 3D characters in simple hulls for instant hit testing.
- Self-Driving Cars & Robotics: Turning scattered LiDAR sensor dots into solid boundary boxes around cars/pedestrians.
- Geographic Mapping & Geofencing: Defining delivery zones and municipal borders based on customer addresses.
- Computer Vision: Detecting hand gestures by finding the outer perimeter of a silhouette to count extended fingers.
"""

import functools


# 2D cross product orientation: 0 = collinear, 1 = counter-clockwise, 2 = clockwise
def orientation(p1, p2, p3):
    val = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (
        p3[0] - p1[0]
    )
    if val == 0:
        return 0
    return 1 if val > 0 else 2


# Squared Euclidean distance (avoids float square root)
def dist_sq(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


# Graham Scan algorithm for 2D Convex Hull
def convex_hull(points):
    n = len(points)
    if n < 3:
        return points

    # Bottom-most point (tie-break with left-most)
    pivot = min(points, key=lambda p: (p[1], p[0]))

    def polar_cmp(p1, p2):
        o = orientation(pivot, p1, p2)
        if o == 0:
            return -1 if dist_sq(pivot, p1) < dist_sq(pivot, p2) else 1
        return -1 if o == 1 else 1

    others = [p for p in points if p != pivot]
    sorted_pts = sorted(others, key=functools.cmp_to_key(polar_cmp))

    hull = [pivot, sorted_pts[0]]
    for i in range(1, len(sorted_pts)):
        while (
            len(hull) >= 2
            and orientation(hull[-2], hull[-1], sorted_pts[i]) != 1
        ):
            hull.pop()
        hull.append(sorted_pts[i])

    return hull


if __name__ == "__main__":
    pts = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]
    print(f"Hull vertices: {convex_hull(pts)}")
