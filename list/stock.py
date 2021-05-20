class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code
    def get_Stock(self):
        return f'종목명: {self.name}, 종목코드: {self.code}'

    @staticmethod
    def main():
        ls = []
        while True:
            result = int(input(" 1.입력\n 2.출력\n 3.삭제\n 0.프로그램종료\n"))
            if result == 1:
                ls.append(Stock(input(f'종목명:'), input(f'종목코드:')))
            elif result == 2:
                for i in ls:
                    print(i.get_Stock())
            elif result == 3:
                del_name = input('삭제할 종목:')
                for i,j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]
            elif result == 0:
                break
            else:
                continue

Stock.main()