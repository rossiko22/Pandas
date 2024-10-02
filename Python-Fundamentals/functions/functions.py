# n = 20
# def getNumbers(num1, num2=3):
#     global n
#     return num1 + num2 + n

# num = getNumbers(1,1)


class Engine:
    def __init__(self, power: int):
        if not isinstance(power,int):
            raise TypeError(f"Expected an integer")
        self.power = power

engine = Engine(123)
print(type(engine.power))