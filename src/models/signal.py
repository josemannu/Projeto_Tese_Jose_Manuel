import pandas as pd


class signal():
    mainDf: pd.DataFrame

    def fillRows(self):
        df = pd.read_csv(r'data\raw\sinaisExemplo.xlsx', delimiter=";")
        mainDf = df
