import random

from geometry.Polygon import Polygon

class Square(Polygon):
    def __init__(self, ax, center, size=None, color=None, frames_to_live=None, rotation_speed=None): 
        if size is None: size = random.uniform(0.05, 0.3)   
        x, y = center
        points = [
            (x - size / 2, y - size / 2),
            (x + size / 2, y - size / 2),
            (x + size / 2, y + size / 2),
            (x - size / 2, y + size / 2)
        ]
        super().__init__(ax, points, center, color, frames_to_live, rotation_speed)