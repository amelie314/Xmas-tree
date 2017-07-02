#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 14:59:13 2017

@author: huihua
"""
#作業
text = input ('我們將獻上屬於你行數的圖形，請輸入你想要的行數：') 
key = int (text) 

head = 0
bottom = 0
sum = 0

if key >= 5:
    for x in range (1, key + 4): #X跑進迴圈,當x>=5時(且key+1包含key），後面3行放樹幹三支
        sum = " " * (key-x) + "*" * (2*x-1) + " " * (key-x)
        if x == 1:
            head = " " * (key-x) + "☾" * (2*x-1) + " " * (key-x)     
            print(head)  
        elif x >= key + 1:
            bottom = " " * (key-2) + "|" * 3 +  " " * (key-2)
            print(bottom)
        else:
            print(sum)  
else:
    for x in range (1, key + 3): #X跑進迴圈,當x<5時,key+1包含key，後面2行放樹幹一支
        sum = " " * (key-x) + "*" * (2*x-1) + " " * (key-x)
        if x == 1:
            head = " " * (key-x) + "✇" * (2*x-1) + " " * (key-x)     
            print(head)  
        elif x >= key+1:
            bottom = " " * (key-1) + "|" * 1 +  " " * (key-1)
            print(bottom)
        else:
            print(sum) 