from flask import Flask, render_template, request
import pandas as pd
from matplotlib import use; use('Agg') #macOS bug fix
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) 

def index():
    return render_template(
        "index.html",
        foo = "test"
    )

#!!flask server!!
if __name__ == "__main__":
    app.run(debug=True)
