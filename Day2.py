# LONGEST LOGIN STREAK
"""
1 means logged in and 0 means missed day. Find the longest continuous login streak.
"""
logins = [1,1,0,1,1,1,0,1]
streak = 0
Longeststreak = 0 
for login in logins:
    if login == 1:
        streak+=1
        if streak>Longeststreak:
            Longeststreak = streak
    else:
        streak=0
print(f"Longest Streak = {Longeststreak}")

# PASSWORD STRENGTH CHECKER
"""
Count uppercase letters, lowercase letters, and digits. Print Strong Password if it contains 
at least one uppercase letter, one lowercase letter, and one digit.
"""
password = 'Abc123X'
Uppercase = Lowercase = Digits = 0
for char in password:
    if 'A'<= char <= 'Z':
        Uppercase += 1
    elif 'a' <= char <= 'z':
        Lowercase += 1
    elif '0' <= char <= '9':
        Digits += 1
print(f"Uppercase = {Uppercase}")
print(f"Lowercase = {Lowercase}")
print(f"Digits = {Digits}")
if Uppercase and Lowercase and Digits >= 1:
    print("Strong Password")
else:
    print("Weak Password")

# WAREHOUSE STOCK ALERT
"""
Ignore products with stock 0. Count how many products need restocking (stock less than 10).
"""
stock = [25,5,0,18,3,40]
restock = 0 
for product in stock:
    if product==0:
        continue
    elif product<10:
        restock+=1
print(f"Products to Restock = {restock}")

# BUS SEAT OCCUPANCY
"""
1 means occupied and 0 means empty. Calculate occupied seats, empty seats, and occupancy percentage.
"""
seats = [1,0,1,1,0,0,1]
ind = 0
Occupied, Empty = 0,0
while ind<len(seats):
    if seats[ind] == 1:
        Occupied += 1
    else:
        Empty+=1
    ind+=1
print(f"Occupied = {Occupied}")
print(f"Empty = {Empty}")
print(f"Occupancy = {round((Occupied/len(seats))*100,2)}%")

#CONSECUTIVE FAILURES DETECTOR
"""
Stop processing when 3 consecutive failures occur.
"""
results = ['P','P','F','F','F','P']
count = 0
for result in results:
    if result=='F':
        count+=1
    else:
        count = 0
    if count==3:
        print("3 COnsecutive Failures found")
        break

# PRODUCT RETURN ANALYSIS
"""
Positive values are sales and negative values are returns. Calculate total sales, 
total returns, and net revenue.
"""
orders = [500,800,-500,1000,-800]
sales, returns = 0,0
for order in orders:
    if order>0:
        sales+=order
    else:
        returns += abs(order)
print(f"Sales = {sales}")
print(f"Returns = {returns}")
print(f"Net Revenue = {sales-returns}")

# MOBILE DATA USAGE TRACKER
"""
Process usage day by day and stop when the limit is exceeded.
"""
Usage = [450,600,700,550]
limit = 2000
ind = 0
used = 0
while ind < len(Usage):
    used += Usage[ind]
    if used>2000:
        print(f"Limit Exceeded! on Day {ind + 1}")
        break
    ind +=1
print(f"Used = {used}")

# VOTING MACHINE RESULT
"""
Count votes for each candidate and find the winner.
"""
votes = ['A','B','A','C','A','B','A']
a,b,c = 0,0,0
for vote in votes:
    if vote=='A':
        a+=1
    elif vote == 'B':
        b+=1
    else:
        c+=1
if a>b and a>c:
    print("Winner = A")
elif b>a and b>c:
    print("Winner = B")
else:
    print("Winner = C")

# PARKING SLOT MANAGEMENT
"""
Count Cars, Bikes, and Trucks.
"""
vehicles = ['C','B','C','T','B','C']
bike,car,truck = 0,0,0
for vehicle in vehicles:
    if vehicle == 'B':
        bike+=1
    elif vehicle == 'C':
        car+=1
    else:
        truck +=1
print(f"Cars = {car}")
print(f"Bikes = {bike}")
print(f"Trucks = {truck}")

# NUMBER SEQUENCE ANALYSER
numbers = [12,5,8,21,14,7]
even,odd = 0,0
large= numbers[0]
small = numbers[0]
for number in numbers:
    if number>large:
        large = number
    elif number<small:
        small = number
    elif number % 2 ==0:
        even +=1
    else:
        odd+=1
print(f"Even = {even}")
print(f"Odd = {odd}")
print(f"Largest = {large}")
print(f"Smallest = {small}")