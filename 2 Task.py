class DivisionByNull:
    def __init__(self, divisible, divisor):
        self.divisible = divisible
        self.divisor = divisor


    @staticmethod
    def divide_by_null(divisible, divisor):
        try:
            return divisible / divisor
        except:
            return "you can not devide by null"


div = DivisionByNull(555, 111)
print(DivisionByNull.divide_by_null(111, 0))
print(div.divide_by_null(555, 11))
print(DivisionByNull.divide_by_null(555, 11))
