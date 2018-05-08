# -*- coding: utf-8 -*-
"""
Created on Tue May  8 14:11:03 2018

@author: Dell
"""

address='addressbook.txt'
with open(address,'r') as file:
    res=file.readlines()
    #print(res)
    dic={}
    for line in res:
        dicx=line.split(',')
        #print(dicx)
        dic[dicx[0]]=dicx[1]
    #print(dic)
    name=input('Please input the name you want to find:')
    if name in dic:
        print('The info is:',name,dic[name].rstrip())
    else:
        print('Not found')