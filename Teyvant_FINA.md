# 金融数学总结（Financial Mathematics）

###### 课程简介

1. 基于利息理论与微积分基础的金融数学1
2. "Options and Futures 期权与期货"
3. 套利机会arbitrage
4. 学习内容
5. ![](E:\pict_sea_of_fm\屏幕截图 2023-05-31 215222.png)
6. 第1章：利息度量
   第2章：等额年金
   第3章：变额年金
   第4章：收益率
   第5章：债务偿还方法
   第6章：债券和股票
   第7章：利率风险
   第10章：利率的期限结构 (自学)
   第8章：远期、期货和互换 金融衍生
   第9章：期权（简化B-S模型和期权交易策略） 工具
   第11章：随机利率 (自学）
7. MOOC地址址：https://www.icourse163.org/course/RUC-1463188162#/info
8. 常用的统计软件

Excel
◼ SPSS
◼ R
◼ (通过编程可以实现(开发)满足自己需要的函数或宏
包 )
◼ MATLAP
◼ SAS(是一个世界上最为优秀的统计分析软件之一)

#### 该项目的编程简介

我使用了python3.10，通过调用如numpy，matplotlib，scipy等库完成常见的在我们这本书中在的金融数学概念对象的定义，并通过对具体习题的解决和对现实生活中的一些问题的分析，来对我这个学期对金融数学这门课的总结与回顾



## 现金流的定义（cashflow)

![](E:\pict_sea_of_fm\屏幕截图 2023-05-31 221120.png)

######累计函数（accumualation function）

时间零点的1元在时间 t 的累积值, 记为a (t) 。

a(0)==1

金额函数或总量函数(Amount function)
当原始投资不是1个单位的本金,而是P个单位金额的
本金时,则把P个单位金额本金的原始投资在时刻t的累积
值记为A(t), 称为金额或总量函数.

使用特定的方法计算出的本金的增长随时间变化的函数，定义为一种方法，求现值和求累积值直接返回该时刻现金流的值就可以了

```
10
本金为
100
累计值为
[10, 20, 50, 100]
a(time=3,benjin=10)累计函数是1+t**2的情形
```





###### 利息（interest）

借用他人资金需支付的成本，
或出让资金获得的报酬

原因：资金的稀缺性；时间偏好（延迟消费的补偿）；资本也是生产力（是生产要素，要参与生产结果的分配）

与 时间，本金，利率，相关。

本金 (principal)：初始投资的资本金额。
 累积值 (accumulated value或终值(FV))：
一段时期后收到的总金额。
 利息 (interest)——累积值与本金之间的差额。

###### #时间的计算方法

（1） “实际/365”（actual/ 365）：投资天数按两个
日期之间的实际天数计算，每年按365天计算。
 （2）“实际/360 ”：投资天数按两个日期之间的实际天
数计算，每年按360天计算。称为行家规则 ( banker’s 
rule )。
 (3)“ 30/360 ”规则：
每月按30天计算, 每年按360天计算。两个给定日期之间
的天数按下述公式计算：
2 1 2 1 2 1 360( ) 30( ) ( ) Y Y M M D D − + − + − 其中起始日为Y2年M2月D2日，到期日为Y1年M1月D1日









######有效利率(也称为实际利率) (Effective rate of interest)

有效利率i 是期末获得的利息金额与期初本金之比法豆腐干豆腐干：

定义，方法，得到一段无进无出的现金流的利息的方法

> 把1000元存入银行，第1年末存款余额为1020
> 元，第2年末存款余额为1050元，求有效利率

```
[1.02, 1.0294117647058822]
get_eff_interst_rate([1000,1020,1050])
```



###### 单利和复利(Simple interest and compound interest)

只有本金产生利息，而利息不会产生新的利息

所以单利率相等，每一期产生的利息相等，但是有效利率随时间递减，由此可得，分段投资可产生更多的利息

取无进无出现金流，本金1，期数10 ，单利率0.1，考察其

有效利率的时间流

```
#结果
[0.10000000000000009, 0.09090909090909105, 0.08333333333333348, 0.07692307692307687, 0.0714285714285714, 0.06666666666666665, 0.0625, 0.05882352941176472, 0.05555555555555558, 0.052631578947368]
```

复利：前期的利息收入计入下一期的本金,即“利滚利”.
 Compound interest has been one of the foundation 
stones of the actuarial profession

相同长短的不同时期的实利率相等

取无进无出现金流，本金1，期数10 ，复利率0.1，考察其

有效利率的时间流

```
[0.10000000000000009, 0.10000000000000009, 0.10000000000000009, 0.10000000000000009, 0.09999999999999987, 0.10000000000000009, 0.09999999999999987, 0.10000000000000009, 0.09999999999999987, 0.10000000000000009]

Process finished with exit code 0

```



######贴现函数(Discount function)

时间 t 的1元(或1个单位本金或1个货币
单位)在时间零点的价值称为贴现函数, 记为 a-1（t）

常见的无进无出现金流的贴现

单利a-1（t) = (1+it)-1

复利：a-1(t)= (1+i)-1

有进有出现金流的贴现，几个术语

![](E:\pict_sea_of_fm\屏幕截图 2023-06-01 160122.png)



######有效贴现率(也称为实际贴现率)(Effective rate of discount with compound interest)

是期末获得的利息金额与期末累积值之比

关系：i = d\1-d

d = i\1+i

d = iv 

v=1-d

i-d -id

i = 1\n

d = 1\1+n





######⑤ 名义利率(Nominal rate of interest)

![](E:\pict_sea_of_fm\屏幕截图 2023-06-01 161127.png)

```
nominal_rate = 0.08
period1 = 1  # 年
period2 = 4  # 期数时间2（未提供具体数值）
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
effective_rate = nominal_to_effective_rate(nominal_rate, period1, period2)
print("转换后的有效利率:", effective_rate)
转换后的名义利率: 0.10250000000000004
转换后的有效利率: 0.0194265469082735
```

相关术语
◼ 利息结转期(或利息换算期): interest conversion period；
◼ 每月结转一次(或月换算)：convertible monthly；
◼ 每月支付一次：payable monthly ；
◼ 每月复利一次： compound monthly ；
◼ 季换算：payable quarterly ;
◼ 半年换算：compounded semiannually 

######名义贴现率(Nominal annual rate of discount)

```

#名义贴现率与有效贴现率的互换

def nominal_to_effective_discount_rate(nominal_rate, period):
    effective_rate =1- (1 - nominal_rate) ** (1 / period)
    return effective_rate
def effective_to_nominal_discount_rate(effective_rate, period):
    nominal_rate = 1-(1 + effective_rate) ** (-period)
    return nominal_rate
```

![](E:\pict_sea_of_fm\屏幕截图 2023-06-01 162718.png)

######利息力(连续复利) (Force of interest)贴现力 (Force of discount

![](E:\pict_sea_of_fm\屏幕截图 2023-06-01 162928.png)



##### 等额年金(Level annuity)

年金的含义和类型
② 期末付年金 (Annuity-immediate)
③ 期初付年金 (Annuity-due)
◼ 期初付与期末付年金的关系
④ 延期年金 (deferred annuity)
⑤ 永续年金 (Perpetuity)
⑥ 每年支付m次的年金 (mthly payable annuity)
⑦ 连续年金 (continuous payable annuity

就是时间周期固定，金额变化有规律的现金流

除开永续年金的现值与终值计算需要重新定义以外，其他的继承现金流的方法即可，我们著需要再重新定义不同种类年金的创建即可

年金 (Annuity)的相关概念:
 两次年金付款之间的间隔称为支付期(payment period);
 支付期的个数称为此年金的期;
 年金支付的金额称为年金金额(payment);

◼ 定期年金（period-certain annuity)
◼ 永续年金（perpetuity）, 例: 优先股

支付时点？
◼ 期初付年金（annuity-due）
◼ 期末付年金（annuity-immediate）
 开始支付的时间？
◼ 即期年金，简称年金
◼ 延期年金（deferred annuity）
 每次付款的金额是否相等？
◼ 等额年金(level annuity)
◼ 变额年金(varying annuity

⑥ 每年支付m次的年金 (mthly payable annuity)
⑦ 连续年金 (continuous payable annuity

![](E:\pict_sea_of_fm\屏幕截图 2023-06-01 193744.png)

###### 变额年金

离散变额年金
◼ 每年支付一次的离散变额年金(递增、递减、复递增)
◼ 每年支付 m 次的离散变额年金(递增、递减、复递增)
◼ 连续支付的离散变额年金（递增、递减、复递增）
 连续变额年金
◼ 一般形式的连续变额现金流
◼ 特例：连续递增(或递减)的

![](E:\pict_sea_of_fm\屏幕截图 2023-06-01 235141.png)

![](E:\pict_sea_of_fm\屏幕截图 2023-06-01 234909.png)

![](E:\pict_sea_of_fm\屏幕截图 2023-06-01 235042.png)

#### 收益率(yield rate）

投资活动最简单的两个个体: 基金本身(fund)和投资者(investor).
收益(yield): 
投资者在一定时间内将一定的资本进行投资活动所取得的收入

######净现值(net present value, NPV)与收益率

将投资资金流贴现到零时刻考察投资现值的方法也叫做
贴现现金流分析(DCF).

收益率 (yield rate)：使得资金流入的现值与资金流出的现
值相等时的利率. (临界利率)
也称作为内部报酬率(internal rate of return, IRR)
资金流入的现值与资金流出的现值之差就是净现值，所以
收益率也是使得净现值等于零的利率：

######• 基金的收益率(Yield rate of a fund) 

######• 币值加权收益率 (dollar-weighted yield rate )

```
def get_time_weighted_yield_rate(cashflow,weights):
    get = sum(cashflow)
    if len(returns) != len(weights):
        raise ValueError("收益列表和权重列表的长度必须相同")


    weighted_returns = [r * w for r, w in zip(cashflow, weights)]
    time_weighted_yield_rate= get / weighted_returns
    return  time_weighted_yield_rate

```

######• 时间加权收益率 (time-weighted yield rate )



######• 再投资与修正收益率 (modified rate of internal return)

######• 基金的收益分配(Allocating investment income)

######• 投资组合法(portfolio methods)

######• 投资年度法(investment year method,new year method

收益分配 (Allocating investment income)
 基金 (Fund): 从广义上说，基金是指为了某种目的而设立的
具有一定数量的资金。如：信托投资基金、公积金、保险基金、退
休基金，各种基金会的基金。
 狭义：证券投资基金。
 所谓基金是指一种利益共享、风险共担的集合证卷投资方式，即通过发
行基金单位，集中投资人的资金，由基金托管人委托基金管理人管理和
运用资金，从事股票、债卷等金融工具投资。

封闭式基金在发行期满后就封闭起来，投资者须
通过二级市场买入或卖出，其价格在很大程度上由市
场供求决定，波动类似于股票。但这种基金常有设定
的存续期限，一旦期满就进行清盘，将剩余资产按持
有份额分配给持有人或转成开放式基金继续存在下去。
且基金收益分配必须采用现金形式，不能配股。
开放式基金有两个特点：一方面基金的发行份额
是不固定的，投资者随时可按该基金的价格购买新的
份额，也可以随时要求基金公司赎回所购买的基金份
额，收回投资，退出基金，购买或赎回的价格以当时
基金单位资产净值为基础。另一方面是不设定存续期
限。
开放式基金的价格主要由资产价值而非市场供求
关系决定。投资者的收益主要来自基金的分红及基金
净资产价值的增值。故可用利息理论来研究

投 资 年 度 法
(investment year method，new year method)
 各年的收益率不同？投资年度法
 分配收益时使用的两种利率：
◼ 投资年度利率：投资年度不同，利率不同。
◼ 组合利率：不同年度的投资使用相同的平均利率。
 投资年度法的应用：新投资在前几年按投资年度利率分
配收益，超过一定年数以后，按组合利率分配收益

#### 债务偿还(Repaying Loans)

###### 等额分期偿还

借款人分期偿还贷款，在每次偿还的金额中，包括：
◼ 当期利息
◼ 一部分本金

```
class Loan:
    def __init__(self, total_amount, interest_rate, num_periods):#总金额，利率，期数
        self.total_amount = total_amount
        self.interest_rate = interest_rate
        self.num_periods = num_periods
#等额偿债的现金流
    def calculate_installment(self):
        installment==good_annuity(benji=1,time=self.num_periods,isdue=True,isdelay=0)
        loancash = cashflow(cash=installment,period=self.num_periods,interst_rate=self.interest_rate)
        l = loancash.cal_AV()
        R = self.total_amount/l
        loan = [R*kk for  kk in installment]
        installment =loan[0]
        return  installment

    def calculate_amortization_schedule(self):
        installment = self.calculate_installment()
        installment = installment[0]
        remaining_balance = self.total_amount
        amortization_schedule = []

        for period in range(1, self.num_periods + 1):
            interest_payment = remaining_balance * self.interest_rate / 12
            principal_payment = installment - interest_payment
            remaining_balance -= principal_payment

            amortization_schedule.append((period, installment, interest_payment, principal_payment, remaining_balance))

        return amortization_schedule

```



###### 等额偿债基金

偿债基金法：借款人为偿还债务而成立基金的做法.
借款人会在指定期限内，分期拨款人基金，累计起一笔足够
款项以偿还未来到期的债款.
一般的债券发行多数附有要求发债人设立偿债基金的条款

借款人在贷款期间：
◼ 分期偿还利息
◼ 积累偿债基金，到期时一次性偿还贷款本金

###### 变额分期偿还

仅需要改写还款的生成函数即可，本息分离不需要重写

L0 原始贷款本金
i 贷款年利率
n 贷款期限
I 借款人在每年末名义上支付的利息，即
I = iL0
j 偿债基金的利率
D 借款人每年末向偿债基金的储蓄

###### 匾额偿债基金

例子

Period	Installment	Interest	Principal	Remaining Balance
1	504.75		100.00		404.75		9591.20
2	504.75		95.91		408.84		9174.15
3	504.75		91.74		413.01		8748.63
4	504.75		87.49		417.26		8314.43
5	504.75		83.14		421.60		7871.32
6	504.75		78.71		426.03		7419.07
7	504.75		74.19		430.56		6957.46
8	504.75		69.57		435.17		6486.23
9	504.75		64.86		439.89		6005.13
10	504.75		60.05		444.70		5513.91
11	504.75		55.14		449.61		5012.30
12	504.75		50.12		454.62		4500.01
13	504.75		45.00		459.75		3976.78
14	504.75		39.77		464.98		3442.30
15	504.75		34.42		470.32		2896.26
16	504.75		28.96		475.78		2338.37
17	504.75		23.38		481.36		1768.29
18	504.75		17.68		487.06		1185.69
19	504.75		11.86		492.89		590.22
20	504.75		5.90		498.85		-18.47

Process finished with exit code 0







###因为我嗯时间安排的不够好，从第六章开始的编程实现先欠着吧，之后补上

#### 债卷与股票

证券 (Security)= 股票(Stock) + 债券(Bond) + 其他类型的证券
• 证券是一个总称，股票、债券是具体的某类证券的名称
• 总的来说，证券是指对未来某种经济收入的凭证。
“债券”和“股票”的区别
•债券：借钱的关系
• 你借给A 1万块钱，A承诺3个月后还你1万整。作为利息，还
会每个月给你50块钱；
• 不管A是富了穷了都与你无关，他到期就要给你这么钱，到
期A不给就是违约了；
• A可能是国家政府，也可能是企业。
•股票：入股的关系，一定份额的拥有权
• 你买了一公司多少股，你就有了这个公司多少股的拥有权，
也就是有了这个公司多少股的收益；
• 公司盈利，你就盈利，公司亏损，你就亏损了，没有承诺
说一定会给你多少收入；
•一般来说，债券风险低收益低，股票收益高风险高

###### 债卷定价

主要内容
 债券价值分析
◼ 债券定价原理
◼ 债券在任意时点上的价格和账面值
◼ 分期偿还债券的价格（非重点）
◼ 可赎回债券的价格
 股票价值分析

金融市场 (Financial Market)：
◼ 资金供求双方借助金融工具进行资金交易活动的场所，
◼ 就是实现资金从盈余者向短缺者流动的市场
◼ (在金融市场上，通过金融工具，资金得以融通，金融
交易得以进行)
 按照交易期限，分为：
◼ 货币市场 (Money market): 
 融资期限在一年以下(交易短期债务工具)
◼ 资本市场 (Capital market)：
 交易长期债务工具(到期期限通常在一年以上), 比如
股票市场、债券市场

债券的基本要素：
◼ 票面价值 (面值F)：100或1000元。
◼ (债券发行的)价格(P)：平价，溢价，折价
◼ 偿还期限：长期 (10年以上), 中期(1－10), 短期(1年以内)。
◼ 票面利率(息票率)。根据利息支付方式, 可分为附息
债券(Coupon, 票息) 和零息债券 (Zero-coupon

◼ P — 债券的价格(bond price)
◼ i —债券的到期收益率
(yield-to-maturity rate, internal rate of return)
指平均的每年实际收益或称内部收益，它表示债券投资的实
际年收益率。
◼ F — 债券的面值(或票面价值或到期值, 债券到期时支付给债
券持有人的金额(par value, face amount, nominal value)
◼ r — 债券的息票率
(coupon rate per payment period)
◼ rF —息票收入(coupon: 包含本金偿还+利息收入)
◼ C — 债券的偿还(或兑现)值 (redemption payment), 
 通常等于债券的面值，即C = F。
 例外：提前偿还时，偿还值不等于债券的面值。
◼ n —息票的支付次数 (number of coupon payments)。
◼ 投资者获得的利息收入: 
发行价格与面值的差额就是投资者获得的利息收入。
债券的现金流
定价公式
 基本公式
 溢价公式
 基价公式 (了解)
 Makeham公式 (了解

#### 利率风险

久期(duration)：马考勒久期，久期，有效久期
◼ 凸度(convexity)：马考勒凸度，凸度，有效凸度
◼ 免疫(immunization): 久期和凸度的应用
◼ 现金流配比(Cash flow matching)
◼ 衡量债券价格对市场利率敏感程度的两个主要指
标是久期和凸度，它们也是公司进行利率风险管
理的常用工具。

1. 久期（Duration）：久期是衡量债券价格对市场利率变动的敏感程度的指标。常见的久期类型包括马考勒久期（Macaulay Duration）、久期（Duration）和有效久期（Effective Duration）。
2. 凸度（Convexity）：凸度衡量债券价格对市场利率变动的非线性响应。与久期不同，凸度考虑了债券价格曲线的曲率。常见的凸度类型包括马考勒凸度（Macaulay Convexity）、凸度（Convexity）和有效凸度（Effective Convexity）。
3. 免疫（Immunization）：免疫是利用久期和凸度来管理债券投资的利率风险的方法。通过匹配久期和凸度，投资者可以构建一个投资组合，以确保在市场利率变动时，投资组合的价值保持稳定。
4. 现金流配比（Cash Flow Matching）：现金流配比是一种利用久期和凸度来匹配债券现金流与预期负债现金流的方法。通过合理安排债券的到期日和现金流，可以确保在特定时间点有足够的现金流来支付预期的负债。
5. 久期和凸度是衡量债券价格对市场利率敏感程度的两个主要指标。久期衡量价格的线性变化，而凸度衡量价格的非线性变化。投资者可以利用这些指标来评估债券的风险和回报，并进行有效的利率风险管理。

###### 久期

###### 凸度

#### 远期，期货与互换

远期 (forward)和期货 (futures)的基本概念
 远期和期货的定价
 合成远期 (synthetic forward)
 套保（hedge）和套利（arbitrage）
 互换（swap）的基本概念及其定价

1. 远期（Forward）：远期合约是双方协商在未来某个特定日期以约定的价格交换资产或商品的合约。合约的交割日期、交割价格和交割资产都在协商时确定。远期合约在交易所外进行，定价和交割条件根据协商达成。
2. 期货（Futures）：期货合约是标准化的远期合约，在交易所上进行交易。与远期合约不同，期货合约具有统一的标准化规格，包括交割日期、交割单位和交割地点等。期货合约的交割是通过现金结算或实物交割进行的。
3. 远期和期货的定价：远期和期货的定价涉及利率、存储成本、分红率、市场供需等因素。使用的主要模型包括无套利条件、期权定价模型（如Black-Scholes模型）和成本加成模型等。
4. 合成远期（Synthetic Forward）：合成远期是通过组合其他金融工具（如期权和现货）来模拟远期合约的效果。通过合成远期，投资者可以在没有实际远期合约的情况下获得类似的投资策略和风险暴露。
5. 套保（Hedge）和套利（Arbitrage）：套保是投资者为了对冲或减少特定风险而采取的行动。通过建立相反的头寸，套保可以降低投资组合的风险。套利则是利用市场的定价差异，在无风险或低风险条件下进行交易以获得利润。
6. 互换（Swap）：互换是一种合约，双方同意在未来的一段时间内交换资产流或支付流。常见的互换类型包括利率互换（Interest Rate Swap）、货币互换（Currency Swap）和股票互换（Equity Swap）等。互换的定价依赖于各种因素，包括利率差异、信用风险和市场预期等。

###### 远期期货

金融衍生产品 (Derivative instrument)：
 在货币、债券、股票等传统金融产品的基础上衍化和派
生的金融产品，其价值依赖于基础资产(underlying 
assets)的价值。
 这里的基础资产也称作标的资产，是一个相对概念，可
以是货币、债券、股票或商品，也可以是金融衍生品。
 也称为一种金融工具，其价值依赖于基础资产（如证券、
商品、利率或指数）的价格。
 常见的衍生产品(Derivative instrument)：
◼ 远期（forwards）
◼ 期货（futures）
◼ 互换（swaps）
◼ 期权（options）

金 融 衍 生 工 具 的 作用
 套期保值: 进行反向对冲交易，避免价格变化带来的损失。
 投机: 利用价差进行买卖从中获得利润(有风险)。
 套利：采用两个或更多相互抵消的交易锁定盈利(无风险)
 价格发现：大量市场参与者通过公开竞价形成均衡价格。
 提高信息透明度，降低交易成本。

一、远期 (Forward)
 远期合约（forward contract）：双方约定在未来
某一个确定的时间，按照某一确定的价格买卖一定
数量的某种资产的协议。
 远期合约是一种非标准化的合约，灵活性较强，双
方通过协商，来满足双方的需求。
 远期合约是为了规避现货交易的风险而产生的，
最初主要应用于农产品的交易，通过锁定未来的价
格，使得农产品的供需双方免受未来现货市场价格
波动的影响。
 例：小麦，石有

标的资产（underlying asset）：双方约定买卖的资产。如上
例中的小麦。
 交割价格(delivery price): 约定的成交价格。如每公斤1.5元。
 空头或空方（short forward, short position）：卖出标的资产
的一方。如上例中的农场主。
 多头或多方（long forward, long p

###### 定价

回收 (payoff):
持有人在合约满期时实现的现金价值。
◼ 多头的回收 ＝ 满期时的即期价格 － 交割价格
◼ 例:1年后以40美元买入石油,到期时石油价格为50美元。
◼ 空头的回收 ＝ －多头的回收

盈亏 (net payoff, profit), 也称作净回收或利润, 从回
收中扣除初始费用的终值。
 盈亏 ＝ 回收－初始费用的终值
◼ 注：即期价格就是到期日的实际价格。
◼ 远期合约的初始费用为零，故:盈亏 = 回收

###### 互换

#### 期权

期权的基本概念
 期权的回收和盈亏
 期权的平价关系
 期权定价模型
• 二叉树模型（重点）
• Black-Scholes(B-S)模型
 期权交易策略

1. 期权的基本概念：期权合约包括买方（持有权利）和卖方（承担义务）。买方支付权利金，获得在未来特定日期或期间内以约定价格（行权价格）购买或卖出资产的权利。卖方收取权利金，有义务在买方行使期权时履行合约。
2. 期权的回收和盈亏：期权的回收指期权行使时的盈利情况。对于买方而言，回收取决于期权行使时的市场价格和行权价格之间的差异。对于卖方而言，回收取决于权利金收入与实际履约成本之间的差异。
3. 期权的平价关系：期权的平价关系指相同标的资产、相同到期日和相同类型（认购期权或认沽期权）的期权应具有相同的理论价值。平价关系有助于寻找套利机会。
4. 期权定价模型：期权定价模型用于计算期权的理论价值。常用的模型包括二叉树模型和Black-Scholes（B-S）模型。

- 二叉树模型：通过构建期权价格的二叉树，模拟资产价格的上涨和下跌过程，计算期权的理论价值。
- Black-Scholes（B-S）模型：基于一些假设（如市场无风险利率恒定、资产价格服从几何布朗运动等），计算欧式期权的理论价值。

1. 期权交易策略：期权交易策略是根据投资者对市场走势的预期和风险承受能力制定的交易计划。常见的策略包括买入认购期权、买入认沽期权、卖出认购期权、卖出认沽期权等。





 









# 实验说明

##### 简介

作为这次的这次的课程的一些实践，我本来是想着我要特别认真写一个特别好的程序，来作为实践的，但是因为我可能摆烂，然后也比较，不是那么勤快，自己对这门课的学习，也不是特别认真，课下没有怎么花功夫，编程也是三天打鱼，两天晒网，不过呢。我大概离我自己想象的完成度少了一半多，从第六章开始便没有了编程的实现，想做一个GUI界面也只是搭了一个框架.所以目前的实践是一个半成品。但是，这次实践还是很有意义的，我在编程和调试的时候更加深入的理解了这个学期我们学习金融数学得到的知识，同时，也锻练了我的一些能力，在未来（放假的时候），我会继续完成该项目，作为我的编程实践，

环境

| Pillow          | 9.5.0  |        |
| --------------- | ------ | ------ |
| contourpy       | 1.0.7  | 1.0.7  |
| cycler          | 0.11.0 | 0.11.0 |
| fonttools       | 4.39.3 | 4.39.4 |
| kiwisolver      | 1.4.4  | 1.4.4  |
| matplotlib      | 3.7.1  |        |
| mpmath          | 1.3.0  | 1.3.0  |
| numpy           | 1.24.3 |        |
| packaging       | 23.1   |        |
| pandas          | 2.0.1  |        |
| pip             | 21.3.1 |        |
| pygame          | 2.4.0  |        |
| pyparsing       | 3.0.9  |        |
| python-dateutil | 2.8.2  |        |
| pytz            | 2023.3 |        |
| scipy           | 1.10.1 |        |
| setuptools      | 60.2.0 |        |
| six             | 1.16.0 |        |
| sympy           | 1.11.1 |        |
| tzdata          | 2023.3 |        |
| wheel           | 0.37.1 |        |

#### 具体代码，见文件夹中的py文件，大概有500行好像，是一个比较小的demo，实现的思路也比较简单，没有什么复杂的数据结构。调用了一些与数值计算相关的包，比如收益率的计算哪里scipy，使用numpy数组是数据分析所必须要的，matplotlib本来是象拿来可视化一些现金流的分解啊，还有画后面的之类图的，不过现在没有了，之后我会添加的，pygame是可视化。主要用的应该就这些，其他有很多是我当年雄心壮志但是失败的残留

#上传地址以及后续更新地址：

####在给一些写的时候的一些测试例子

```
:\PycharmProjects\Teyvat_Fincial\venv\Scripts\python.exe E:\PycharmProjects\Teyvat_Fincial\venv\Lib\site-packages\pip-21.3.1.dist-info\chapter5.py 
[1, 1.01]
[10, 10.089041095890412]
[1, 1.0425, 1.08680625, 1.132995515625]
10
本金为
132.5
累计值为
[10, 20, 50, 100, 132.5]
[0.020000000000000018, 0.02941176470588225]
[0.09999999999999998]
两个日期之间的天数: 119
[0.10000000000000009, 0.09090909090909105, 0.08333333333333348, 0.07692307692307687, 0.0714285714285714, 0.06666666666666665, 0.0625, 0.05882352941176472, 0.05555555555555558, 0.05263157894736836]
[0.10000000000000009, 0.10000000000000009, 0.09090909090909105, 0.08333333333333348, 0.07692307692307687, 0.0714285714285714, 0.06666666666666665, 0.0625, 0.05882352941176472, 0.05555555555555536]
转换后的名义利率: 0.10250000000000004
转换后的有效利率: 0.0194265469082735
转换后的有效贴现率: 0.05131670194948623
转换后的名义贴现率: 0.09524108301747614
单利率: 1.2214027581601699
利息力: 0.999896315728952
ln m: 2.302585092994046
该年金的现金流是：
[0, 0, 0, 0, 0, 0, 0, 100, 100, 100]
该年金的现金流是：
[0, 0, 0, 0, 0, 0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0]
每年支付5次的年金为
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0, 20.0]
该递增年金的现金流是：
[1, 2, 3, 4, 5, 6, 7, 8]
该递减年金的现金流是：
[19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
该复递增年金的现金流是：
[0, 0, 1, 1.5, 2.25, 3.375, 5.0625]
edyrc e5tjc r86 c,loEDed6fcduudfdu[1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0]
该递增年金的现金流是：
[0, 0, 0, 0, 0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0]
每年支付5次的递增年金为
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 3.0, 3.0, 3.0, 3.0]
打印了期初期末的01个
edyrc e5tjc r86 c,loEDed6fcduudfdu[1.0, 1.0, 2.0, 2.0, 3.0, 3.0]
该递减年金的现金流是：
[0, 0, 0, 0, 0, 4.0, 4.0, 3.0, 3.0, 2.0, 2.0]
每年支付2次的递减年金为
[0, 0, 0, 0, 0, 0, 4.0, 4.0, 3.0, 3.0, 2.0, 2.0]
[0, 0, 0, 0, 0, 0, 4.0, 4.0, 3.0, 3.0, 2.0, 2.0]
每年支付3次的复递增年金为：
[1, 1.5, 2.25, 3.375, 5.0625, 1, 1.5, 2.25, 3.375, 5.0625, 1, 1.5, 2.25, 3.375, 5.0625]
[-0.06825485849042448, 0.07325485849042324]
[-0.06825485849042448, 0.07325485849042324]
投资发生后的账户余额，从t=0kaisji，
[2, 6, 14, 30]
[2.0, 4.0, 8.0, 16.0]
该年金的现金流是：
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Period	Installment	Interest	Principal	Remaining Balance
1	504.75		100.00		404.75		9591.20
2	504.75		95.91		408.84		9174.15
3	504.75		91.74		413.01		8748.63
4	504.75		87.49		417.26		8314.43
5	504.75		83.14		421.60		7871.32
6	504.75		78.71		426.03		7419.07
7	504.75		74.19		430.56		6957.46
8	504.75		69.57		435.17		6486.23
9	504.75		64.86		439.89		6005.13
10	504.75		60.05		444.70		5513.91
11	504.75		55.14		449.61		5012.30
12	504.75		50.12		454.62		4500.01
13	504.75		45.00		459.75		3976.78
14	504.75		39.77		464.98		3442.30
15	504.75		34.42		470.32		2896.26
16	504.75		28.96		475.78		2338.37
17	504.75		23.38		481.36		1768.29
18	504.75		17.68		487.06		1185.69
19	504.75		11.86		492.89		590.22
20	504.75		5.90		498.85		-18.47

Process finished with exit code 0

```



## chapter1



> 半年期的定期存款利率是2%。请问1万元存半年，到期
> 的利息是多少？

```python
 a1 = cashflow(cash=[1],interst_rate=0.01,period=1)
m=a1.cal_FV(time= 1)
print(m)  
#结果
[1, 1.01]
#答案1.01
```

> 三年期的定期存款利率是4.25%。请问1万元存三年，
> 到期的利息是多少？
>
> 银行推出的理财产品为65天，预期年化收益率为5%，
> 购买10万元到期可以获得多少利息

 

```python
#[1, 1.01]
#[10, 10.089041095890412]
#[1, 1.0425, 1.08680625, 1.132995515625]
a1 = cashflow(cash=[10],interst_rate=0.05,period=1)
m=a1.cal_FV(time=cal_period_true_rule(65))
print(m)
a1 = cashflow(cash=[1],interst_rate=0.0425,period=1)
m=a1.cal_FV(time=3)
print(m)
```



##chapter2

## chapter4

##chapter5

##chapter6

##chapter7

##chapter8

##chapter9

```
from Cashflow import  cashflow
from datetime import datetime
import AF_by_chapter1
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
            k-=0
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

def decreasing_annuityformm(benji, time, everynum, isdue=True, isdelay=0):
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

def  decreasingmmayearanuity(benji, numyear,m, everynum, isdue=True, isdelay=0):#本金，年数，每年负多少次，期末起初，延期
    time =numyear
    benji = benji /m
    everynum =everynum/m
    cash =[]
    isdelay =isdelay
    isdue =isdue
    if not isdue:
        cash+=([0]*(m-1))

    a = decreasing_annuityformm(benji=benjin, time=time, everynum=everynum, isdue=isdue, isdelay=isdelay)
    cash += a
    print("每年支付{}次的递减年金为".format(m))
    print(cash)
    return cash
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



```

