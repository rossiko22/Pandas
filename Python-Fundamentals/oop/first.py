import pickle
# class Car:
#     all = []
#     def __init__(self, engine: str , year : int):
#         assert engine != " ", "Engine cant be empty"
#         assert year != 0, "Year needs to be greater than 0"

#         self.engine = engine
#         self.year = year
#         Car.all.append(self)
    
#     def setnametonone(self):
#         self.engine = None

#     def __repr__(self):
#         return f"{self.year}"

# car = Car("Maric", 20)
# car = Car("Maric", 21)
# car = Car("Maric", 22)
# car = Car("Maric", 23)

# print(Car.all)
# dct = car.__dict__

# for marko in Car.all:
#     print(marko)
# car.setnametonone()

# for key, value in dct.items():
#     print(f"{key} : {value}")

# print(car.engine, car.year)



class Person:
    def __init__(self, gender: int):
        assert gender in [0, 1], "Gender can be only 1 and 0"
        self.gender = gender

    def hi(self):
        if self.gender == 0:
            print(f"I am a man")
        elif self.gender == 1:
            print("I am a woman")

class Man(Person):
    def __init__(self, name, gender=0 ):
        super().__init__(gender=gender)
        self.name = name

class Woman(Person):
    def __init__(self, name, gender=1):
        super().__init__(gender=gender)
        self.name = name
    
    def hi(self):
        print(1)

obj = None
with open("maric.txt", "rb") as f:
    obj = pickle.load(f)
obj.hi()