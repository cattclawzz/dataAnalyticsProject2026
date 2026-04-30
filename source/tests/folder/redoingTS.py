import matplotlib.animation as animation 
import matplotlib.pyplot as plt
import pandas as pd
import os
from PIL import Image

df = pd.read_csv(r"C:\Users\LaraEdwards\Documents\dataAnalyticsProject2026\tests\folder\sample.csv")

def animatedLineGraph(data, xAxis, yAxis, xTitle = "", yTitle = "", title = "[Title]", time = 3, fps = 12):

    fig = plt.figure(figsize=(10, 6))
    axis = plt.axes() 
    
    plt.plot(
        data[xAxis],
        data[yAxis],
        marker='o', #TAKE THIS OUT AFTER DEBUGGING
        color = "lightGrey",
    )

    line, = axis.plot([], [], lw = 5)

    plt.title(title)
    plt.xlabel(xTitle if xTitle else xAxis)
    plt.ylabel(yTitle if yTitle else yAxis)
    plt.tight_layout()

    def init(): 
        line.set_data([], []) 
        return line,

    xData = []
    yData = []

    def animate(i):

        xData.append(data[xAxis][i%10])
        yData.append(data[yAxis][i%10])

        line.set_data(xData, yData)
        return line,

    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = time*fps, interval = 2, blit = True) 
    
    plt.show()

animatedLineGraph(
    data = df,
    xAxis = "x",
    yAxis = "fibo",
    yTitle = "Fibonacci Sequence"
)