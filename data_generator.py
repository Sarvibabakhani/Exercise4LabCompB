import numpy as np
import matplotlib.pyplot as plt
def Show_data(x,L,s="data"):
    plt.plot(np.arange(L),x[0])
    plt.plot(np.arange(L,2*L),x[1])
    plt.plot(np.arange(2*L,3*L),x[2])
    plt.title(s)
    plt.xlabel("time")
    plt.show()




def pattern(i,z,a):
    return int(a*np.sin((np.pi*i)/z))
    # random seed for reproducibility
    
def data_generator(s,n):
    np.random.seed(12300+s)
    N=n+300  #300 always will be remained as a test set
    Z=12
    A=500
    L=60
    DX = 50
    bias = 5
    y = [0] * N
    x = [[0] * L for i in range(N)]
    for i in range(N):
        if i>0:
            x[i][0] = x[i-1][-1] + int(np.random.normal(bias,DX))
        		
        for j in range(1,L):
            x[i][j] = x[i][j-1] + int(np.random.normal(bias,DX))
			
            y[i] = i%3
  		
        if y[i]>0:
            j0 = np.random.randint(0,L-1-Z)
            sign = 3-2*y[i]
            for j in range(Z):
                x[i][j0+j] += sign*pattern(j,Z,A)
    return np.array(x), np.array(y)
	
    



