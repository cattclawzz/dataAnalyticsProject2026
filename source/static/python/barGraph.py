import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def barGraph(data, title, path):
    '''bar graph based on count'''
    plt.figure(figsize=(10, 6))

    titles = list(set(data))
    bars = {i: list(data).count(i) for i in titles}

    plt.bar(
        bars.keys(),
        bars.values(),
    )

    plt.title(title)

    plt.xticks(rotation=90)
    plt.tight_layout()
    
    plt.savefig(path + r"\barGraph.jpeg", dpi=300)
    plt.close()