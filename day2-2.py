# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:21:13 2020

@author: user
"""
while True:
    import random
    shit=random.randint(1,10)
    kk=input("1~10猜猜看:")
    shit=int(shit)
    kk=int(kk)
    if kk>0 and kk<11:
        if kk==shit:
            print("厲害喔")
        else:
            print("猜錯了")    
    else:
        print("請輸入1~10")    
