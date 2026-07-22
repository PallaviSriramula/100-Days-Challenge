"""
1. Task: A shop owner records the profit for N months. Print the highest profit and its month number.
"""
n = int(input('Enter number of months: '))
highest_profit = int(input('Enter profit of month 1: '))
month = 1

for i in range(2,n+1):
    profit = int(input(f'Enter profit of month {i}: '))

    if profit>highest_profit:
        highest_profit = profit
        month = i
print(f"""Highest profit = {highest_profit}
month = {month}""")

"""
2. Task: Read N numbers and count how many are perfect squares.
"""
n = 5
numbers = [16,20,25,18,49]
i = 0
count = 0
while i<n:
    num = numbers[i]
    j = 1
    while j*j <= num:
        if j*j == num:
            count+=1
        j+=1
    i+=1
print(f'Number of Perfect squares: {count}')

"""
3. Task: Read A and B. Sum all multiples of 7 between them.
"""
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))
sum = 0
for i in range(start,end+1):
    if i%7==0:
        sum+=i
print(f'Sum of Multiples of 7 between {start} and {end} = {sum}')

"""
4. Task: Read N numbers and find the longest positive streak.
"""
n = int(input("Enter how many numbers: "))
count = 0
longest = 0
i = 1
while i <= n:
    num = int(input("Enter a number: "))
    if num > 0:
        count += 1
        if count > longest:
            longest = count
    else:
        count = 0
    i += 1
print(f"Longest streak = {longest}")

"""
5. Task: Some numbers have exactly three positive divisors. Read N numbers and count them.
"""
numbers = [5,4,9,8,16,25]
count=0
for num in numbers:
    divisor = 0
    for i in range(1,num+1):
        if num%i==0:
            divisor+=1
    if divisor==3:
        count+=1
print(f'Count of Numbers which has 3 positive divisors = {count}')

"""
6. Task: Difference is the gap between two values. Find the largest difference between consecutive inputs.
"""
values = [5, 10, 25, 18, 40, 32]
n = 6
large_diff = 0
for i in range(n-1):
    if values[i] > values[i + 1]:
        diff = values[i] - values[i + 1]
    else:
        diff = values[i + 1] - values[i]

    if diff > large_diff:
        large_diff = diff
print(f"Largest difference ={large_diff}")

"""
7. Employees below a threshold qualify. Task: Count salaries below Rs.30000.
"""
n = 5 
salaries = [25000,40000,18000,32000,29000]
i = 0
count = 0
while i<n:
    if salaries[i]<30000:
        count+=1
    i+=1
print(count)

"""
8. Digit sum is the sum of all digits.Task: Print the number having the largest digit sum.
"""
n = 4
digits = [123,98,555,71]
largest_sum = 0
for i in digits:
    digit_sum = 0
    temp = i
    while temp>0:
        digit = temp%10
        digit_sum+=digit
        temp//=10
    if digit_sum>largest_sum:
        largest_sum = digit_sum
        result = i
print(f'Largest digit sum = {result}')

"""
9. Task: Read numbers until 0 and print the average.
"""
total = 0
count = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
    count += 1

average = total / count
print(f"Average = {average}")

"""
10. Compare values with the calculated average. Task: Read N numbers, compute average, then count numbers above it.
"""
n = 5
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
average = total / n
count = 0
for num in numbers:
    if num > average:
        count += 1

print(count)