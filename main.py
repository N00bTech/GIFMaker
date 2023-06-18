from moviepy.editor import *
from tkinter import Tk
from tkinter.filedialog import askopenfilenames


def image_collector():
    Tk().withdraw()
    files = askopenfilenames()
    images = []
    for image in files:
        images.append(image)
    return images

def create_gif(in_video, out_gif):
    video = VideoFileClip(in_video)
    video_slowed = video.speedx(0.3)
    video_slowed.write_gif(out_gif, fps=3)
    return None


if __name__ == "__main__":
    images = image_collector()
    for image in images:
        image_wo_ext = image.strip('.jpg')
        image_gif = f"{image_wo_ext}.gif"
        create_gif(image, image_gif)