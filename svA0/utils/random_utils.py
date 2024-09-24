import random

def get_random_position():
    return (random.uniform(0, 1), random.uniform(0, 1))

def get_random_color():
    return 'white'
    choices = [
        (0,0,1),  # Blue
        (0,1,0),  # Green
        (1,0,0)   # Red
    ]
    return choices[random.randint(0, len(choices) - 1)]