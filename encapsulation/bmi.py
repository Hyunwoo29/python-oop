def bmi_function(weight, tall):
    return weight / tall ** 2 * 10000

class Bmi(object):
    def __init__(self, weight, tall):
        self.weight = weight
        self.tall = tall

    def get_bmi(self):
        return self.weight / self.tall ** 2 * 10000
"""
고도 비만 : 35 이상
중(重)도 비만 (2단계 비만) : 30 - 34.9
경도 비만 (1단계 비만) : 25 - 29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만
"""
    def get_bmigrade(self):
        bmi = ''
        index = self.weight / self.tall ** 2 * 10000
        if index >= 35:
            bmi = '고도 비만'
        elif index >= 30:
            bmi = '중도 비만'
        elif index >= 25:
            bmi = '경도 비만'
        elif index >= 23:
            bmi = '과체중'
        elif index >= 18.5 and index <= 22.9:
            bmi = '정상'
        else:
            bmi = '저체중'
        return bmi
    @staticmethod
    def main():
        c = Bmi(int(input('몸무개를 입력하시오')),int(input('키를 입력하시오')))
        print(f'결과 = {c.get_bmi()}')
        print(f'등급 = {c.get_bmigrade()}')

Bmi.main()