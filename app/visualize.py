import mysql.connector
from config import Config
import matplotlib.pyplot as plt
import pandas as pd

class Plot:
    def __init__(self):
        self.name = "Plots"

    def plot_tweets(self, hashtag):
        config = Config.config
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        df = pd.read_sql(('SELECT tweet_type FROM tweets WHERE tweet_hashtag=%(h)s'), params={"h":hashtag}, con=connection)
        return df.apply(pd.value_counts).plot.pie(subplots=True)
