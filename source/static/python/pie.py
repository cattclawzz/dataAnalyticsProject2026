import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\Anakin\Documents\dataAnalyticsProject2026\source\static\python\pldb.csv")

def pieChart(data, title):
    data = data.dropna()

    titles = list(set(data))
    values = {i: list(data).count(i) for i in titles if list(data).count(i)}

    slices = {k: v for k, v in values.items() if v >= 10}
    slices["other"] = sum([i for i in values.values() if i < 5])

    print(slices)

    plt.figure(figsize=(10, 6))

    plt.pie(
        slices.values(),
        labels= slices.keys(),
        autopct="%.1f%%",
    )

    plt.title(title)
    plt.tight_layout()
    
    plt.savefig(r"C:\Users\Anakin\Documents\dataAnalyticsProject2026\source\static\images\pie.jpeg", dpi=300)

pieChart(
    data = df["lineCommentToken"],
    title = "Line Comment Token",
)