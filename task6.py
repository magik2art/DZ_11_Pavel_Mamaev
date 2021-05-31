class ComplexNumber:
    def __init__(self, num1, num2):
        self.num_1 = num1
        self.num_2 = num2

    def __add__(self, other):
        return f'Сумма равна: {self.num_1 + other.num_1} + {self.num_2 + other.num_2}'

    def __mul__(self, other):
        return f'Произведение равно: {self.num_1 * other.num_1 - (self.num_2 * other.num_2)} + {self.num_2 * other.num_1}'


first_num = ComplexNumber(10, 80)
second_num = ComplexNumber(3, 22)
print(first_num + second_num)
print(first_num * second_num)
