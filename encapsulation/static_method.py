class Bmi(object):
    def __init__(self, weight, tall):
        self.weight = weight
        self.tall = tall

    def get_bmi(self):
        return self.weight / self.tall ** 2 * 10000
