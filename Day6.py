# Student Grade Checker
"""
 A school wants to automatically assign grades based on student marks. 
 A→90 and above, B→75-89, C→60-74, D→35-59, Fail→Below 35.
"""
def studentGradeChecker():
    marks = int(input("Enter the marks obtained: "))

    if marks >= 90:
        print("Grade : A")
    elif marks >= 75:
        print("Grade : B")
    elif marks >= 60:
        print("Grade : C")
    elif marks >= 35:
        print("Grade : D")
    else:
        print("Fail")

studentGradeChecker()

# ATM PIN Verification
"""
Allow only 3 PIN attempts. Correct PIN: Login Successful. After 3 wrong attempts: Card Blocked.
"""
def atmPinVerification():
    pin=9866
    attempts=1
    while attempts <=3:
        userpin=int(input("Enter the pin:"))
        if userpin==pin:
            print("Login successfull")
            break
        else:
            print("Wrong password!Please enter the correct password")
            attempts+=1
    if attempts==4:
        print("Card Blocked")
        
atmPinVerification()

# Multiplication Tables
"""
Print multiplication table up to 10.
"""
def multiplicationTables():
    num = int(input("Enter a number: "))
    for i in range(1, 51):
        print(num, "x", i, "=", num * i)
        
multiplicationTables()

# Number Guess Validation
"""
Keep asking until number is between 1 and 100.
"""
def numberValidation():
    while True:
        num = int(input("Enter a number: "))
        if num >= 1 and num <= 100:
            print("Valid Number")
            break
        else:
            print("Invalid Number")
            
numberValidation()

# Restaurant Ordering System 
"""
Menu: 1.Pizza 2.Burger 3.Sandwich 4.Exit
Keep ordering until Exit. Display Total Items Ordered = X.
"""
count = 0
while True:
    print("\n1. Pizza")
    print("2. Burger")
    print("3. Sandwich")
    print("4. Exit")
    order  = int(input("Enter your choice: "))
    if order == 1:
        print("Pizza Ordered")
        count += 1
    elif order  == 2:
        print("Burger Ordered")
        count += 1
    elif order  == 3:
        print("Sandwich Ordered")
        count += 1
    elif order  == 4:
        print("Total Items Ordered =", count)
        break
    else:
        print("Invalid order!please enter  a valid order")

# Cinema Seat Booking
"""
Theatre has 5 rows and 6 seats. If seat already booked print Already Booked
else Seat Booked Successfully. Continue until 5 seats booked.
"""
seats = []
for i in range(5):
    row = []
    for j in range(6):
        row.append(0)      
    seats.append(row)
booked = 0
while booked < 5:
    row = int(input("Enter Row (1-5): "))
    seat = int(input("Enter Seat (1-6): "))
    if row < 1 or row > 5 or seat < 1 or seat > 6:
        print("Invalid Seat")
        continue
    if seats[row-1][seat-1] == 1:
        print("Already Booked")
    else:
        seats[row-1][seat-1] = 1
        booked += 1
        print("Seat Booked Successfully")
print("Booking Closed (5 seats booked)")

# Employee Attendance Report
"""
3 departments, 5 employees each. Attendance: 1=Present, 0=Absent. Display department-wise Present and Absent counts.
"""
departments = 3
employees = 5
for i in range(1, departments + 1):
    present = 0
    absent = 0
    print("\nDepartment", i)
    for j in range(1, employees + 1):
        attendance = int(input("Employee " + str(j) + " (1=Present, 0=Absent): "))
        if attendance == 1:
            present += 1
        else:
            absent += 1
    print("Present =", present)
    print("Absent =", absent)

# Bank Transaction Simulator 
"""
Menu: Deposit, Withdraw, Balance, Mini Statement, Exit. 
Rules: Login with PIN (3 attempts), continue until Exit, withdrawal cannot exceed balance, 
maintain transaction count, display total deposits and withdrawals.
"""
def bankTransactionSimulator():
    pin = 1234
    balance = 5000
    depositTotal = 0
    withdrawTotal = 0
    transactionCount = 0
    attempts = 3
    while attempts > 0:
        enteredPin = int(input("Enter PIN: "))
        if enteredPin == pin:
            print("Login Successful")
            break
        else:
            attempts -= 1
            print("Incorrect PIN")
    if attempts == 0:
        print("Too many attempts. Account Locked.")
        return
    while True:
        print()
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Mini Statement")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            amount = int(input("Enter deposit amount: "))
            balance += amount
            depositTotal += amount
            transactionCount += 1
            print("Amount Deposited")
        elif choice == 2:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance -= amount
                withdrawTotal += amount
                transactionCount += 1
                print("Amount Withdrawn")
            else:
                print("Insufficient Balance")
        elif choice == 3:
            print("Current Balance =", balance)
        elif choice == 4:
            print()
            print("Balance =", balance)
            print("Total Deposits =", depositTotal)
            print("Total Withdrawals =", withdrawTotal)
            print("Total Transactions =", transactionCount)
        elif choice == 5:
            print("Thank You!")
            break
        else:
            print("Invalid Choice")
bankTransactionSimulator()