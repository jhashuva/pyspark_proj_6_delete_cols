import pandas as pd
from data_man import df1

def write_data():
    pdf = df1.toPandas()
    pdf.to_csv("Data/df1.csv")