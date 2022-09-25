import pandas
import matplotlib.pyplot as plt
import numpy as np
import sys

test=pandas.read_csv('data.csv')
test['OFFENCE_MONTH']=pandas.to_datetime(test['OFFENCE_MONTH'])

count=0

print(len(test.index)) #length of csv file?
for x in test.index:
    if test.loc[x,"FACE_VALUE"]>300:
        count+=1

xpoints = np.array([0,6])
ypoints = np.array([0,count])
plt.plot(xpoints,ypoints)
plt.show()

#print(test.loc[0][1])
#print(type(test.loc[0][1]))
print(count)

