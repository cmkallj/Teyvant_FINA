from Cashflow import  cashflow
from datetime import datetime
import AF_by_chapter1
import  chapter1
#年金的定义
#1期数有限，不非每年支付m次的，也不是连续支付的好年金
def good_annuity(benji,time,isdue=True,isdelay=0):#本金，期数，期初付期末付 ，延期多久
    flow=[]
    if not isdue:
        flow.append(0)
    while isdelay !=0:
        flow.append(0)
        isdelay-=1
    for i in range(time):
        flow.append(benji)
    print("该年金的现金流是：")
    print(flow)
    return  flow
good_annuity(100,3,isdue=False,isdelay=6)

#永续年金 (Perpetuity) 期初付期末付，延期时间,利率
def   Perpetuity(benji,i,time,isdue=True,isdelay=0):
    factor =1
    v = 1/(1+i)
    if not isdue:
        factor *=v
    while isdelay !=0:
        factor*=v
        isdelay-=1

    av= (benjin/i) *factor
    return  av
#每年支付 m 次的年金
def mmayearanuity(benji,numyear,fujici,isdue=True,isdelay=0):#本金，年数，每年负多少次，期末起初，延期
    isdelay = fujici*isdelay
    time =numyear*fujici
    benji = benji /fujici
    cash =[]
    isdelay =isdelay
    isdue =isdue
    if not isdue:
        cash+=([0]*(fujici-1))

    a=good_annuity(benji, time, isdue=isdue, isdelay=isdelay)
    cash+=a
    print("每年支付{}次的年金为".format(fujici))
    print(cash)
    return  cash
mmayearanuity(benji=100,numyear=2,fujici=5,isdue=False,isdelay=1)

#连续年金
def continuously_payable_annuity():
    pass

#变额年金
def increasingl(benji, time):
    av = []
    for i in range(time):
        av.append(benji * (1 + i))
    return av
def increasinglformm(benji,m, time):
    av = []
    for i in range(time):
        k=m
        while k!=0:
            av.append(benji * (1 + i))
            k-=1

    print("edyrc e5tjc r86 c,loEDed6fcduudfdu{}".format(av))
    return av

def decrease(benji, everynum, time):
    av = increasingl(everynum, time)
    mv = []
    for i in range(time):
        mv.append(benji)
    vvv = []
    for i in range(time):
        vvv.append(mv[i] - av[i])
    return vvv
def decreaseformm(benji, everynum,m, time):
    av = increasinglformm(everynum,m, time)
    mv = []
    for i in range(time):
        k=m
        while k!=0:

            mv.append(benji)
            k-=1
    vvv = []
    for i in range(time*m):
        vvv.append(mv[i] - av[i])
    return vvv

def Compound_increasing(benji, r, time):
    av = []
    av.append(benji)
    for i in range(1, time):
        av.append(av[i - 1] * (1 + r))
    return av

def increasing_annuity(benji, time, isdue=True, isdelay=0):
    flow = []
    if not isdue:
        flow.append(0)
    while isdelay != 0:
        flow.append(0)
        isdelay -= 1
    flow += increasingl(benji, time)
    print("该递增年金的现金流是：")
    print(flow)
    return flow
def increasing_annuityformm(benji, time,m, isdue=True, isdelay=0):
    flow = []
    if not isdue:
        flow.append(0)
    while isdelay != 0:
        flow.append(0)
        isdelay -= 1
    flow += increasinglformm(benji,m, time)
    print("该递增年金的现金流是：")
    print(flow)
    return flow

eg3 = increasing_annuity(benji=1, time=8, isdue=True, isdelay=0)

def decreasing_annuity(benji, time, everynum, isdue=True, isdelay=0):
    flow = []
    if not isdue:
        flow.append(0)
    while isdelay != 0:
        flow.append(0)
        isdelay -= 1
    flow += decrease(benji, everynum, time)
    print("该递减年金的现金流是：")
    print(flow)
    return flow

def decreasing_annuityformm(benji, time, everynum,m, isdue=True, isdelay=0):
    flow = []
    if not isdue:
        flow.append(0)
    while isdelay != 0:
        k=m
        while k!=0:
            flow.append(0)
            k-=1
        isdelay -= 1
    flow += decreaseformm(benji, everynum,m, time)
    print("该递减年金的现金流是：")
    print(flow)
    return flow

eg4 = decreasing_annuity(benji=20, time=10, everynum=1, isdue=True, isdelay=0)

def Compound_increasing_annuity(benji, time, r, isdue=True, isdelay=0):
    flow = []
    if not isdue:
        flow.append(0)
    while isdelay != 0:
        flow.append(0)
        isdelay -= 1
    av = Compound_increasing(benji, r, time)

    flow += av
    print("该复递增年金的现金流是：")
    print(flow)
    return flow
eg5 = Compound_increasing_annuity(benji=1, time=5, r=0.5, isdue=True, isdelay=2)


#每年支付 m 次的递增年金，递减年金，以及复递增年金

def  increasingmmayearanuity(benji,numyear,m,isdue=True,isdelay=0):#本金，年数，每年负多少次，期末起初，延期
    isdelay = m*isdelay
    time =numyear
    benji = benji /m
    cash =[]
    isdelay =isdelay
    isdue =isdue
    if not isdue:
        cash+=([0]*(m-1))

    a=increasing_annuityformm(benji, time, m,isdue=isdue, isdelay=isdelay)
    cash+=a
    print("每年支付{}次的递增年金为".format(m))
    print(cash)
    return  cash
eg6 =increasingmmayearanuity(benji=5,numyear=3,m=5,isdue=False,isdelay=1)

def  decreasingmmayearanuity(benjin, numyear,m, everynum, isdue=True, isdelay=0):#本金，年数，每年负多少次，期末起初，延期
    time =numyear
    benjin = benjin /m
    everynum =everynum/m
    cash =[]
    isdelay =isdelay
    isdue =isdue
    if not isdue:
        cash+=([0]*(m-1))
        print("打印了期初期末的0{}个".format(m-1))


    a = decreasing_annuityformm(benji=benjin, time=time, everynum=everynum,m=m, isdue=isdue, isdelay=isdelay)
    cash += a
    print("每年支付{}次的递减年金为".format(m))
    print(cash)
    return cash
eg8= decreasingmmayearanuity(benjin=10, numyear=3,m=2, everynum=2, isdue=False, isdelay=2)
print(eg8)
def compound_increasingmm_annuity(benji, time, r, m, isdue=True, isdelay=0):
    flow = []
    if not isdue:
        flow.append(0)
    while isdelay != 0:
        for _ in range(m):
            flow.append(0)
        isdelay -= 1
    av = Compound_increasing(benji, r, time)

    for _ in range(m):
        flow += av

    print("每年支付{}次的复递增年金为：".format(m))
    print(flow)
    return flow
                     # 在每年支付m次的复递增年金的定义上遇到了问题
eg9 = compound_increasingmm_annuity(benji=1, time=5, r=0.5, m=3, isdue=True, isdelay=0)



#连续支付的离散变额年金（递增、递减、复递增）
#连续变额年金
#◼ 一般形式的连续变额现金流
#◼ 特例：连续递增(或递减)的年





























