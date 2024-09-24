import random

class Drawing:
    def __init__(self, ax, frames_to_live=None):
        if frames_to_live is None: frames_to_live=random.randint(3, 40)

        self.ax = ax
        self.remaining_frames = frames_to_live
        self.is_dead = False
        self.shape = None

    def update(self):
        """Update the shape state, reducing lifespan."""
        self.remaining_frames -= 1
        if self.remaining_frames <= 0:
            self.is_dead = True
            self.shape.remove()  # Remove the shape from the canvas
        return not self.is_dead  # Return whether the shape is still alive

    def live(self):
        """Handles shape updates each frame and checks if it's still alive."""
        return self.update()