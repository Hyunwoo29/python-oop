class Grade:
    def setdata(self, kr, en, math):
        self.kr = kr
        self.en = en
        self.math = math
    def add(self):
        return c.kr + c.en + c.math
    def sub(self):
        return c.kr - c.en + c.math
    def mul(self):
        return c.kr * c.en + c.math
    def div(self):
        return c.kr / c.en / c.math
    def avg(self):
        return self.add() / 3

if __name__ == '__main__':
    c = Grade()
    c.setdata(50,70,90)
    print(c.add())
    print(c.sub())
    print(c.mul())
    print(c.div())
    print(c.avg())