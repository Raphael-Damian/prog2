#Raphaël Ashruf MA4
import random
import concurrent.futures as future
import math
import functools
import time
def volume(d):
    return (math.pi**(d/2))/(math.gamma(d/2 + 1))

def hyperSphere(n):
    d = 11
    vals = []
    list1 = [[random.uniform(-1,1) for i in range(d)] for j in range(n)] #used list comprehension
    for i in range(n):
        lst = list1[i] #make list of size d
        for k in range(d):
            lst[k] = (lst[k]**2) #square elements
        vals.append(functools.reduce(lambda x,y: (x+y), lst)) #used lambda and functools.reduce
    count = 0
    for x in vals:
        if x <= 1:
            count+=1
    return count
def main():
    t1_start = time.perf_counter()
    n = 1000000
    count = hyperSphere(1000000)
    d = 11
    approx = (2**d) * (count/n)
    print(approx)
    t1_stop = time.perf_counter()
    print(t1_stop - t1_start)
    t2_start = time.perf_counter()
    with future.ProcessPoolExecutor() as ex:
        p = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]
        results = ex.map(hyperSphere, p)
        count = 0
        for x in results:
            count += x
        n = 1000000
        d = 11
        approx = (2**d) * (count/n)
        print(approx)
        t2_stop = time.perf_counter()
        print(t2_stop-t2_start)
if __name__ == '__main__':
    main()