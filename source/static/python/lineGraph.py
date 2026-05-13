import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def lineGraph(data, title, xTitle, yTitle, path):
    '''line graph based on count'''
    plt.figure(figsize=(10, 6))

    titles = list(set(data))
    values = {i: list(data).count(i) for i in titles}

    plt.plot(
        values.keys(),
        values.values(),
        marker='o',
        linestyle='-',
    )

    plt.title(title)
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)

    plt.tight_layout()
    
    plt.savefig(path + r"\lineGraph.jpeg", dpi=300)
    plt.close()