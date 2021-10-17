#Raphaël Ashruf MA4
import random
import matplotlib.pyplot as plt
import numpy as np

def main():
    n = input('Give n\n')
    n = int(n)
    list = [[0 for i in range(2)] for j in range(n)] #initialize list with all zeroes
    for x in range(n):
        list[x][0] = random.uniform(-1,1) #first column: x coords
        list[x][1] = random.uniform(-1,1) #second column: y coords
    b = np.array(list)
    blue_list = np.zeros([n,2])
    red_list = np.zeros([n,2])
    countBlue = 0
    for x in range(n):
        if (b[x][0]**2) + (b[x][1]**2) > 1:
            blue_list[x][0] = b[x][0]
            blue_list[x][1] = b[x][1]
            countBlue+=1
        else:
            red_list[x][0] = b[x][0]
            red_list[x][1] = b[x][1]  
    pi = 4.0 * (1-(countBlue/n))
    plt.scatter(blue_list[:,0],blue_list[:,1], color = 'blue') #print blue points
    plt.scatter(red_list[:,0],red_list[:,1], color = 'red') #print red points
    plt.savefig(f'NumberofPoints_{n}.png')
    plt.close()
    print('PI =',pi)
    
if __name__ == '__main__':
    main()