import numpy as np

def rotate(points, angle, center):
    """Rotate points by a given angle (in radians) around a center."""
    c, s = np.cos(angle), np.sin(angle)
    cx, cy = center
    new_points = []
    for x, y in points:
        # Translate point back to origin:
        x -= cx
        y -= cy
        # Rotate point
        x_new = x * c - y * s
        y_new = x * s + y * c
        # Translate point back
        x_new += cx
        y_new += cy
        new_points.append((x_new, y_new))
    return new_points