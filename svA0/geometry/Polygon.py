import matplotlib.pyplot as plt
import random

from geometry.Drawing import Drawing
from utils.random_utils import get_random_color
from utils.geometry_utils import rotate

class Polygon(Drawing):
    def __init__(self, ax, points, center, color=None, frames_to_live=None, rotation_speed=None):
        if color is None: color = get_random_color()
        if rotation_speed is None: rotation_speed=random.uniform(-0.01, 0.01)

        super().__init__(ax, frames_to_live)
        self.points = points  # Store original points for rotation
        self.center = center
        self.rotation_speed = rotation_speed
        self.angle = 0  # Initial angle of rotation
        self.shape = plt.Polygon(points, color=color, animated=True)
        self.ax.add_patch(self.shape)  # Add the shape to the axes once

    def update(self):
        """Update and rotate the polygon shape."""
        if not super().update():  # Call the parent class's update method
            return False
        # Apply rotation
        self.angle += self.rotation_speed
        rotated_points = rotate(self.points, self.angle, self.center)
        # Update the shape with the new rotated points
        self.shape.set_xy(rotated_points)
        return True