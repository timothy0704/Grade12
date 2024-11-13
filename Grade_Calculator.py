score = float(input("Enter your score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 0 <= score <= 69:
    print("Grade: D")
else:
    print("Grade: Below LD (Invalid or out-of-range score)")
