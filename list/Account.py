import random


class Account(object):

    def __init__(self, account_number, name, money):
        self.BANK_NAME = 'SC은행'
        self.name = name
        self.account_number = account_number
        self.money = money

    def to_string(self):
        return f'Bank Name: {self.BANK_NAME},' \
               f' Name: {self.name},' \
               f'Account Number: {self.account_number},' \
               f' Money: {self.money}'

    '''
    계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
    '''

    @staticmethod
    def create_account_number():
        ls = [str(random.randint(0, 9)) for i in range(3)]
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0, 9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0, 9)))
        return "".join(ls)  # "" ---> 공백없이 붙이라는 뜻


    @staticmethod
    def del_account(ls, account_number):
        for i, j in enumerate(ls):
            if j.account_number == account_number:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.계좌개설 2.계좌내용 3.입금 4.출금 5.계좌탈퇴')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(Account.create_account_number(),
                                  input('name'),
                                  input('money')))
            elif menu == '2':
                for i in ls:
                    print(i.to_string())

            elif menu == '3':
                account_number = input('입금할 계좌번호')
                money = input('입금액 입력바랍니다')
                for i, j in enumerate(ls):
                    if j.account_number == account_number:
                        replace = Account(j.account_number,
                                          j.name,
                                          int(j.money) + int(money))  # 입금 +
                        Account.del_account(ls, account_number)
                        ls.append(replace)
            elif menu == '4':
                account_number = input('출금할 계좌번호')
                money = input('출금액 입력바랍니다')
                for i, j in enumerate(ls):
                    if j.account_number == account_number:
                        replace = Account(j.account_number,
                                          j.name,
                                          int(j.money) - int(money))  # 출금 -
                        Account.del_account(ls, account_number)
                        ls.append(replace)
            elif menu == '5':
                Account.del_account(ls, input('삭제할 계좌번호'))
            else:
                print('Wrong Number')
                continue


Account.main()
