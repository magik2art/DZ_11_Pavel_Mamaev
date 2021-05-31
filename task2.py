class Own(Exception):
    def __init__(self, txt):
        self.txt = txt


def div(num1, num2):
    try:
        if num2 == 0:
            raise Own("Делить на ноль нельзя, учи математику")
        else:
            res = num1 / num2
            return res
    except Own as err:
        return err


test = [0, 5]
print(div(test[0], test[1]))
print(div(test[1], test[0]))
