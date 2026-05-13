import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

import lineGraph, scatterGraph, barGraph, pieChart

def reset():
    df = pd.read_csv(r"static\python\pldbCleaned.csv")
    path = r"source\static\images"

    lineGraph.lineGraph(
        data = df["appeared"],
        path = path,
        title = "Year created",
        xTitle = "",
        yTitle = "",
    )

    scatterGraph.scatterGraph(
        data = df,
        path = path,
        xAxis = "appeared",
        yAxis = "numberOfUsers",
        title = "Correlation of popularity of a language to year created"
    )

    barGraph.barGraph(
        data = df["country"],
        path = path,
        title = "Country created",
    )

    pieChart(
        data = df["lineCommentToken"],
        path = path,
        title = "Line Comment Token",
    )