# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 15:58:19 2019

@author: 13674
"""

class Diff:
    def __init__(self,a,b,f,n):
        self.a=a
        self.b=b
        self.f=f
        self.n=n
class Simpson(Diff):
    def __call__(self,x):
        re=0
        h=(self.b-self.a)/(self.n-1)
        w=[0 for i in range(self.n)]
        w[self.n-1]=h/6
        w[0]=h/6
        for i in range(1,self.n-1):
            if int(i/2)==i/2:
                w[i]=h/3
            else:
                w[i]=2*h/3
        for j in range(self.n):
            re+=w[j]*self.f(self.a+i*self.h)
                        