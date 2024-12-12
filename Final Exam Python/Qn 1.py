# 1 (i)
import math # since pi = 3.14
def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    return area

# Testing with radius of 4
radius = 5
area = circle_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")

# 1 (ii)
list = [4,7,2,9,12,15]
sum_of_odds = 0

for num in list:
    if num % 2 != 0:  # Check if the number is odd
        sum_of_odds += num

print("The sum of all odd numbers is:", sum_of_odds)


# 1 (iii) sum of two numbers
num1 = int(input('Enter the first number: ')) 
num2 = int(input('Enter the second number: '))
sum = num1 + num2
print(sum)

# difference of two numbers
num1 = int(input('Enter the first number: ')) 
num2 = int(input('Enter the second number: '))
difference = num1 - num2
print(difference)

# product of two numbers
num1 = int(input('Enter the first number: ')) 
num2 = int(input('Enter the second number: '))
product = num1 * num2
print(product)

# quotient of two numbers
num1 = int(input('Enter the first number: ')) 
num2 = int(input('Enter the second number: '))
quotient = num1 / num2
print(quotient)


# 1 (iv)
student_info = {'name':'Alice', 'age':20, 'grade':'A'}
student_info['age'] = 26
print(student_info)

# adding a new key_value
student_info["city"]='Kampala'
print(student_info)




