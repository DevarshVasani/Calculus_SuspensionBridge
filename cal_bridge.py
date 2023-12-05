
import numpy as np
from scipy.integrate import quad
import math


def tension_cable(alpha, base):
    points = []

    length = mid*float(2)

    x_cab_list = list(x_cab)
    y_cab_list = list(y_cab)
    ten_points = []
    for i in range(0, len(x_cab_list)):
        true_x = abs(mid - int(x_cab_list[i]))
        true_y = abs(height_for_ten-base)
        base_ten = (float(alpha)*(length*length))/(4*true_y)

        
    
        cal1 = (base_ten*base_ten) + (float(alpha)*float(alpha)*true_x*true_x)
        cal2 = math.sqrt(cal1)
        
        ten_points.append(round(cal2, 2))
    return ten_points


   
def parabol(lenght, height, base):
    global mid, x_cab, y_cab, height_for_ten
    height_for_ten = height
    mid = lenght/2

    cal1 = height - base
    cal2 = (lenght/2)*(lenght/2)
    cal3 = cal1/cal2
    x = np.linspace(0, lenght, 100, endpoint=True)
    y= cal3*((x-mid)*(x-mid)) + base

    x_cab = np.linspace(0, lenght, round(lenght/10), endpoint=True)
    y_cab= cal3*((x_cab-mid)*(x_cab-mid)) + base

    return x, y, x_cab, y_cab

def f(x):
    global int_l

    int_l = l
    int_h = h
    int_y = y
    
    cal1 = (int_y*int_h*int_h*4)/(int_l*int_l)

    cal2= cal1*(x*2) + 1

    cal3 = math.sqrt(cal2)

    return cal3




def length_cable(l_c, h_c, y_c):
    global l, h, y, alp
    l = l_c
    h=h_c
    y = y_c
    
    result = quad(f, l_c, 0)
    list_res = list(result)
    return round(list_res[1] - list_res[0], 2)
