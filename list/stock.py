class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code


    def to_string(self):
        return f'종목명: {self.name}, 종목코드: {self.code}'


    @staticmethod
    def del_element(ls, code):
        for i, j in enumerate(ls):
            if j.code == code:
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while True:
            result = int(input(" 1.입력\n 2.출력\n 3.수정\n 4.삭제\n 0.프로그램종료\n"))
            if result == 1:
                # stock = Stock(input(f'종목명:'), input(f'종목코드:')))
                # ls.append(stock)
                # ---- 이렇게 만들어도 된다. 대신 한개만 쓰는거니까 밑에처럼 넣어주는게 좋다.
                ls.append(Stock(input(f'종목명:'), input(f'종목코드:')))

            elif result == 2:
                for i in ls:
                    print(i.to_string())

            elif result == 3:
                code = input('종목코드:')
                stock = Stock(input('수정할 이름:'), code)
                stock.del_element(ls, code)
                ls.append(stock)

            elif result == 4:
                stock = Stock(None, input('종목코드:'))
                stock.del_element(ls)


            elif result == 0:
                     break

            else:
                continue

Stock.main()

