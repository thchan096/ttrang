# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:25:44 2024

@author: Student
"""

import math

x = int(input("Nhập vào số nguyên dương có 2 chữ số = "))
if 10 <= x and x <= 99:
    a = x//10
    b = x%10
    print("Tổng các chữ số: ",a+b)
else:
    print("Không xác định")
    