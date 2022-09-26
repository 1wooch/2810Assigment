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
        
        
    
    def draw_bar_graph(self):
        plt.figure(figsize=(20,3))
        #width:20,height:3
        plt.bar(range(len(self.month_result)),list(self.month_result.values()),align='center',width=0.3)
        #set width.
        plt.xticks(range(len(self.month_result)),list(self.month_result.keys()))
        plt.show()
    def draw_line_graph(self):
        print(self.month_result.keys())
        print(self.month_result.values())


