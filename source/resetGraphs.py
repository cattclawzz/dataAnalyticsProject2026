import pandas as pd

from static.python.lineGraph import *
from static.python.scatterGraph import *
from static.python.barGraph import *
from static.python.pieChart import *

def reset():
    df = pd.read_csv(r"static\python\pldbCleaned.csv")
    path = r"static\images"

    lineGraph(
        data = df["appeared"],
        path = path,
        title = "Year created",
        xTitle = "",
        yTitle = "",
    )

    scatterGraph(
        data = df,
        path = path,
        xAxis = "appeared",
        yAxis = "numberOfUsers",
        title = "Correlation of popularity of a language to year created"
    )

    barGraph(
        data = df["country"],
        path = path,
        title = "Country created",
    )

    pieChart(
        data = df["lineCommentToken"],
        path = path,
        title = "Line Comment Token",
    )