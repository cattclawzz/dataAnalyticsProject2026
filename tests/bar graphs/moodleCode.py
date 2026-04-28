import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\Anakin\Documents\dataAnalyticsProject2026\tests\bar graphs\pldb.csv")

#title = "[Title]", time = 3, fps = 12
def barGraph(data, xTitle, yTitle, title):
    '''bar graph based on count'''
    plt.figure(figsize=(10, 6))

    titles = list(set(data))
    values = {i: list(data).count(i) for i in titles}

    bars = {k: v for k, v in values.items() if v >= 20 and v< 1000} #pl is an outlier
    bars["other"] = sum([i for i in values.values() if i < 20])

    print(bars)

    plt.bar(
        bars.keys(),
        bars.values(),
        color="skyblue",
    )

    plt.title(title)
    plt.xlabel(xTitle)
    plt.ylabel(yTitle)

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

barGraph(
    data = df["type"],
    title = "Title",
    xTitle = "xAxis",
    yTitle = "yAxis",
)

'''

when I first generated the graph, the largest bar was "pl" -- likely standing for programming language.
I removed it due to it's signifigantly larger mass disrupting the graph's overall readabity.
However, it is important to consider the reason behind it, being that... [write more just remember to add this note]

'''