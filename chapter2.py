import numpy as np
import time

def multTime():
    ''' Calculate the time taken to perform x*y element-wise using list comprehension. zip() helps
        us perform consecutive looping'''
    start=time.time()   #start the stopwatch
    ans = [x*y for x,y in zip(range(1000000),range(15,1000015))] #calculating the answer
    end=time.time()     #stop the stopwatch
    print(end-start)    #print the time taken


def arrayMultTime():
    ''' Calculate the time taken to perform x*y element-wise using numpy.'''
    start = time.time()
    ans = np.multiply(np.arange(1000000),np.arange(15,1000015))
    end = time.time()
    print(end-start)

print('Time taken for multTime():')
multTime()  #calling the multTime method
print('Time taken for arrayMultTime():')
arrayMultTime()  #calling the arrayMultTime method






