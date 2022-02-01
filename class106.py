import csv
import plotly.express as px
import numpy as np

def getDataSource(path):
    coffee = []
    sleep = []

    with open("coffee.csv", newline = '') as f:
        df = csv.DictReader(f)
        '''fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
        fig.show()'''

        for row in df:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
        
    return {"x" : coffee, "y" : sleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between coffee and sleep is: ", correlation[0, 1])

def setup():
    path = "coffee.csv"
    dataSource = getDataSource(path)
    findCorrelation(dataSource)

setup()