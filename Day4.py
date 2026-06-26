# RUNNING SUM TRIANGLE
"""
For each row, add numbers from 1 up to that row number.
"""
n = 5
for i in range(1, n + 1):
    total = 0
    for j in range(1, i + 1):
        total += j
        if j < i:
            print(j, end="+")
        else:
            print(j, end="")
    print(f" = {total}")

# MULTIPLICATION TABLE STATISTICS
"""
Count how many multiplication results are less than 20, between 20 and 50, and greater than 50.
"""
lessthan20 = 0
btw20nad50 = 0
greateerthan50 = 0
total = 0
for i in range(2,21):
    for j in range(1,11):
        total = i*j
        if total<20:
            lessthan20+=1
        elif 20<=total<=50:
            btw20nad50 += 1
        elif total>50:
            greateerthan50 +=1
print(f"Less than 20 = {lessthan20}")
print(f"Between 20 and 50 = {btw20nad50}")
print(f"Greater than 50 = {greateerthan50}")

# STUDENT MARKS COMPETITION
"""
For each student count how many students scored more than them.
"""
marks = [85, 70, 92, 78, 88]
for mark in marks:
    greater = 0
    for j in marks:
        if j>mark:
            greater+=1
    print(f"{mark} -> {greater}")

# SALES LEADERBOARD
"""
Find rank of every salesperson.
"""
sales = [500, 900, 700, 1200]
for sale in sales:
    highest = 1
    for j in sales:
        if j>sale:
            highest+=1
    print(f"{sale} -> Rank{highest}")

# PAIR SUM FINDER
"""
Print all pairs whose sum is 10.
"""
numbers = [2, 5, 7, 8, 3]
total = 0
for num in numbers:
    for j in numbers:
        total = num+j
        if total == 10:
            print(f"{num}+{j}")

# PAIR PRODUCT FINDER
"""
Print all pairs whose product is 24.
"""
numbers=[2,3,4,6,8]
total=0
for num in numbers:
    for j in numbers:
        total=num*j
        if total==24:
            print(f"{num}*{j}")

# MATRIX TOTAL
"""
Find total of all values.
"""
Data=[[10,20,30],[40,50,60],[70,80,90]]
total=0
for i in Data:
    for j in i:
        total+=j
print(f"Total = {total}")

# ROW WISE TOTALS
"""
Find sum of every row.
"""
Data=[[10,20,30],[40,50,60],[70,80,90]]
total = 0
rownum = 1
for i in Data:
    total = 0
    for j in i:
        total += j
    print(f"Row {rownum} = {total}") 
    rownum+=1

# MATCH SCHEDULE GENERATOR
"""
Generate all matches.
"""
teams=['A','B','C','D']
for i in range(len(teams)):
    for j in range(i+1,len(teams)):
        print(f"{teams[i]} VS {teams[j]}")
    

#HIGHEST ROW TOTAL
"""
Find row having highest total.
"""
Data = [[10,20,30],[50,60,70],[15,25,35]]
highest =0
rownum = 0
currentrow = 1
for i in Data:
    total = 0
    for j in i:
        total += j
    if total>highest:
        highest = total
        rownum = currentrow
    currentrow+=1 
print(f"Row {rownum}")
print(f"Total = {highest}")