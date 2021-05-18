def add_fucntion(first, second):
    return first + second
def mul_fucntion(first, second):
    return first * second
def sub_fucntion(first, second):
    return first - second
def div_fucntion(first, second):
    return first / second
class Calculator:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        return c.first + c.second
    def mul(self):
        return c.first * c.second
    def sub(self):
        return c.first - c.second
    def div(self):
        return c.first / c.second
if __name__ == '__main__':
    c = Calculator()
    print(add_fucntion(1, 3))
    print(mul_fucntion(1, 3))
    print(sub_fucntion(1, 3))
    print(div_fucntion(1, 3))
