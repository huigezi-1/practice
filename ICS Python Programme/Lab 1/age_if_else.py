age = int(input())

if age >= 21:
    print("You are eligible to vote.")
elif 13 <=age < 21:
    print("You are a teenager.")
elif 0 < age <13:
    print("You are a child.")
else:
    print("Invalid age entered.")
