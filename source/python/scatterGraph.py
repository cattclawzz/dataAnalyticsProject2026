import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def scatterGraph(data, xAxis, yAxis, title, path, xTitle = "", yTitle = ""):

    corr = data[xAxis].corr(data[yAxis])

    plt.figure(figsize=(10, 6))
    plt.scatter(
        data[xAxis],
        data[yAxis],
        s=50,
        alpha=0.6
    )

    plt.title(f"{title} (r = {round(corr, 2)})")
    plt.xlabel(xTitle if xTitle else xAxis)
    plt.ylabel(yTitle if yTitle else yAxis)
    plt.tight_layout()

    plt.savefig(path + r"\scatterGraph.jpeg", dpi=300)
    plt.close()