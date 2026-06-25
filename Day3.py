# FACTORS OF A NUMBER
"""
Print all factors of the given number
"""
num = 24
i = 1
while i <= num:
    if num % i == 0:
        print(i, end=" ")
    i += 1

# COUNT FACTORS
"""
Count the total number of factors.
"""
num = 24
i = 1
count = 0
while i <= num:
    if num % i == 0:
        count += 1
    i += 1
print(f"Total Factors = {count}")

# COMMON FACTORS OF TWO NUMBERS
"""
Factors that are common to both numbers.
"""
a = 12
b = 18
i = 1
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        print(i, end=" ")
    i += 1

# HIGHEST COMMON FACTOR
"""
The largest factor common to both numbers.
"""
a = 12
b = 18
i = 1
hcf = 1
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        hcf = i
    i += 1
print(f"HCF = {hcf}")

# LEAST COMMON MULTIPLE
"""
Find the LCM.
"""
a = 12
b = 18
largest = a
if b > a:
    largest = b
while True:
    if largest % a == 0 and largest % b == 0:
        print(f"LCM = {largest}")
        break
    largest += 1

# COPRIME NUMBERS
"""
Check whether the numbers are coprime.
"""
a = 8
b = 15
i = 1
hcf = 1
while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        hcf = i
    i += 1
if hcf == 1:
    print("Coprime Numbers")
else:
    print("Not Coprime")

# PERFECT NUMBER
"""
Check whether the number is perfect.
"""
num = 28
i = 1
total = 0
while i < num:
    if num % i == 0:
        total += i
    i += 1
if total == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")

# FIND GREATEST FACTOR OTHER THAN ITSELF
"""
Print the greatest factor other than the number.
"""
num = 36
i = 1
greatest = 1
while i < num:
    if num % i == 0:
        greatest = i
    i += 1
print(greatest)

# FACTORY MACHINE SYNCHRONIZATION
"""
Find after how many minutes both machines will complete a cycle together again.
"""
machine1 = 12
machine2 = 18
time = machine1
if machine2 > machine1:
    time = machine2
while True:
    if time % machine1 == 0 and time % machine2 == 0:
        print(f"{time} Minutes")
        break
    time += 1

# GIFT BOX DISTRIBUTION
"""
Find the maximum number of gift boxes.
"""
chocolates = 24
biscuits = 36
i = 1
giftboxes = 1
while i <= chocolates and i <= biscuits:
    if chocolates % i == 0 and biscuits % i == 0:
        giftboxes = i
    i += 1
print(f"{giftboxes} Gift Boxes")