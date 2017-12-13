import numpy as np
import matplotlib.pyplot as plt

def calculate_coef(x,y):
    #number of observation
    size_x=np.size(x);
    #find the mean of x & y
    mean_x=np.mean(x);
    mean_y=np.mean(y);

    #calculation of deviation cross deviation
    ss_xy=np.sum(y*x-size_x*mean_x*mean_y)
    ss_xx=np.sum(x*x-size_x*mean_x)

    #calculation of regression coefficient
    b_1=ss_xy/ss_xx
    b_0=mean_y-b_1*mean_x

    return (b_0,b_1)

def plot_regression_line(x,y,b):
    plt.scatter()

