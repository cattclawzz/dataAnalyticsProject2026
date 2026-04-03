import matplotlib.animation as animation 
import matplotlib.pyplot as plt
from celluloid import Camera
import pandas as pd

df = pd.read_csv(r"C:\Users\Anakin\Documents\dataAnalyticsProject2026\tests\5.2 Line Graph 2 {Single}\names.csv")

fig = plt.figure(figsize=(10, 6)) 
axis = plt.axes(xlim =(0, 6.5), ylim =(0, 8.5)) 

plt.plot(
    df['name'],
    df['activityLevel'],
    marker = 'o',
    linestyle = '-',
    label = 'Activity Level'
)

line, = axis.plot([], [], lw = 2) 

# Labels and Theme
plt.title("Activity Level by Name")
plt.xlabel("Name")
plt.ylabel("Activity Level")
plt.legend()
plt.xticks(rotation=45)  # Rotate x-axis labels for readability
plt.tight_layout()       # Prevents label cutoff
 
def init(): 
    line.set_data([], []) 
    return line, 
 
xdata, ydata = [], [] 
 
def animate(i): 

    lst = [1,1,7,5,8,7,3]

    t = i // 30

    x = t
    y = lst[t]
     
    xdata.append(x) 
    ydata.append(y) 
    line.set_data(xdata, ydata) 
    
    return line,
   
anim = animation.FuncAnimation(fig, animate, init_func = init, frames = 7*30, interval = 20, blit = True) 
anim.save('animation.gif', writer='Pillow', fps=30)

print("Program completed")