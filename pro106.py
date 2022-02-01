import csv
import plotly.express as px
import numpy as np

def getDataSource(path):
    daysPresent = []
    percentage = []

    with open("attendence.csv", newline = '') as f:
        df = csv.DictReader(f)
        '''fig = px.scatter(df, x = "Days Present", y = "Marks In Percentage")
        fig.show()'''

        for row in df:
            daysPresent.append(float(row["Days Present"]))
            percentage.append(float(row["Marks In Percentage"]))
        
    return {"x" : daysPresent, "y" : percentage}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation between Marks in percentage and days present is: ", correlation[0, 1])

def setup():
    path = "attendence.csv"
    dataSource = getDataSource(path)
    findCorrelation(dataSource)

setup()