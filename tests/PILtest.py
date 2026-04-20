import os
from PIL import Image

def extractLastFrame(inGif, outFolder):
    frame = Image.open(inGif)

    frame.seek(frame.n_frames - 1)

    out_path = os.path.join(outFolder, f"animationLastFrame.jpeg")
    frame.save(out_path, 'GIF')


extractLastFrame('animation.gif', 'tests')