# Define numeric variables
integer_number = 15  # An integer value
float_number = 5.5   # A floating-point number
negative_number = -10  # A negative integer
lst = [21, 22]  # A list of integers

# Calculate the absolute value of a number
print(abs(negative_number))  
# Output: 10
# The abs() function returns the positive version of the given number.

# Round a floating-point number
print(round(float_number))  
# Output: 6
# The round() function rounds the number to the nearest integer. 
# 5.5 rounds up to 6, and 5.4 would round down to 5.

# Calculate the power of a number using pow()
print(pow(2, 3))  
# Output: 8
# The pow() function calculates 2 raised to the power of 3 (2^3).

# Calculate the power of a number using the ** operator
print(2**3)  
# Output: 8
# The ** operator is another way to calculate 2 raised to the power of 3.

# Find the maximum, minimum, sum, and average of a list
print(f"Maximum : {max(lst)} Minimum : {min(lst)} Sum : {sum(lst)} Average : {sum(lst) / len(lst)}")
# Output: Maximum : 22 Minimum : 21 Sum : 43 Average : 21.5
# max() returns the largest number in the list.
# min() returns the smallest number in the list.
# sum() returns the total sum of the numbers in the list.
# The average is calculated by dividing the sum by the number of elements in the list.

# Calculate the sum of a list with a starting value
print(sum(lst, 10))  
# Output: 53
# sum(lst, 10) starts the summation at 10 and then adds all the elements of the list to it.

# Calculate quotient and remainder using divmod()
quotient, remainder = divmod(20000, 150)
print(quotient, remainder)  
# Output: 133 50
# divmod() returns a tuple (quotient, remainder). 
# Here, it tells us that 20000 divided by 150 gives a quotient of 133 and a remainder of 50.

# Import the math module for additional mathematical functions
import math  

# Calculate the square root of a number
print(math.sqrt(64))  
# Output: 8.0
# The sqrt() function from the math module returns the square root of 64.
