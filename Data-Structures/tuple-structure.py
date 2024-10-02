#tuple can also hold multiple datatypes
my_tuple = (1, 2, 3, 4, "Maric")

new_tuple = my_tuple * 2 # it is the same tuple twice (1, 2, 3, 1, 1, 2, 3, 1)

big_tuple = new_tuple + my_tuple

a, b ,c ,d, e = my_tuple # tuple unpacking

print(a, b , c ,d )
print(my_tuple)
print(new_tuple)
print(big_tuple)




a = 2
b = 4

print(f"a = {a} b = {b}")
a, b = b, a
print(f"a = {a} b = {b}")
