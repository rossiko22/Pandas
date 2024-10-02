#set can also hold multiple data types but set cant contain duplicate elements
#order that we make is not order that will be of set 
lst = [1, 2, 3, 4, "maric"]

my_set = set(lst)
my_new_set = {1, 2, 3, 4}

my_set.remove(3) # this removes element but raises error if it is not found in set
my_set.discard(5) # this removes element but doesnt raise error if it is not found in set
my_set.pop() # usually the last but the element order is not garanteed so any
my_set.clear() #clear set

#this is also like pointers if i make new_set = my_set i will edit the my_set when i edit new_set i am only refferencing by doing this
my_set = set(lst)
new_set = my_set

new_set.add(5)
print(f"My Set {my_set}")
print(f"My New Set {my_new_set}")

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
difference_set = set1 - set2
unique_set = set1 ^ set2 #elements only in one set but not in both
intersection_set = set1 & set2

print(f"Union set {union_set}")
print(f"Difference set {difference_set}")
print(f"Unique set {unique_set}")
print(f"Intersection set {intersection_set}")

print(1 in union_set)

list_duplicates = [1, 1, 2, 3, 4, 5, 6, 4, 6, 7, 5]
remove_duplicates_set = set(list_duplicates)
print(f"Remove Duplicates {remove_duplicates_set}")

#Frozen set is combination of tuple that we cant add or remove elementns , and that removes duplicates like sets
frozen_set = frozenset(remove_duplicates_set)
frozen_set = {1, 2, 3}
print(frozen_set)