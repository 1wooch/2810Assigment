from cgitb import reset
from datetime import datetime
from itertools import count
from operator import truediv
from tracemalloc import start
import pandas
import matplotlib.pyplot as plt
import numpy as np
import sys
from draw_graph import *

class basic_function(object):
    def __init__(self,start_year,start_month,end_year,end_month,school_zone_bool):
        self.start_year = start_year
        self.start_month=start_month
        self.end_year = end_year
        self.end_month = end_month
        self.school_zone_bool = school_zone_bool
        self.range_date=[]
        self.range_date_date_format=[]
        self.month_result={}


    def get_date_range(self):
        

        #inspired from https://stackoverflow.com/questions/5734438/how-to-create-a-month-iterator

        ym_start = 12*int(self.start_year)+int(self.start_month)-1
        ym_end = 12*int(self.end_year)+int(self.end_month)+1
        for ym in range(ym_start,ym_end):
            y,m=divmod(ym,12)
            self.range_date.append([y,m+1]) #year and month 
            #type(int) -> convert into string?
        #print(self.range_date)

        for i in range(len(self.range_date)):
            year=self.range_date[i][0]
            month=self.range_date[i][1]
            year=str(year)
            month=str(month)
            date_change='01-'+month+'-'+year #type string
            date_change=datetime.strptime(date_change, '%d-%m-%Y').date()
            self.range_date_date_format.append(date_change)


    def date_and_school(self):
        result=0

        self.get_date_range()
    

        test=pandas.read_csv('data.csv')
        test['OFFENCE_MONTH']=pandas.to_datetime(test['OFFENCE_MONTH'])

       

        print(test[0:3])      
                



        test_oop=draw_graph(result,self.range_date)
        test_result=test_oop.draw_bar_graph()

        # #use for loop get each month and get count and store as dictionary
        # for x in test.index:
        #     count=0
        #     for i in range(len(self.range_date_date_format)):
        #         #print(self.range_date_date_format[i])
        #         if (test.loc[x,"OFFENCE_MONTH"]==self.range_date_date_format[i]):
        #             count+=1
        #     self.month_result[str(self.range_date_date_format[i])]=count
        # print(self.month_result)
        
        return self.range_date,result
      

start=basic_function('2012','01','2013','02',True)
test = start.date_and_school()

print (type(test))
#print(test[0]) #-> self.range_date
#print(test[1]) #-> result


#https://www.entechin.com/how-to-import-a-class-from-another-file-in-python/ -> how to use other file class in OOP