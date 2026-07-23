"""
1. A consecutive pass means students pass one after another without any failure in between. 
   Task: Read marks of N students and find the longest consecutive sequence of students scoring 35 or more.
"""
n = 8
marks = [40, 55, 20, 36, 70, 90, 15, 45]
i = 0
count = 0
longest = 0
while i<n:
    if marks[i]>=35:
        count+=1
        if count>longest:
            longest=count
    else:
        count=0
    i+=1
print(longest)

"""
2. A prime number has exactly two positive divisors. Task: Read N numbers and print the largest prime.
"""
n = 6 
numbers = [12, 17, 21, 29, 18, 7]
large_prime = 0
prime = 0
for num in numbers:
    count = 0
    fact = 1
    while fact<=num:
        if num%fact==0:
            count+=1
            if count>2:
                break
        fact+=1
    if count==2:
        prime = num
    if prime>large_prime:
        large_prime=prime
print(large_prime)

"""
3. Task: Read a number and print the sum of even digits.
"""
number = 4827316
sum = 0
while number>0:
    digit = number%10
    if digit%2==0:
        sum+=digit
    number//=10
print(f'Sum of even digits : {sum}')

"""
4. Quality below 50 is defective. Task: Read N scores and print defective and good counts.
"""
n = 6 
scores = [45, 60, 72, 38, 80, 49]
good_cnt, defective_cnt = 0, 0
i = 0
while i<n:
    if scores[i]>=50:
        good_cnt+=1
    else:
        defective_cnt+=1
    i+=1
print(f"""Defective count = {defective_cnt}
Good count = {good_cnt}""")

"""
5. Increase is today's sales minus yesterday's. Task: Find the maximum increase between consecutive days.
"""
n = 5 
sales = [100, 130, 110, 180, 200]
increase, max_increase = 0, 0
i = 0
while i<n-1:
    increase = sales[i+1]-sales[i]
    if increase>max_increase:
        max_increase = increase
    i+=1
print(f'Maximum increase among sales = {max_increase}')

"""
6. Digit count is the number of digits. Task: Print the number with the most digits.
"""
n = 5 
nums = [23, 9876, 105, 123456, 89]
i = 0
greatest_cnt = 0
while i<n:
    count = 0
    temp = nums[i]
    while temp>0:
        digit = temp%10
        count+=1
        temp//=10
    if count>greatest_cnt:
        greatest_cnt=count
        number = nums[i]
    i+=1
print(number)

"""
7. Count Numbers Divisible by Both 4 and 6
"""
n = 6 
nums = [12, 24, 18, 36, 40, 48]
i = 0
count = 0
while i<n:
    if nums[i]%4==0 and nums[i]%6==0:
        count+=1
    i+=1
print(count) 

"""
8. An odd streak is consecutive odd numbers. Task: Find the longest odd streak.
"""

n = 8 
streaks = [3, 5, 8, 7, 9, 11, 4, 13]
long_streak, streak = 0, 0
i = 0
while i<n:
    streak = streak+1 if streaks[i]%2!=0 else 0
    if streak>long_streak:
        long_streak = streak
    i+=1
print(long_streak)

"""
9. Digit sum is the sum of a number's digits. Task: Print the number with the smallest digit sum.
"""
n = 4
nums = [123, 81, 44, 70]
temp = nums[0]
smallest_sum = 0
while temp > 0:
    digit = temp % 10
    smallest_sum += digit
    temp //= 10
number = nums[0]

i = 1
while i < n:
    digit_sum = 0
    temp = nums[i]
    while temp > 0:
        digit = temp % 10
        digit_sum += digit
        temp //= 10
    if digit_sum < smallest_sum:
        smallest_sum = digit_sum
        number = nums[i]
    i += 1
print(f"Number with smallest digit sum = {number}")

"""
10. Running balance updates after each transaction. Task: Print balance after each transaction and final balance.
"""
balance = int(input("Enter initial balance: "))
n = int(input("Enter number of transactions: "))
i = 0
while i < n:
    transaction = int(input("Enter transaction: "))
    balance += transaction
    print(f"Balance = {balance}")
    i += 1
print(f"Final Balance = {balance}")