# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 00:26:18 2023

@author: DELL
"""

import pandas as pd
import matplotlib.pyplot as plt


'''
A  user defined function is created to depict the piechart ,also inserted the required data set to plot the chart.
Which is used for the furthur analysis of  provided data. 
'''


def piechart(piedata):
    data_3 = piedata # New variable is created to store the dataset.

    print(data_3) # prints the specified dataset for plotting pie chart
    plt.pie(data_3["2017"], labels=data_3["COUNTRY"], autopct="%1.1f%%")
    # plot title
    plt.title('MOBILE SUBSCRIPTION RATE PER 100 PERSON IN THE YEAR OF 2017')
    plt.savefig("Pieplot.png")
 
    # function to show the plot
    plt.show()
    return # A return statement is used to end the execution of the function call 

if __name__ == "__main__":
    #To read the data in excel format for linechart
    data_3 = pd.read_excel("Mobile_sub.xlsx")
    #Here is the function for calling lineplot
    piechart(data_3)
