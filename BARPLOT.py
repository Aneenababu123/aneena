# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 00:14:11 2023

@author: DELL
"""
import pandas as pd
import matplotlib.pyplot as plt


'''
A user defined function is created to depicts the bar plot ,also inserted the required data set to plot the chart.
Which is used for the furthur analysis of  provided data. 
'''

def barchart(bardata):
    data_2 = bardata # New variable is created to store the dataset.
    print(data_2) # prints the specified dataset for plotting bar chart

# Set labels for x and y axis
    plt.figure()
    plt.bar(data_2["COUNTRY"], data_2["FEMALE"], label="FEMALE")
    plt.bar(data_2["COUNTRY"], data_2["MALE"], label="MALE")
    plt.title("CAUSE OF DEATH BY INJURY IN THE YEAR 2018") # Shows the title of chart
    plt.xlabel("Country") # for x axis
    plt.ylabel("Death Rate") # for y axis
    plt.savefig("barplot.png") # Saving the figure with png file extension
    plt.legend()
    plt.show()
    return # A return statement is used to end the execution of the function call 

if __name__ == "__main__":
    #To read the data in excel format for barchart
    data_2 = pd.read_excel("death.xlsx")
    #Here is the function for calling barchart
    barchart(data_2)