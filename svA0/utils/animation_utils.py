import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip, AudioFileClip

def init_fig(size_px=600, dpi=72):
    width_inch = size_px / dpi
    height_inch = size_px / dpi

    fig, ax = plt.subplots(figsize=(width_inch, height_inch), dpi=dpi)
    fig.patch.set_facecolor('black')
    ax.set_facecolor('black')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    return fig, ax

def export_animation(ani, sound_path):
    ani.save('tmp.mp4', fps=24)

    video = VideoFileClip("tmp.mp4")
    audio = AudioFileClip(sound_path)

    final_video = video.set_audio(audio)
    final_video.write_videofile("main.mp4", fps=24)