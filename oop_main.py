from calendar import month
from cgitb import reset
from datetime import datetime
from itertools import count
from operator import truediv
from tracemalloc import start
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys
from draw_graph import *
import re


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
            date_change=datetime.strptime(date_change, '%d-%m-%Y').strftime('%d/%m/%Y')
            self.range_date_date_format.append(date_change)


    def date_and_school(self):
        result=0

        self.get_date_range()



        data=pandas.read_csv('data.csv')
        data['OFFENCE_MONTH']=pandas.to_datetime(data['OFFENCE_MONTH'])

        data=pd.DataFrame(data)
        #print(data[data["OFFENCE_MONTH"]==self.range_date_date_format[0]].count())
        if self.school_zone_bool==True:
            for i in range(len(self.range_date_date_format)):
                month=self.range_date_date_format[i]
                count=pd.DataFrame(data[(data['OFFENCE_MONTH']==self.range_date_date_format[i])&(data['SCHOOL_ZONE_IND']=='Y')]).count()['OFFENCE_MONTH']
                self.month_result[self.range_date_date_format[i]]=count
        else:
            for i in range(len(self.range_date_date_format)):
                month=self.range_date_date_format[i]
                count=pd.DataFrame(data[data['OFFENCE_MONTH']==self.range_date_date_format[i]]).count()['OFFENCE_MONTH']
                self.month_result[self.range_date_date_format[i]]=count
        
        #sort the dictionary

        test_oop=draw_graph(self.month_result)
        bar_graph=test_oop.draw_bar_graph()
        line_graph=test_oop.draw_line_graph()
        double_line_graph=test_oop.draw_2_line_graph()
        pie_chart=test_oop.draw_pie_chart()
    def camera_or_radar(self):
        result=0
        camera_result={} #SPEED_CAMERA_IND #Camera recorded in block D
        radar_result={} #'Radar' -- section h=='Y'
        self.get_date_range()
    

        data=pandas.read_csv('data.csv')
        data['OFFENCE_MONTH']=pandas.to_datetime(data['OFFENCE_MONTH'])
        data=pd.DataFrame(data)

        

        #Camera found
        #------------------------------------------------------------------------------------------------------------------------
        if self.school_zone_bool==True:
            for i in range(len(self.range_date_date_format)):
                month=self.range_date_date_format[i]
                count=pd.DataFrame(data[(data['OFFENCE_MONTH']==self.range_date_date_format[i])&(data['SCHOOL_ZONE_IND']=='Y')&(data['CAMERA_IND']=='Y')]).count()['OFFENCE_MONTH']
                camera_result[self.range_date_date_format[i]]=count
        else:
            for i in range(len(self.range_date_date_format)):
                month=self.range_date_date_format[i]
                count=pd.DataFrame(data[(data['OFFENCE_MONTH']==self.range_date_date_format[i])&(data['CAMERA_IND']=='Y')]).count()['OFFENCE_MONTH']
                camera_result[self.range_date_date_format[i]]=count
        #-------------------------------------------------------------------------------------------------------------------------
        # Radar found
        #-------------------------------------------------------------------------------------------------------------------------
        if self.school_zone_bool==True:
            count=0
            for i in range(len(self.range_date_date_format)):
                month=self.range_date_date_format[i]
                basic_data=pd.DataFrame(data[(data['OFFENCE_MONTH']==self.range_date_date_format[i])&(data['SCHOOL_ZONE_IND']=='Y')])
                for j in range(len(basic_data)):
                    #print(test1['OFFENCE_DESC'].iloc[j])  
                    if(re.search("Radar$",str(basic_data['OFFENCE_DESC'].iloc[j]))):
                        count+=1
                radar_result[self.range_date_date_format[i]]=count
        else:
            count=0
            for i in range(len(self.range_date_date_format)):
                month=self.range_date_date_format[i]
                basic_data=pd.DataFrame(data[(data['OFFENCE_MONTH']==self.range_date_date_format[i])])
                for j in range(len(basic_data)):
                    #print(test1['OFFENCE_DESC'].iloc[j])  
                    if(re.search("Radar$",str(basic_data['OFFENCE_DESC'].iloc[j]))):
                        count+=1
                radar_result[self.range_date_date_format[i]]=count
        #print(radar_result)
        #print(camera_result)
        #-------------------------------------------------------------------------------------------------------------------------
        test_oop=draw_graph(self.month_result)
        double_line_graph=test_oop.draw_2_line_graph(radar_result,camera_result)

start=basic_function('2012','01','2013','02',True)
test = start.camera_or_radar()

#https://www.entechin.com/how-to-import-a-class-from-another-file-in-python/ -> how to use other file class in OOP