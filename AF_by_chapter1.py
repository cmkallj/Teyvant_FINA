#因为我目前还没有具体做好该怎么实现对那些类，那些方法的定义，那么呢
#我也只有先把，先按着书，先把代码先跑起来再说吧，目前的初步想法是先完成从第1章到第4章的内容的编写
#然后呢，把我的程序做好可视化，接下来再继续编写剩下的内容吧
#如果暑假开始前我还没有完成这个项目，那么我就暑假的时候继续做

import  numpy
import scipy
import math
import matplotlib
import random
import pandas
import sympy
import tkinter
#计息周期，先放外边吧

finish_period=1
#嗯，算了，先就按照课本打吧，第一章的内容是，累计函数，贴现函数，各种利率，贴现，利息等
time =3
effective_rate=0.0198
is_simple_rate=False
#累计函数类， time：+real_num   effective_rate: +real_num ,is_simple_rate:bool,is_compound_rate:bool
class  one_based_af():
    def __init__(self,time,effective_rate,is_simple_rate):
        self.account=1
        self.time=time
        self.B ='tevant'
        self.effective_rate=effective_rate
        self.is_simple_rate =is_simple_rate
        self.is_compound_rate = is_compound_rate
        self.effective_rate_vary_with_time=[]

        #在整数倍计息周期内的时间所获得的利息和本金，用列表表示，在非整数周期内所得到的本金和利息，时间结束的本金和利息
        self.goodtime_rate = [0.0]
        self.goodtime_principle = [1.0]
        self.not_enough_time_rate=0
        self.not_enough_time_principle = 0
        self.all_rate=0
        self.all_principle = 0



    def __str__(self):
        print(f"时间为{time}年\n")
        print(f"整个时间的现金流为{self.goodtime_principle}，{self.all_principle}")
        print(f"整个时间利息的现金流为{self.goodtime_rate}，{self.all_rate}")
        print(f"最后的累计值为{self.all_principle}")
        print(f"获得利息为{self.all_rate}")
        print(f"有效利率为{effective_rate}")


    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass
    #计算在时间t时的以复利累计的本金和利息
    def cal_principle_and_rate_compand(self):
        numtime=int(self.time/finish_period)
        littletime = self.time-numtime
        for i in range(numtime):
            tem_rate=self.goodtime_principle[-1]* self.effective_rate
            self.goodtime_rate.append(tem_rate)
            self.goodtime_principle.append( self.goodtime_principle[-1]+tem_rate)
        self.not_enough_time_rate = self.goodtime_principle[-1]*self.effective_rate
        self.not_enough_time_principle =self.goodtime_principle[-1]+self.not_enough_time_rate
        self.all_principle =self.not_enough_time_principle
        self.all_rate =self.not_enough_time_principle-self.goodtime_principle[0]
    #计算时间t时以单利累计的本金和利息
    def cal_principle_and_rate_simple(self):
        numtime=int(self.time/finish_period)
        littletime = self.time-numtime
        for i in range(numtime):
            tem_rate=self.goodtime_principle[0]* self.effective_rate
            self.goodtime_rate.append(tem_rate)
            self.goodtime_principle.append( self.goodtime_principle[0]+tem_rate)
        self.not_enough_time_rate = self.goodtime_principle[0]*self.effective_rate
        self.not_enough_time_principle =self.goodtime_principle[0]+self.not_enough_time_rate
        self.all_principle =self.not_enough_time_principle
        self.all_rate =self.not_enough_time_principle-self.goodtime_principle[0]
        #计算有效利率
    def cal_effective_rate_vary_with_time(self):
        numtime = int(self.time / finish_period)
        for i in range(numtime):
            effective_rate_vary_with_time.append()
####时间的换算函数，同时，如何实现日后利率与时间与贴现力与利率与计息周期的强相关


#贴现函数类
class  one_based_af():
    def __init__(self,time,effective_rate,is_simple_rate):
        self.account=1
        self.time=time
        self.B ='tevant'
        self.effective_rate=effective_rate
        self.is_simple_rate =is_simple_rate
        self.is_compound_rate = is_compound_rate

        #在整数倍计息周期内的时间所获得的利息和本金，用列表表示，在非整数周期内所得到的本金和利息，时间结束的本金和利息
        self.goodtime_rate = [0.0]
        self.goodtime_principle = [1.0]
        self.not_enough_time_rate=0
        self.not_enough_time_principle = 0
        self.all_rate=0
        self.all_principle = 0



    def __str__(self):
        print(f"时间为{time}年\n")
        print(f"整个时间的现金流为{self.goodtime_principle}，{self.all_principle}")
        print(f"整个时间利息的现金流为{self.goodtime_rate}，{self.all_rate}")
        print(f"最后的累计值为{self.all_principle}")
        print(f"获得利息为{self.all_rate}")
        print(f"有效利率为{effective_rate}")


    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass
    #计算在时间t时的以复利累计的本金和利息
    def cal_principle_and_rate_compand(self):
        numtime=int(self.time/finish_period)
        littletime = self.time-numtime
        for i in range(numtime):
            tem_rate=self.goodtime_principle[-1]* self.effective_rate
            self.goodtime_rate.append(tem_rate)
            self.goodtime_principle.append( self.goodtime_principle[-1]+tem_rate)
        self.not_enough_time_rate = self.goodtime_principle[-1]*self.effective_rate
        self.not_enough_time_principle =self.goodtime_principle[-1]+self.not_enough_time_rate
        self.all_principle =self.not_enough_time_principle
        self.all_rate =self.not_enough_time_principle-self.goodtime_principle[0]
    #计算时间t时以单利累计的本金和利息
    def cal_principle_and_rate_simple(self):
        numtime=int(self.time/finish_period)
        littletime = self.time-numtime
        for i in range(numtime):
            tem_rate=self.goodtime_principle[0]* self.effective_rate
            self.goodtime_rate.append(tem_rate)
            self.goodtime_principle.append( self.goodtime_principle[0]+tem_rate)
        self.not_enough_time_rate = self.goodtime_principle[0]*self.effective_rate
        self.not_enough_time_principle =self.goodtime_principle[0]+self.not_enough_time_rate
        self.all_principle =self.not_enough_time_principle
        self.all_rate =self.not_enough_time_principle-self.goodtime_principle[0]