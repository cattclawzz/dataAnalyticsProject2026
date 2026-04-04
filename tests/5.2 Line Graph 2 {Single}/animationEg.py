import matplotlib.animation as animation 
import matplotlib.pyplot as plt
from celluloid import Camera
import pandas as pd

def animatedGraph(title, xLabel, yLabel, xAxis, yAxis, fps, time):

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
    
    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = time*fps, interval = 2, blit = True) 
    anim.save('animation.gif', writer='pillow', fps=fps)

    print("Program completed")

df = pd.read_csv(r"C:\Users\Anakin\Documents\dataAnalyticsProject2026\tests\5.2 Line Graph 2 {Single}\names.csv")

animatedGraph(
    title = "Activity Level by Name",
    xLabel = "Name",
    yLabel = "Activity Level",
    xAxis = df["name"],
    yAxis = df["activityLevel"],
    fps = 30,
    time = 7,
)