import  numpy
import scipy
import math
import matplotlib
import random
import pandas
import sympy
import tkinter
#现金流的定义
class cashflow:
    def __init__(self,cash:list,period=1,interst_rate=0):
        self.cashflow=cash
        self.period =period
        self.interst_rate=interst_rate
        self.d =None
        self.v =None

        #return  self.cashflow


    def __str__(self):
        print(self.cashflow)
        print("计息周期是")
        return " ".join(map(str, self.cashflow))

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass
    def set_period(self,period):
        self.period=period
    def  set_interst_rate(self,interst_rate):
        self.interst_rate = interst_rate
    def  cal_FV(self,time):#计算累计值
        fv=[]
        fv.append(self.cashflow[0])
        m = [0]* int(round(time))
        self.cashflow+=m
        if isinstance(time, (int)):
            for i in range(1,time+1):
                fv.append(self.cashflow[i]+fv[i-1]*(1+self.interst_rate))
        if isinstance(time, (float)) and time<1:
            fv.append(self.cashflow[-1]*(1+self.interst_rate*time))

        return  fv
    def cal_d_and_v_andmom(self):
        if  not self.d:
            self.d = self.interst_rate/(1.0+self.interst_rate)
        if not  self.v:
            self.v  = 1/(1.0+self.interst_rate)
    def cal_AV(self,time):
        self.cal_d_and_v_andmom()
        av = []
        av.append(0)
        last = -len(self.cashflow)+time-1
        av[0] = self.cashflow[last]

        for i in range(1,time):
            av.append(self.cashflow[last-i] * self.v+av[i-1])
        return av




#累计函数
class  chapter1at(cashflow):
    def __init__(self,time,base=1):
        av= []
        av.append(base)
        for i in range(1,time+1):
            av.append(1+i**2)
        super().__init__(cash=av)

class no_out_and_in_cashflow(cashflow):
    def __init__(self, cash: list, period=1,):
        self.cashflow = cash
        self.period = period
        self.interst_rate = None
        self.d = None
        self.v = None

