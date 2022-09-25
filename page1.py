from datetime import datetime
from tracemalloc import start
import pandas
import matplotlib.pyplot as plt
import numpy as np
import sys
def q1(start_date,end_date):
    test=pandas.read_csv('data.csv')
    #get a data from data.csv
    test['OFFENCE_MONTH']=pandas.to_datetime(test['OFFENCE_MONTH'])
    #convert OFFENCE_MONTH into date format.
    start_date=datetime.strptime(start_date, '%m-%d-%Y').date()
    #convert start date into date format.
    count=0
    count1=0
    print(type(test.loc[0]['OFFENCE_MONTH']))

    #print(len(test.index)) #length of csv file?
    for x in test.index:
        if test.loc[x,"OFFENCE_MONTH"]>pandas.Timestamp(start_date):
            count+=1
    for x in test.index:
        if test.loc[x,"OFFENCE_MONTH"]>pandas.Timestamp(end_date):
            count1+=1

    print(count)
    print(count1)
    xpoints = np.array([0,6])
    ypoints = np.array([0,count])
    plt.plot(xpoints,ypoints)
    plt.show()

    #print(test.loc[0][1])
    #print(type(test.loc[0][1]))
    print(count)

q1('01-01-2012','01-01-2013')


