# -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:02:19 2018

@author: Dell
"""

class BMI:
    '''Define "Body Mass Index" class'''
    def __init__(self,height,weight):
        self.height=height
        self.weight=weight
        self.BMI=weight/(height**2)
    def printBMI(self):
        print('{0:.1f}'.format(self.BMI))
        
if __name__ == '__main__':
    myBMI=BMI(1.75,70)
    myBMI.printBMI()