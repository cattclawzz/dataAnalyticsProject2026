# Line Graph 2
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\Anakin\Documents\dataAnalyticsProject2026\tests\5.2 Line Graph 2 {Single}\names.csv")

def nameActivityLevelChart(df):
    plt.figure(figsize=(10, 6))
    
    plt.plot(
        df['name'],
        df['activityLevel'],
        marker='o',
        linestyle='-',
        label='Activity Level'
    )
    
    # Labels and Theme
    plt.title("Activity Level by Name")
    plt.xlabel("Name")
    plt.ylabel("Activity Level")
    plt.legend()
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.tight_layout()       # Prevents label cutoff
    
    plt.show()

nameActivityLevelChart(df)