import matplotlib.animation as animation 
import matplotlib.pyplot as plt
import pandas as pd
import os
from PIL import Image

def extractLastFrame(inGif, outFolder, outJpeg):
    frame = Image.open(inGif)

    frame.seek(frame.n_frames - 1)

    out_path = os.path.join(outFolder, f"{outJpeg}.jpeg")
    frame.save(out_path, 'GIF')

def animatedGraph(title, xLabel, yLabel, xAxis, yAxis, fps, time, file, folder):

    print("Please wait...")

    fig = plt.figure(figsize=(10, 6)) 
    axis = plt.axes(xlim =(0, 6.5), ylim =(0, 8.5)) 

    plt.plot(
        xAxis, yAxis,
        marker = 'o',
        linestyle = '-',
        color = "white",
    )

    line, = axis.plot([], [], lw = 5) 

    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)

    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.tight_layout()       # Prevents label cutoff
    
    def init(): 
        line.set_data([], []) 
        return line, 
    
    xdata, ydata = [], [] 
    
    def animate(i):
        x = (time*fps)/len(yAxis)

        a = i // x
        t = (i % x) / x

        if a < len(yAxis):
            xdata.append(a + t)
            ydata.append(yAxis[a] + (yAxis[min(a + 1, len(yAxis) - 1)] - yAxis[a]) * t)

        line.set_data(xdata, ydata)
        
        return line,
    
    os.mkdir(f"{folder}/{file}")

    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = time*fps, interval = 2, blit = True) 
    anim.save(f"{folder}/{file}/{file}.gif", writer="pillow", fps=fps)
    extractLastFrame(f"{folder}/{file}/{file}.gif", f"{folder}/{file}", file)

    print("Program completed")

df = pd.read_csv(r"C:\Users\LaraEdwards\Documents\dataAnalyticsProject2026\tests\folder\names.csv")

animatedGraph(
    title = "Activity Level by Name",
    xLabel = "Name",
    yLabel = "Activity Level",
    xAxis = df["name"],
    yAxis = df["activityLevel"],
    fps = 30,
    time = 7,
    file = "lineGraphTest",
    folder = "tests/folder"
)