#mutable - moze da se menja u njima koe kako kje stoi, moze duplikati , i moze da ima povise data types u njima

class Engine:
    def __init__(self, power):
        self.power = power

    def getPower(self):
        return self.power

lst = ["marko", 123, "maki", 12.3, Engine(150)]

print(lst[len(lst) - 1].power)

list_functions = [1, 2, 3, 1, 4, 5, 1]

list_functions.append(6)
list_functions.insert(0,9)
list_functions.remove(9)

sub_list = list_functions[1:4]

print(list_functions.count(1))
print(list_functions)

contains_one = [s for s in list_functions if 1 == s]
loop_check = []

#find all occurences of some element
for index, element in enumerate(list_functions):
    if element == 1:
            loop_check.append(list_functions.index(element, index))

matching_strings = list(filter(lambda s: s == 1, list_functions))
print(matching_strings)
print(contains_one)
print(loop_check)