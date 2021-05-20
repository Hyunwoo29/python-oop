import random
class Account(object):
    def __init__(self,name, money):
        self.bank_name = 'SC은행'
        self.name = name
        self.money = money

        number1 = random.randint(0, 999)
        number2 = random.randint(0, 99)
        number3 = random.randint(0, 999999)

        number1 = str(number1).zfill(3)
        number2 = str(number2).zfill(2)
        number3 = str(number3).zfill(6)


        self.account_number = number1+'-'+number2+'-'+ number3


    def get_account(self):
        return f''
        return f'예금주: {self.name}'
        return f'잔액: {self.money}'
        return f'계좌번호: {self.account_number}'

    @staticmethod
    def main():
        while True:
            result = int(input("1.입력\n2.출력\n0.프로그램종료\n"))
            if result == 1:
                c = Account(input('예금주:'), int(input('잔액:')))
            elif result == 2:
                print(f'출력결과: {c.get_account()}')
            elif result == 0:
                break
            else:
                continue

Account.main()