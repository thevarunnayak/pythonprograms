# Program to calculate grade of a student

score = float(input("Enter the score: "))

if 90 <= score <= 100:
    print("Grade O")
elif 80 <= score < 90:
    print("Grade A+")
elif 70 <= score < 80:
    print("Grade A")
elif 60 <= score < 70:
    print("Grade B+")
elif 50 <= score < 60:
    print("Grade B")
elif 50 > score >= 0:
    print("No Grade")
else:
    print("Invalid Score")
