# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 19:04:28 2024

@author: ADMINIS
"""

import math

a= float(input("Nhap gia tri thuc cho a: "))
b= float(input("Nhap gia tri thuc cho b: "))
print("Giá trị biểu thức bằng ", ((math.sqrt(a)-math.sqrt(b))/((a**1/4)-(b**1/4)))-((math.sqrt(a)-((a*b)**1/4))/((a**1/4)+(b**1/4))))