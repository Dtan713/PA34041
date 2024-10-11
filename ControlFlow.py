# 1. Check if x is less than 10
x = 7
if x < 10:
    print("Less than 10")
x = 15  # Changing x to 15, no output expected

# 2. Check if x is less than or greater than 10
x = 7
if x < 10:
    print("Less than 10")
else:
    print("Greater than 10")
x = 15  # Changing x to 15, no output expected

# 3. Check the range of x with if...elif...else
x = 15
if x < 10:
    print("Less than 10")
elif 10 <= x < 20:
    print("Between 10 and 20")
else:
    print("Greater than or equal to 20")
x = 50  # Changing x to 50, no output expected

# 4. Check if x is in range 10-20
x = 15
if x < 10 or x > 20:
    print("Out of range")
else:
    print("In range")
x = 5  # Changing x to 5, expected output: "Out of range"

# 5. Determine letter grade based on user input
score = int(input("\nEnter your score (0-100): "))
if score < 0 or score > 100:
    print("Score out of range")
elif 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# 6. Calculate tax based on filing status and income
filing_status = input("\nEnter your filing status (Single, Married Filing Jointly, Married Filing Separately, Head of Household): ")
income = float(input("Enter your income: "))

tax = 0.0

if filing_status == "Single":
    if income <= 9875:
        tax = income * 0.10
    elif income <= 40125:
        tax = 987.50 + (income - 9875) * 0.12
    elif income <= 85525:
        tax = 4617.50 + (income - 40125) * 0.22
    else:
        tax = 14605.50 + (income - 85525) * 0.24

elif filing_status == "Married Filing Jointly":
    if income <= 19750:
        tax = income * 0.10
    elif income <= 80250:
        tax = 1975 + (income - 19750) * 0.12
    elif income <= 171050:
        tax = 9235 + (income - 80250) * 0.22
    else:
        tax = 29211 + (income - 171050) * 0.24

elif filing_status == "Married Filing Separately":
    if income <= 9875:
        tax = income * 0.10
    elif income <= 40125:
        tax = 987.50 + (income - 9875) * 0.12
    elif income <= 85525:
        tax = 4617.50 + (income - 40125) * 0.22
    else:
        tax = 14605.50 + (income - 85525) * 0.24

elif filing_status == "Head of Household":
    if income <= 14100:
        tax = income * 0.10
    elif income <= 53700:
        tax = 1410 + (income - 14100) * 0.12
    elif income <= 85500:
        tax = 6090 + (income - 53700) * 0.22
    else:
        tax = 13490 + (income - 85500) * 0.24

else:
    print("Invalid filing status.")

print(f"Your estimated tax: ${tax:.2f}")
