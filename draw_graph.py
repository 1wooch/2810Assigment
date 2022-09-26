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
        print(type(self.month_result))
        plt.bar(range(len(self.month_result)),list(self.month_result.values()),align='center')
        plt.xticks(range(len(self.month_result)),list(self.month_result.keys()))
        plt.show()

