"""
이름, 출생년도, 주소를 입력받아서
회원가입한 사람의 이름, 나이(만), 주소를 출력하시오
"""
class Person(object):
    def __init__(self, name, year, address):
        self.name = name
        self.year = year
        self.address = address

    def person_name(self):
        return self.name

    def person_year(self):
        year = int(self.year)

        return 2020 - year

    def person_address(self):
        return self.address


    @staticmethod
    def main():
        g = Person(input('이름을 입력하시오:')), int(input('출생년도를 입력하시오:')), input('주소를 입력하시오:')))
        print(f'이름: {g.person_name()}')
        print(f'출생년도: {g.person_year()}')
        print(f'주소: {g.person_address()}')

Person.main()