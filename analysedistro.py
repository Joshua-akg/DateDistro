#import csv and seaborn
import csv
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pprint
import json

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

# #read csv file called 'datedistro.csv'
def main():
    #set up seaborn
    sns.set_theme()
    df = pd.read_csv('datedistro.csv')

    #print third column
    # print(df.iloc[:, 2])

    # remove the first row
    df = df.iloc[1:]

    print(df.iloc[1286,0])
    print(df.iloc[1474,0])
    print()
    print(df.iloc[940,0])
    print(df.iloc[1031,0])
    print()
    print(df.iloc[370,0])
    print(df.iloc[568,0])

    # create a new list
    julian_dates = []
    # set new list to the first column
    julian_dates = df.iloc[:, 0]

    #convert julian dates to dates
    dates = pd.to_datetime(julian_dates, unit='D', origin='julian')

    # print(dates[0])
    #print the first julian date
    # print(julian_dates[0])

    print("printing dates")
    print(dates[1293])
    print(dates[1474])
    print()
    print(dates[940])
    print(dates[1031])
    print()
    print(dates[370])
    print(dates[568])

    plot_date(df)

    #sort by the third column, print top 15 rows
    # df = df.sort_values(by=[df.columns[2]], ascending=False)
    # print(df.head(15))

def plot_date(df):
    # label the x and y-axis
    plt.xlabel('Date Index')
    plt.ylabel('Percentage Distribution')

    #plot the third column
    sns.lineplot(data=df.iloc[:, 2])
    plt.show()


if __name__ == "__main__":
    main()
