from  statistics import mean,stdev
from fractions import Fraction as fr
import sys


data1 = (11, 3, 4, 5, 7, 9, 2)
#data2 = (-1, -2, -4, -7, -12, -19) 
#data3 = (-1, -13, -6, 4, 5, 19, 9) 
#data4 = (fr(1, 2), fr(44, 12), fr(10, 3), fr(2, 3)) 
#data5 = {1:"one", 2:"two", 3:"three"}

print("Mean of data set 1 is % s" % (mean(data1))) 
#print("Mean of data set 2 is % s" % (mean(data2))) 
#print("Mean of data set 3 is % s" % (mean(data3))) 
#print("Mean of data set 4 is % s" % (mean(data4))) 
#print("Mean of data set 5 is % s" % (mean(data5))) 

sample = [1, 2, 3, 4, 5] 
print("Standard Deviation of set 1 is % s "% (stdev(data1))) 



