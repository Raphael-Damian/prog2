#Raphaël Ashruf MA4
import random
import math
import functools
def volume(d):
    return (math.pi**(d/2))/(math.gamma(d/2 + 1))
def main():
    n = input('n is:\n')
    d = input('d is:\n')
    n = int(n)
    d = int(d)
    vals = []
    list1 = [[random.uniform(-1,1) for i in range(d)] for j in range(n)] #used list comprehension
    for i in range(n):
        lst = list1[i] #make list of size d
        for k in range(d):
            lst[k] = (lst[k]**2) #square list
        vals.append(functools.reduce(lambda x,y: (x+y), lst)) #used lambda and functools.reduce: add elements
    count = 0
    for x in vals:
        if x <= 1:
            count+=1 #if they are less than one: inside circle
    approx = (2**d) * (count/n)
    print('approx: ', approx)
    print('actual volume: ', volume(d))
if __name__ == '__main__':
    main()