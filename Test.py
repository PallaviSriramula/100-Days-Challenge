"""
1. Write a program that accepts an integer and prints whether it is positive, negative, or zero.
"""
n = int(input("Enter a number: "))
if n==0:
    print('zero')
elif n>0:
    print(f'Entered number {n} is a Positive number')
else:
    print(f'Entered number {n} is a negative number')

"""
2. Write a program that takes a student's marks as input and prints:
   - "Pass" if marks are 40 or more
   - "Fail" otherwise
"""
marks = int(input("Enter marks obtained: "))
if marks>=40:
    print("Pass")
else:
    print("Fail")

"""
3. Write a program that checks whether a given year is a leap year.
"""
year = int(input("Enter the year: "))
if (year%4==0 and year%100!=0) or year%400==0:
    print('Leap Year')

"""
4. Using a for loop, print all even numbers from 1 to 50.
"""
for num in range(1,51):
    if num%2==0:
        print(num)
"""
5. Write a program to find the sum of all numbers from 1 to n, where n is entered by the user.
"""
n = int(input("Enter the number: "))
sum = 0
for num in range(1,n+1):
    sum += num
print(f'Sum of numbers from 1 to {n} : {sum}') 

"""
6. Write a program that counts how many digits are present in a number entered by the user.  
   Example: 12345 → 5
"""
number = input("Enter the number: ")
count = 0
for num in number:
    count+=1
print(f'Total no.of digits in {number} are {count}')

"""
7. Using a loop, print the multiplication table of a number entered by the user up to 10.
"""
number = int(input("Enter the number: "))
for i in range(1,11):
    mul = number*i
    print(f'{number} X {i} = {mul}')

"""
8. Define a function is_even(number) that returns True if the number is even; otherwise returns False.
"""
def is_even(number):
    if number%2==0:
        return True
    else:
        return False
print(is_even(24))

"""
9. Define a function largest_of_three(a, b, c) that returns the largest of three numbers without using max().
"""
def largest_of_three(a,b,c): # 9 8 10  # 10 9 8  # 9 10 8
    if a>b and a>c:
            largest = a
    elif b>a and b>c:
            largest = b
    else:
        largest = c
    return largest

print(largest_of_three(1,9,18))

"""
10. Define a function count_vowels(text) that returns the number of vowels in a given string.
"""
def count_vowels(string):
    count = 0
    for i in string:
        if i in 'aeiouAEIOU':
            count+=1
    return count
print(count_vowels('watermelon'))

"""
11. Given this list:
    numbers = [3, 8, 12, 5, 7, 10, 15]
    Use a list comprehension to create a new list containing only the even numbers.
"""
numbers = [3, 8, 12, 5, 7, 10, 15]
even = [num for num in numbers if num%2==0]
print(even)

"""
12. Given this list:
    words = ["python", "java", "c", "javascript", "go"]
    Use a dictionary comprehension to create a dictionary where each word is a key and its length is the value.
"""
words = ["python", "java", "c", "javascript", "go"]
print((dictionary := {word: len(word) for word in words}))
