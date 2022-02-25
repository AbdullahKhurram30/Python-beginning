import numpy 
import statistics as stat
import matplotlib
from matplotlib import pyplot as plt


#pcw6.2: data set type 1(same range &sd, different mean)
data_set_1 = [1,3,4,5,5,6,7,8,9]
data_set_2 = [1,4,4,4,4,4,7,8,9]

#print (stat.stdev(data_set_1))
#print (stat.stdev(data_set_2))

#print(stat.mean(data_set_1))
#print(stat.mean(data_set_2))

def range(a):
    return max(a) - min(a)

#print(range(data_set_1))
#print(range(data_set_2))

#pcw6.2: data set type 2(same range &mean, different sd)
data_set_3 = [1,2,3,3,4,4,5,6,8,9]
data_set_4 = [1,1,2,3,4,5,6,6,8,9]

print(stat.stdev(data_set_3))
print(stat.stdev(data_set_4))

print(stat.mean(data_set_3))
print(stat.mean(data_set_4))

print(range(data_set_3))
print(range(data_set_4))

#pcw 6.2: data set type 3(same mean &sd, different range)
data_set_5 = [1,5,5,5,5,6,6,6,6]
data_set_6 = [3,3,4,4,5,6,6,7,7]

print(stat.stdev(data_set_5))
print(stat.stdev(data_set_6))

print(stat.mean(data_set_5))
print(stat.mean(data_set_6))

print(range(data_set_5))
print(range(data_set_6))