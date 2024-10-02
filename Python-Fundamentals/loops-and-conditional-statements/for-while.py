"""
Advanced Python Loop Syntax Documentation
"""

# `for` Loop with `continue` and `break`
# This loop iterates over a list of strings, using `continue` to skip "melon" and `break` to exit the loop when "dinasour" is encountered.
list_for_loops = ["banana", "melon", "watermelon", "apple", "dinasour"]

for item in list_for_loops:
    if item == "melon":
        continue  # Skip "melon"
    elif item == "dinasour":
        break   # Exit loop at "dinasour"
    print(item)
# Output: banana, watermelon, apple

# `for` Loop with `enumerate()`
# This loop iterates over a list, providing both the index and the value at each step.
for index, item in enumerate(list_for_loops):
    print(f"Index[{index}] : {item}")
# Output:
# Index[0] : banana
# Index[1] : melon
# Index[2] : watermelon
# Index[3] : apple
# Index[4] : dinasour

# `for` Loop with `zip()`
# This loop iterates over two lists in parallel, pairing corresponding elements from each list.
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 88]

for name, score in zip(names, scores):
    print(f"{name} scored {score} goals.")
# Output:
# Alice scored 85 goals.
# Bob scored 90 goals.
# Charlie scored 88 goals.

# List Comprehension with Conditional
# This one-liner creates a list of squares for even numbers from the input list.
list_for_comprehension = [i for i in range(0, 10)]
squares = [x**2 for x in list_for_comprehension if x % 2 == 0]
print(squares)
# Output: [0, 4, 16, 36, 64]

# `while` Loop with Increment
# This loop increments a variable from 10 to 14, printing each value.
i = 10
j = 15

while i < 15:
    print(i)
    i += 1
# Output: 10, 11, 12, 13, 14

while True:
    if j > 15:
        break
    j += 1