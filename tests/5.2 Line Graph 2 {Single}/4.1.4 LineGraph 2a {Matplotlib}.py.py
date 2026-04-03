# Line Graph 2
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\Anakin\Documents\dataAnalyticsProject2026\tests\5.2 Line Graph 2 {Single}\names.csv")

def nameActivityLevelChart(df):
    # Create figure - plt.figure() creates a new chart canvas
    plt.figure(figsize=(10, 6))
    
    # Plot data - plt.plot() is a function that adds data to the canvas
    # marker='o' shows dots, linestyle='-' connects them with lines
    plt.plot(df['name'],           # x-axis column data
             df['activityLevel'],   # y-axis column data
             marker='o',            # markers shows dots
             linestyle='-',         # linestyle connects the points with lines
             label='Activity Level')
    
    # Labels and Theme
    plt.title("Activity Level by Name")
    plt.xlabel("Name")
    plt.ylabel("Activity Level")
    plt.legend()
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.tight_layout()       # Prevents label cutoff
    
    plt.show()  # Display the chart

nameActivityLevelChart(df)  # Call function with df