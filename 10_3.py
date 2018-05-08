# -*- coding: utf-8 -*-
"""
Created on Tue May  8 14:48:45 2018

@author: Dell
"""

addr='subtitles.srt'
with open(addr) as file:
    res=file.readlines()
    #print(res)
    n=len(res)
    new=[]
    for i in range(n):
        if (i+1)%3==0:
            new.append(res[i])
    new=''.join(new)
    with open('subtitles.txt','w') as files:
        files.write(new)