#!/usr/bin/env python3

import sys

def tax(x):
    y=int(x)-3500
    if y<0:
        z=0
    elif y<=1500 and y>=0:
        z=y*3/100-0
    elif y>1500 and y<=4500:
        z=y*10/100-105
    elif y>4500 and y<=9000:
        z=y*20/100-555
    elif y>9000 and y<=35000:
        z=y*25/100-1005
    elif y>35000 and y<=55000:
        z=y*30/100-2755
    elif y>55000 and y<=80000:
        z=y*35/100-5505
    elif y>80000:
        z=y*45/100-13505
    else:
        print("out of range")
    print(format(z,'.2f'))

try:
    x=sys.argv[1]
    int(x)
    tax(x)
except ValueError:
    print("Parameter Error")
