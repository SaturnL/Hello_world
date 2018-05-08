 # -*- coding: utf-8 -*-
"""
Created on Tue May  8 15:30:18 2018

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


class ChinaBMI(BMI):
    '''Define subclass ChinaBMI'''
    def printBMI(self):
        mBMI=self.BMI
        if mBMI<18.5:
            rate='偏瘦'
            dang='低（但其它疾病危险性增加）'
        elif 18.5<=mBMI<23.9:
            rate='正常'
            dang='平均水平'
        elif 24<=mBMI<26.9:
            rate='偏胖'
            dang='增加'
        elif 27<=mBMI<29.9:
            rate='肥胖'
            dang='中度增加'
        elif 30<=mBMI:
            rate='重度肥胖'
            dang='严重增加'
        print('{0:.1f} 你的BMI分类是{1}，相关疾病发病的危险性是{2}。'.format(mBMI,rate,dang))

if __name__ == '__main__':
    myBMI=ChinaBMI(1.75,70)
    myBMI.printBMI()