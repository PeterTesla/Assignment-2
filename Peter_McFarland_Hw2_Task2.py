import numpy as np
import math as m
import matplotlib.pyplot as plt

"""
Make sure you make this module as modular as you can.
That is add as many functions as you can.
1) Have a main function
2) A function to capture user input, this could be inside your "main" function
3) A function to calculate the projectile motion
4) A function to display the graph

Make sure you use docstring to document your module and all
your functions.

Make sure your python module works in dual-mode: by itself or import to other module
"""
# NOTE: You may need to run: $ pip install matplotlib

# Function to calculate projectile motion
def px(x,v,t,a):
    return x + v*t + 0.5*a*t**2

# Function to plot data
def plot_data():
    pass

# "Main" Function
def main():
     

    x0 =  int(input("Please INput Initial X Position: "))
    vx0 = int(input("Please Input Vx Initial: " ))

    y0 = int(input("Please Input Initial Y Position: ")) 
    vy0 = int(input("Please input Vy Initial: ")) 

    ax = 0.0
    ay = -9.8           # define a constant

    delt = 0.1
    t = 0.0

   
    x = []
    y = []

    interval = 170

    for i in range(interval):
       
        if px(y0,vy0,t,ay) < 0.0:
            y.append(0)
            x.append(px(x0,vx0,(-vy0-m.sqrt(vy0**2 - 2*ay*(y0)))/(ay), ax))
            break

        x.append(px(x0,vx0,t,ax))
        y.append(px(y0,vy0,t,ay))
       
        t = t + delt


    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()
    
