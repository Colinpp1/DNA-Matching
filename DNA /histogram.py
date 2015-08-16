import matplotlib.pyplot as plt
import numpy
import matplotlib.mlab as mlab
from math import sqrt
import os

os.chdir(os.curdir)
f=open("human.txt","r")
value=[]
for i,line in enumerate(f):
    line=line.strip("\n")
    if line !="":
        value.append(int(line[0:5]))

f=open("neanderthal.txt","r")
value2=[]
for i,line in enumerate(f):
    line=line.strip("\n")
    if line !="":
        value2.append(int(line[0:5]))



mean=numpy.mean(value)
mean2=numpy.mean(value2)
std=numpy.std(value)
std2=numpy.std(value2)
x = numpy.linspace(82000,83000,10000)
y = numpy.linspace(80400,81400,6000)
plt.ylim(ymax=0.007)

plt.plot(x,mlab.normpdf(x,mean,std),color='black')
plt.plot(y,mlab.normpdf(y,mean2,std2),color='b')
#plt.hist(value2,bins=50,histtype='stepfilled',normed=True,color='g')
#plt.hist(value,bins=50,histtype='stepfilled',normed=True,color='r')
#plt.title("Gaussian Histogram")
#plt.xlabel("Value")
#plt.ylabel("Frequency")
plt.show()
