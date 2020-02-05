import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io

class RealestateAnalyzer:
    def __init__(self, datasource, plotx, ploty, minTrans=20):
        self.datasource = datasource
        self.plotx = plotx
        self.ploty = ploty
        self.minTrans = minTrans

    def analyze(self, row_identifier, row_value):
        df = self.create_df(self.datasource) #
        df = self.filter_df(df, row_identifier, row_value)
        return self.plot_df(df, self.plotx, self.ploty)

    def create_df(self, source):
        df = pd.read_csv(source, encoding="utf8")
        df = df[df["2018"] > self.minTrans]
        df = df[df["2017"] > self.minTrans]
        df = df[df["2016"] > self.minTrans]
        df = df[df["2015"] > self.minTrans]
        df = df[df["2014"] > self.minTrans]
        df = df[df["2013"] > self.minTrans]
        df = df[df["2012"] > self.minTrans]
        return pd.melt(df, id_vars=["Sifra", "Zupanija", "JLS"], var_name="Year", value_name="Transactions")

    def filter_df(self, df, row_identifier, row_value):
        return df.loc[df[row_identifier] == row_value,:]

    def plot_df(self, df, x, y):
        df.plot(kind='bar', y=y, x=x)
        byts = io.BytesIO()
        plt.savefig(byts, format='png')
        byts.seek(0)
        return byts