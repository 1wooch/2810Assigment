from cgitb import reset
from datetime import datetime
from itertools import count
from operator import truediv
from tracemalloc import start
import pandas
import matplotlib.pyplot as plt
import numpy as np
import sys



class draw_graph(object):
    def __init__(self,month_result):
        self.month_result=month_result
        

        
    
    def draw_bar_graph(self): #mobile phone , School Zone
        plt.figure(figsize=(20,3))
        #width:20,height:3
        plt.title('Bar Graph')
        plt.bar(range(len(self.month_result)),list(self.month_result.values()),align='center',width=0.3)
        #set width.
        plt.xticks(range(len(self.month_result)),list(self.month_result.keys()))
        plt.show()
    def draw_line_graph(self):
        plt.title('Line Graph')
        #print(self.month_result.keys())
        #print(self.month_result.values())
        labels=np.array(list(self.month_result.keys())) #month
        y=np.array(list(self.month_result.values())) #data
        plt.plot(labels,y,linestyle='-',marker='o')
        plt.show()
    def draw_2_line_graph(self): #for radar or camera
        plt.title(' radar or camera')

        labels=np.array(list(self.month_result.keys()))
        first_data=np.array(list(self.month_result.values())).astype(np.double)
        second_data=np.array([2, None, 5, None, 4, None, 3, 2]).astype(np.double)
        plt.plot(labels,first_data,linestyle='-',marker='o')
        plt.plot(labels,first_data,linestyle='-',marker='o')
        plt.show()
    def draw_pie_chart(self):
        plt.title('Top 5 most accident day')
        self.month_result=sorted(self.month_result.items(),key=lambda x:x[1],reverse=True)
        #sort the dictionary
        self.month_result=self.month_result[0:5]#list

        label_list=[]
        data_list=[]
        for i in range(len(self.month_result)):
            print(self.month_result[i])
            label_list.append(self.month_result[i][0])
            data_list.append(self.month_result[i][1])

        data=np.array(data_list)
        labels=np.array(label_list)
        plt.pie(data_list,labels=label_list)
        plt.show()



