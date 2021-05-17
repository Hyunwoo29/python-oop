class Calculator:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return c.first + c.second
    def sub(self):
        return c.first - c.second
    def mul(self):
        return c.first * c.second
    def div(self):
        return c.first / c.second

if __name__ == '__main__':
    c = Calculator()
    c.setdata(1, 2)
    print(c.add())
    print(c.mul())
    print(c.sub())
    print(c.div())