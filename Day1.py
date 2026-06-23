# 1. GROCERY STORE BILLING WITH DISCOUNT
"""
Calculate the total bill. If an item price is greater than 1000, give a 10% discount on that item. Calculate the final bill after discount.
"""
prices = [500,1200,800,1500]
totalbill = 0 
for i in prices:
    if i>1000:
        i -= i*10/100
    totalbill += i
print(f"The total bill is {totalbill}")

# 2. EMPLOYEE ATTENDANCE PERCENTAGE
"""
Calculate the total present days and attendance percentage.
"""
attendance = ['P','A','P','P','A','P']
count = 0
totaldays = 0
percentage = 0.0
for i in attendance:
    if i=='P':
        count+=1
    totaldays += 1
percentage = (count/totaldays)*100
print(f"Present days = {count}")
print(f"Attendance Percentage = {percentage}%")

# 3. ONLINE SHOPPING CART
"""
-1 means item removed from cart. Ignore removed items and calculate the total amount.
"""
cart = [500,-1,700,1200,-1,300]
total = 0 
for i in cart:
    if i==-1:
        continue
    total +=i
print(f"Total Amount = {total}")

# 4. BANK TRANSACTIONS
"""
Process transactions one by one. Stop if the balance becomes negative. Display the final balance.
"""
transactions = [5000,-2000,-3000,-4000]
balance = 6000
for i in transactions:
    balance += i
    if balance<i:
        print("Insufficient balance")
        break
print(f"Final balance = {balance}")

# 5. CRICKET TOURNAMENT ANALYSIS
"""
Find the total runs, highest score, and average score.
"""
runs = [45,80,22,95,60]
total=average=count = 0
highest = runs[0]
for i in runs:
    total += i
    count +=1
    if i>highest:
        highest = i
print(f"Total = {total}")
print(f"Highest = {highest}")
print(f"Average = {total/count}")

# 6. ELECTRICITY CONSUMPTION BILLING
"""
Calculate the electricity bill using: First 100 units = 5/unit Remaining units = 8/unit
"""
units = [120,150,200,180]
ind = 0
bill = 0
while ind<len(units):
    if units[ind]>100:
        bill += (100*5) + ((units[ind] -100) * 8)
    else:
        bill += units[ind] *5
    ind+=1

print(f"Total Bill = {bill}")

# 7. EXAM RESULT PROCESSING 
"""
Count how many students passed and failed. Pass mark = 35.
"""
marks = [75,30,82,40,95,28]
count = 0
for i in marks:
    if i<35:
        count+=1
print(f"Number of students passed are {len(marks)-count}")
print(f"Number of students failed are {count}")

# 8. FOOD DELIVERY PERFORMANCE
"""
0 means not rated. Ignore those ratings and calculate the average rating.
"""
ratings = [5,4,0,3,5,0,4]
total = count = 0
for i in ratings:
    if i==0:
        count += 1
        continue
    total += i
print(f"Average Rating: {total/(len(ratings)-count)}")

# 9. ATM CASH DISPENSING
"""
Calculate the minimum number of notes required using 2000, 500, 200, and 100 notes.
"""
amount=3700
notes_2k=notes_500=notes_200=notes_100=0
while amount >=2000:
    notes_2k+=1
    amount-=2000
while amount >=500:
    notes_500+=1
    amount-=500
while amount >=200:
    notes_200+=1
    amount-=200
while amount >=100:
    notes_100+=1
    amount-=100
print(f"2000 *{notes_2k}")
print(f"500 *{notes_500}")
print(f"200 *{notes_200}")
print(f"100 *{notes_100}")

# 10. SALES REPORT GENERATOR
"""
-1 means holiday (skip it). 0 means system crash (stop processing). Calculate total sales before crash.
"""
sales = [5000,7000,-1,9000,0,8000]
totalsales = 0
for i in sales:
    if i==-1:
        continue
    elif i==0:
        break
    totalsales += i
print(f"Total Sales = {totalsales}")