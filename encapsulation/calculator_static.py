def calculator_static():
    pass


class Calculatorstatic(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


    def add(self):
            return self.first + self.second

    def mul(self):
            return self.first * self.second

    def sub(self):
            return self.first - self.second

    def div(self):
            return self.first / self.second

    @staticmethod
    def main():
            calc = Calculatorstatic(int(input('첫번째 수 입력')), int(input('두번째 수 입력')))
            print(f'{calc.first} + {calc.second} = {calc.add()}')
            print(f'{calc.first} * {calc.second} = {calc.mul()}')
            print(f'{calc.first} - {calc.second} = {calc.sub()}')
            print(f'{calc.first} / {calc.second} = {calc.div()}')

Calculatorstatic.main()
