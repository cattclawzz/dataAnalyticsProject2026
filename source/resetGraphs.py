import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('Agg')

def lineGraph(data, title, xTitle, yTitle):
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
    
    plt.savefig(r"static\images\lineChart.jpeg", dpi=300)
    plt.close()

def scatter(data, xAxis, yAxis, title, xTitle = "", yTitle = ""):

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

    plt.savefig(r"static\images\scatter.jpeg", dpi=300)
    plt.close()

def barGraph(data, title):
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
    
    plt.savefig(r"static\images\barChart.jpeg", dpi=300)
    plt.close()

def pieChart(data, title):
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
    
    plt.savefig(r"static\images\pie.jpeg", dpi=300)
    plt.close()

def reset():
    df = pd.read_csv(r"static\python\pldbCleaned.csv")

    lineGraph(
        data = df["appeared"],
        title = "Year created",
        xTitle = "",
        yTitle = "",
    )

    scatter(
        data = df,
        xAxis = "appeared",
        yAxis = "numberOfUsers",
        title = "Correlation of popularity of a language to year created"
    )

    barGraph(
        data = df["country"],
        title = "Country created",
    )

    pieChart(
        data = df["lineCommentToken"],
        title = "Line Comment Token",
    )