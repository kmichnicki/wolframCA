

#This program calculates cellular automata of the kind shown in the beginning of wolframs book
#Each cycle, the matrix element below the current one is determined by the neighbors of the current one.
#After a matrix of values is gotten, it is converted into another matrix that holds the color scheme for the image.

def f(x,y,z):

    if x==1 and y==1 and z==1:
        return 0
    elif x==1 and y==1 and z==0:
        return 0
    elif x==1 and y==0 and z==1:
        return 1
    elif x==1 and y==0 and z==0:
        return 1
    elif x==0 and y==1 and z==1:
        return 1
    elif x==0 and y==1 and z==0:
        return 1
    elif x==0 and y==0 and z==1:
        return 1
    elif x==0 and y==0 and z==0: # Crash if changed.
        return 0

    else:
         print "you messed up on the f function"


def appendAll(x):
    for key1 in range(len(x)):
        x[key1].append(0)
    return x

def attachAll(x):
    for key in range(len(x)):
        x[key].insert(0,0)
    return x


#x1=[1,0,1,1,1,1,0,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
x1=[1]

max=20
n=0
tempAppend=[0]
tempStart=[1]
final=[tempStart]






for key in range(max):

    if f(0,0,final[key][0]):
        final=attachAll(final)



    y=len(final[key])


    if f(final[key][y-1],0,0):
        final=appendAll(final)
    if len(final)==max:
        break

    final.append([])

    length=len(final[key])         #new length needed since it might have changed

    for bar in range(len(final[key])):
        if bar==0 and length==1:
            final[key+1][0]=f(0,final[key][0],0)
        elif bar==0 and length!=1:
            final[key+1].append(f(0,final[key][0],final[key][1]))
        elif length-1==bar:
            final[key+1].append(f(final[key][bar-1],final[key][bar],0))
        else:
            final[key+1].append(f(final[key][bar-1],final[key][bar],final[key][bar+1]))



#images are stored as
# [
#   [
#    [1,1,1],[1,1,1]
#   ]
#   ,
#   [
#    [0,0,0],[1,1,1]
#   ]
# ]
#Each 3 numbers specifies intensity of RGB
#I need to convert the matrix to this form

image=[[[]]]


for key1 in range(len(final)):


    for key2 in range(len(final[key1])):
        image[key1][key2]=[float(final[key1][key2]),float(final[key1][key2]),float(final[key1][key2])]
        if key2!=len(final[key1])-1:
            image[key1].append([])
    if key1!=len(final)-1:
        image.append([[]])


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

imgplot = plt.imshow(image)
plt.savefig('simple_plot')

