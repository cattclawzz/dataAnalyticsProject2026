from flask import Flask, render_template
import testingtestingonetwothree as test
import matplotlib.pyplot as plt
import pandas as pd
import python.resetGraphs as resetGraphs

app = Flask(__name__)

@app.route("/") 

def index():
    foo = test.helloWorld()
    return render_template(
        "index.html",
        foo = foo
    )

resetGraphs.reset()

#!!flask server!!
if __name__ == "__main__":
    app.run(debug=True)
