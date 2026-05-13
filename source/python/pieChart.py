import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

def pieChart(data, title, path):
    data = data.dropna()

    titles = list(set(data))
    values = {i: list(data).count(i) for i in titles if list(data).count(i)}

    slices = {k: v for k, v in values.items() if v >= 10}
    slices["other"] = sum([i for i in values.values() if i < 5])

    plt.figure(figsize=(10, 6))

    plt.pie(
        slices.values(),
        labels= slices.keys(),
        autopct="%.1f%%",
    )

    plt.title(title)
    plt.tight_layout()
    
    plt.savefig(path + r"\pieChart.jpeg", dpi=300)
    plt.close()