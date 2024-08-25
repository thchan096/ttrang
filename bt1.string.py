# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:32:07 2024

@author: ADMINIS
"""

cau = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
print(cau.split(","))
c1 = cau.replace("P.","").replace("Q.","").replace("Tp.","")
print(c1.split(","))