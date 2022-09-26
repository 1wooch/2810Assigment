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
    def __init__(self,result,range_date):
        self.result=result
        self.range_date = range_date
        
    
    def draw_bar_graph(self):
        
        return self.result,self.range_date
