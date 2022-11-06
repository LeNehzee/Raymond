gender = input("What is your gender? ")
age = int(input("What is your age? "))

if gender.upper() == "FEMALE" and 20 <= age <= 60:
    print("You can work anywhere")
elif gender.upper() == "MALE" and 20 <= age <= 40:
    print("You can only work in urban area")
elif gender.upper() == "MALE" and 41 <= age <= 60:
    print("You can work anywhere")
else:
    print("ERROR")