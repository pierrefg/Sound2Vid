import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random
import librosa

import os

from geometry.Square import Square
from geometry.Triangle import Triangle
from utils.animation_utils import init_fig, export_animation
from utils.random_utils import get_random_position

class SoundPart():
    def __init__(self, name, path, fps): 
        self.name = name
        self.path = path
        self.fps = fps

        # READING
        y, self.sr = librosa.load(self.path)
        
        # STATS
        self.duration = librosa.get_duration(y=y, sr=self.sr)
        self.n_frames = int(self.fps * self.duration)
        samples_per_frame = self.sr // self.fps
        
        # NORMALIZATION
        y = np.abs(y[:self.n_frames * samples_per_frame:samples_per_frame])
        y /= np.max(y)
        
        # STORING
        self.y = y

    def get_amplitude(self, frame):
        return self.y[frame]
        

sound_parts = {
    'drums': {
        'path': './sound/main drums.wav'
    },
    'bass_perc': {
        'path': './sound/main bass_perc.wav'
    },
}

fps = 24 

print('Loading sounds...')
for part in sound_parts:
    sound_parts[part] = SoundPart(
        part,
        sound_parts[part]['path'],
        fps
    )
print('Done.')

# Initialize the figure
fig, ax = init_fig()

# Initialize the plot
def init():
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return []

# List to store the drawn shapes (alive ones)
shapes = []

# Update function for animation
def update(frame):
    global shapes    

    # Remove shapes that are dead
    shapes = [shape for shape in shapes if shape.live()]

    percussion_amp = (sound_parts['drums'].get_amplitude(frame)+sound_parts['bass_perc'].get_amplitude(frame))/2
    if percussion_amp>0.25:
        shapes.append(Square(ax, get_random_position()))

    if percussion_amp>0.25:
        shapes.append(Triangle(ax, get_random_position()))

    # Only return alive shapes for blitting
    remaining_shapes = [shape.shape for shape in shapes if not shape.is_dead]
    return remaining_shapes

print('Computing animation...')
ref_sound = 'drums'
ani = FuncAnimation(
    fig, 
    update,
    frames=sound_parts[ref_sound].n_frames,
    init_func=init, 
    blit=True
)
print('Done.')

print('Exporting animation...')
export_animation(ani, './sound/main.wav')
print('Done.')
