"""
0.종료 1.계좌개설 2.계좌내용 3.입금 4.출금 5.계좌탈퇴2
Bank Name: SC은행, Name: a,Account Number: 463-91-056954, Money: 100
"""
import random
class Account(object):
    def __init__(self, name, money, account_number):
        self.name = name
        self.money = money
        self.account_number = account_number
        self.BANK_NAME = 'SC은행'

    def to_string(self):
        return f'BANK NAME: {self.BANK_NAME}'\
                f'Name: {self.name}' \
                f'Account Number: {self.account_number}'\
                f'Money: {self.money}'

    @staticmethod
    def creat_account_number():
        ls = [str(random.randint(0, 9)) for i in range(3)]
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0, 9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0, 9)))
        return "".join(ls)

    @staticmethod
    def del_account(ls, account_number):
        for i,j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.계좌개설, 2.계좌내용 3.입금 4.출금 5.계좌탈퇴')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(Account.creat_account_number(), input('name'), input('money')))
            elif menu == '2':
                for i in ls:
                    print(i.to_string)

            elif menu == '3':
                account_number = input('입금할 계좌번호:')
                money = input('입금액:')
                for i,j in enumerate(ls):
                    if j.account_number == account_number:
                        replace = Account(j.account_number, j.name, int(money)+ int(money))
                        Account.del_account(ls, account_number)
                        ls.append(replace)

            elif menu == '4':
                account_number = input('출금할 계좌번호:')
                money = input('출금액:')
                for i, j in enumerate(ls):
                    if j.account_number == account_number:
                        replace = Account(j.account_number, j.name, int(money) - int(money))
                        Account.del_account(ls, account_number)
                        ls.append(replace)
            elif menu == '5':
                Account.del_account(ls, input('삭제할 계좌번호:'))
            else:
                continue

