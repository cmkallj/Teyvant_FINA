from Cashflow import  cashflow
from datetime import datetime
import AF_by_chapter1
import  chapter1
import chapter2and3
#收益率
from scipy.optimize import root_scalar

#流入流出现金流的合成
def get_allcashflow(incash:list,outcash:list):
    allcash = [i + o for i, o in zip(incash, outcash)]
    return  allcash
#流入流出现金流贴现表达式的计算
def  fuc_R(i,allcash):
    v= (1+i)**(-1)
    f = 0
    for i in range(len(allcash)):
        f =f**v+allcash+allcash[-i]
    return  f
#收益率的计算
def cal_yield_rate(allcash,a,b):
    def f(i):
        v = (1 + i) ** (-1)
        R = sum([cash * v ** index for index, cash in enumerate(allcash)])
        return R
    try:
        result = root_scalar(f, bracket=[a, b])
        i = result.root
    except ValueError:
        i= None
    return i
def   get_all_yield_rate(allcash,jindu=0.012323):
    a=-0.4
    amlyst=[]
    while a<1:
        answ=cal_yield_rate(allcash,a,a+jindu)
        if answ!=None:
            amlyst.append(answ)
        a+=jindu
    print(amlyst)
    return  amlyst


allcash = [100, -200.5, 100]
i = get_all_yield_rate(allcash)
print(i)


#币值加权收益率((time-weighted yield rate）
def get_time_weights(cashflow):
    weights=[]
    n=len(cashflow)
    for i in range(n):
        weights.append(n-i/n)
    return  weights
def get_dollar_weighted_yield_rate(cashflow,weights):
    get = sum(cashflow)
    if len(returns) != len(weights):
        raise ValueError("收益列表和权重列表的长度必须相同")


    weighted_returns = [r * w for r, w in zip(cashflow, weights)]
    dollar_weighted_yield_rate= get / weighted_returns
    return  dollar_weighted_yield_rate
#时间加权收益率
def calculate_time_weighted_rate(investment, bookvalue):
    """
    计算收益率

    参数:
    investment (list[float]): 投入的现金流，从时间第0期开始计算
    bookvalue (list[float]): 投资期间的现金流列表，正数表示投入的现金，负数表示提取的现金

    返回:
    time_weighted_rate (list[float]): 时间加权收益率
    """
    benjin = []
    investment =  [0]+investment+[0]
    #(list[float]): #投资期间的现金流列表，正数表示投入的现金，负数表示提取的现金
    for i in range(1,len(investment)):
        benjin.append(bookvalue[i]-investment[i])
    print("投资发生后的账户余额，从t=0kaisji，")
    print(benjin)
    bookvalue.pop()

    time_weighted_rate = []
    time_weighted_rate.append(benjin[0]/bookvalue[0])
    for i in range(1, len(bookvalue)):
        time_weighted_rate.append( time_weighted_rate[i-1]*(benjin[i]/bookvalue[i]))
   # time_weighted_rate =[r-1 for r in time_weighted_rate]

    return time_weighted_rate

a = calculate_time_weighted_rate([1, 1, 1], [1,3,7,15,30])
print(a)
#再投资与修正收益率
#再投资：前期投资的收入按新的利率再次进行投资。
def complex_investment():
    pass
'''
事实上，就是现金流的复合而已，利用我们之前定义的现金流生成函数进行复合即可
'''

