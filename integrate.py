'''
Integrate.py 

Uses the trapezium rule to integrate a given function, defined before the
program runs.
'''

# - - - Import Statements - - -

import numpy as np

# - - - Global Variables - - -

BINS = 100 # the number of bins to use in the integration
START = 0 # value to integrate from
END = 50 # value to integrate to

# - - - Function Definitions - - -

def func(x):
    '''
    The function to be integrated, best to define using numpy routines.
    
    Args:
    x (float): the input variable
    
    Returns:
    y (float): value of the function when evaluated for x
    '''
    y = 3*x**2 + 5*x + 7 # Define the function here
    return y

def trapezium(a,b,h):
    '''
    Calculates the area of a trapezium of parallel side lengths a,b, and 
    'height' h. NB: in the context of the trapezium method of integration, 
    height is actually the width.
    
    Important: negative areas ARE possible here - this is due to the context
    of integration.
    
    Args:
    a (float): the length of one parallel side
    b (float): the length of the other parallel side
    h (float): the height (not always height) of the trapezium
    
    Returns:
    area (float): the area of the trapezium
    '''
    return h*(a+b)/2

def integrate(f,start,end,bins):
    '''
    Integrates the given function using the trapezium rule from start to finish
    over 'bins' trapezia.
    
    Args:
    f (func): function to be integrated
    start (float): value to integrate from
    end (float): value to integrate to
    bins (int): number of trapezia to use
    
    Returns:
    area (float): estimated area under the curve
    '''
    area = 0
    edges = np.linspace(start,end,bins)
    bin_width = (end - start)/bins
    for i in range(len(edges)-1):
        y1 = func(edges[i])
        y2 = func(edges[i+1])
        trp_area = trapezium(y1,y2,bin_width)
        area += trp_area
    return area

# - - - Main Code - - -

area = integrate(func,START,END,BINS)
print(f"Area under curve = {area:.3g}.")
