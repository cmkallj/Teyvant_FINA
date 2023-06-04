from Cashflow import  cashflow
from datetime import datetime
import AF_by_chapter1
import  chapter1
import chapter2and3
import  chapter4

#等额分期偿债法
#计算每期应还使用之前定义的贴现函数与现金流构造方法即可，现在我们需要定义的偿还债务的本息分解
#变额分期偿债法
#等额偿债基金
#变额偿债基金
class Loan:
    def __init__(self, total_amount, interest_rate, num_periods):
        self.total_amount = total_amount
        self.interest_rate = interest_rate
        self.num_periods = num_periods
#等额分期偿还
    def calculate_installment(self):
        installment = chapter2and3.good_annuity(benji=1, time=self.num_periods, isdue=True, isdelay=0)
        loancash = cashflow(cash=installment, period=self.num_periods, interst_rate=self.interest_rate)
        l = loancash.cal_AV(self.num_periods)
        R = self.total_amount / l[-1]
        loan = [R * k for k in installment]
        return loan
#常见的变额分期偿还,想用其他的时候调用你想要的产生其他现金流的函数即可
    def calculate_installmentformm(self):
        installment = chapter2and3.increasing_annuity(benji=1, time=self.num_periods, isdue=True, isdelay=0)
        loancash = cashflow(cash=installment, period=self.num_periods, interst_rate=self.interest_rate)
        l = loancash.cal_AV(self.num_periods)
        R = self.total_amount / l[-1]
        loan = [R * k for k in installment]
        return loan

    # 等额偿债基金，默认偿债基金累计为本金元
    def calculate_installmentforband(self,bandrate):
        installment = chapter2and3.good_annuity(benji=1, time=self.num_periods, isdue=True, isdelay=0)
        loancash = cashflow(cash=installment, period=self.num_periods, interst_rate=self.interest_rate)
        l = loancash.cal_FV(self.num_periods)
        R = self.total_amount / l[-1]
        loan = [R * k for k in installment]
        return loan
    # 变额偿债基金
    def calculate_installmentforbandformm(self,bondrate,momey):
        installment = chapter2and3.increasing_annuity(benji=1, time=self.num_periods, isdue=True, isdelay=0)
        loancash = cashflow(cash=installment, period=self.num_periods, interst_rate=bondrate)
        l = loancash.cal_FV(self.num_periods)
        R = money/ l[-1]
        loanofbond = [R * k for k in installment]

        return loanofbond
    def cal_zhaiwu(self,bondrate,):
        loanbond=calculate_installmentforbandformm(self,bondrate,momey=self.total_amount*(1/(1+bondrate))**self.num_periods)
        loan  =calculate_installmentforbandformm(self,bondrate=self.interest_rate,momey=self.total_amount-self.total_amount*(1/(1+bondrate))**self.num_periods)
        loans = [a + b for a, b in zip(loanbond, loan)]

        return  loans


    #本息分解
    def calculate_amortization_schedule(self):
        installments = self.calculate_installment()  # 偿还的现金流
        remaining_balance = self.total_amount  # 初始化欠款余额
        amortization_schedule = []
        i = 1

        for period, installment in enumerate(installments, start=1):  # 从第一期开始，每一期结算一次
            interest_payment = remaining_balance * self.interest_rate  # 该次偿还的利息
            principal_payment = abs(installment - interest_payment)  # 该次偿还的本金

            remaining_balance -=( principal_payment *(1+self.interest_rate)**i) # 该次偿还完剩下的余额
            i = i + 1

            amortization_schedule.append((period, installment, interest_payment, principal_payment, remaining_balance))

        return amortization_schedule


# Example usage
total_amount = 10000  # Total loan amount
interest_rate = 0.01  # Annual interest rate (5%)
num_periods = 20 # Number of periods (months)

loan = Loan(total_amount, interest_rate, num_periods)
amortization_schedule = loan.calculate_amortization_schedule()

# Print the amortization schedule
print("Period\tInstallment\tInterest\tPrincipal\tRemaining Balance")
for entry in amortization_schedule:
    period, installment, interest_payment, principal_payment, remaining_balance = entry
    print(f"{period}\t{installment:.2f}\t\t{interest_payment:.2f}\t\t{principal_payment:.2f}\t\t{remaining_balance:.2f}")
