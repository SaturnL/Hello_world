# -*- coding: utf-8 -*-
"""
Created on Tue May  8 14:29:08 2018

@author: Dell
"""

addr='file1.txt'
with open(addr,'r') as file:
    res=file.read()
    res=res+'0'
    #print(res)
    n=len(res)
    i=0
    cnt=0
    lst=[]
    while i<n-1:
        if res[i]==res[i+1]:
            cnt+=1
            i+=1
            #print(res[i])
        else:
            lst.append(res[i])
            lst.append(cnt+1)
            cnt=0
            i+=1
    #print(lst)
    lst=[str(i) for i in lst]
    with open('file2.txt','w') as doc:
        k=''.join(lst)
        doc.write(k)
    