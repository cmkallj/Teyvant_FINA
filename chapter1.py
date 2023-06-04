import AF_by_chapter1
from Cashflow import  cashflow
from datetime import datetime

def cal_period_true_rule(date):
    if isinstance(date, (int, float)):
        period = date / 365
    elif isinstance(date, list):
        date1 = datetime.strptime(date[0], "%Y-%m-%d")
        date2 = datetime.strptime(date[1], "%Y-%m-%d")
        period_time = (date2 - date1).days
        period = period_time / 365
    return period

a1 = cashflow(cash=[1],interst_rate=0.01,period=1)
m=a1.cal_FV(time= 1)
print(m)
a1 = cashflow(cash=[10],interst_rate=0.05,period=1)
m=a1.cal_FV(time=cal_period_true_rule(65))
print(m)
a1 = cashflow(cash=[1],interst_rate=0.0425,period=1)
m=a1.cal_FV(time=3)
print(m)
def a(time,benjin=1):
    a=[]

    for i in range(int(round(time))):
        a.append(benjin*(1+i**2))

    a.append(benjin*(1+time**2))
    print(a[0])
    print('本金为')
    print(a[-1])
    print("累计值为")
    print(a)
    return a
a(time=3.5,benjin=10)
def get_eff_interst_rate(m:list):
    a = []
    m=m
    m.append(0)
    i=0
    while m[i+1]!=0:
        a.append(m[i+1]/m[i]-1)
        i+=1
    print(a)
    return  a
get_eff_interst_rate([1000,1020,1050])
def get_eff_discount_rate(m:list):
    a = []
    m=m
    m.append(0)
    i=0
    while m[i+1]!=0:
        a.append(1-m[i]/m[i+1])
        i+=1
    print(a)
    return  a
get_eff_discount_rate([0.9,1.0])





from datetime import date
#时间计算函数
def calculate_days(Y1, M1, D1, Y2, M2, D2, rule):
    date1 = date(Y1, M1, D1)
    date2 = date(Y2, M2, D2)

    if rule == "actual/365":
        days = (date1 - date2).days
        return days

    elif rule == "actual/360":
        days = (date1 - date2).days
        return days

    elif rule == "30/360":
        days = 360 * (Y1 - Y2) + 30 * (M1 - M2) + (D1 - D2)
        return days

    else:
        return None

# 示例用法
Y1, M1, D1 = 2023, 4, 30
Y2, M2, D2 = 2023, 1, 1
rule = "30/360"

days = calculate_days(Y1, M1, D1, Y2, M2, D2, rule)
print("两个日期之间的天数:", days)

#单利率实际有效利率考察
eg1=[]
eg1.append(1)
for i in range(1,10+1):
    eg1.append(eg1[i-1]+eg1[0]*0.1)
get_eff_interst_rate(eg1)

#复利率实际有效利率考察
eg2=[]
eg2.append(1)
for i in range(1,10+1):
    eg2.append(eg1[i-1]+eg1[i-1]*0.1)
get_eff_interst_rate(eg2)

#名义利率与有效利率的互换
def effective_to_nominal_rate(effective_rate, period1, period2):
    nominal_rate = ((1 + effective_rate) ** (period2 / period1)) - 1
    return nominal_rate
effective_rate = 0.05
period1 = 1  # 年
period2 = 2  # 期数时间2（未提供具体数值）

nominal_rate = effective_to_nominal_rate(effective_rate, period1, period2)
print("转换后的名义利率:", nominal_rate)
def nominal_to_effective_rate(nominal_rate, period1, period2):
    effective_rate = ((1 + nominal_rate) ** (period1 / period2)) - 1
    return effective_rate
nominal_rate = 0.08
period1 = 1  # 年
period2 = 4  # 期数时间2（未提供具体数值）

effective_rate = nominal_to_effective_rate(nominal_rate, period1, period2)
print("转换后的有效利率:", effective_rate)


#名义贴现率与有效贴现率的互换

def nominal_to_effective_discount_rate(nominal_rate, period):
    effective_rate =1- (1 - nominal_rate) ** (1 / period)
    return effective_rate
def effective_to_nominal_discount_rate(effective_rate, period):
    nominal_rate = 1-(1 + effective_rate) ** (-period)
    return nominal_rate
nominal_rate = 0.1
period = 2

effective_rate = nominal_to_effective_discount_rate(nominal_rate, period)
print("转换后的有效贴现率:", effective_rate)

nominal_rate = effective_to_nominal_discount_rate(effective_rate, period)
print("转换后的名义贴现率:", nominal_rate)

import math

def calculate_interest_force(i, t):
    interest_force = math.log(i*t)/t
    return interest_force
def calculate_interest_rate(interest_force, t):
    i = math.exp(interest_force*t) / t
    return i

# 示例用法
interest_force = 0.2  # 利息力
t = 1  # 时间期间的长度

interest_rate = calculate_interest_rate(interest_force, t)

print("单利率:", interest_rate)


# 示例用法
i = 2.718  # 单利率

interest_force = calculate_interest_force(i, 1)  # 计算在一个时间期间内的利息力

print("利息力:", interest_force)
import math

m = 10  # 给定的数值

ln_m = math.log(m)  # 计算 ln m

print("ln m:", ln_m)

