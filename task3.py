class Except(Exception):
    def __init__(self):
        pass


class Check_num:
    def __init__(self):
        self.my_list = []

    def check_of_value(self):
        global val
        while True:
            try:
                try:
                    val = int(input('Введите число: '))
                    ex = input(f'В списке добавлено число "{val}". Хотите продолжить? да/нет').lower()
                    self.my_list.append(val)
                    if ex == 'нет':
                        print(f'Ваши числа: {self.my_list}')
                        break
                except ValueError:
                    raise Except
            except Except:
                ex = input(f"введите число цифрой! попробовать еще раз? да/нет").lower()
                if ex == 'нет':
                    print(self.my_list)
                    break
                else:
                    self.check_of_value()


a = Check_num()
a.check_of_value()
