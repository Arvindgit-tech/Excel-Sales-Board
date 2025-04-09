# Problem: Assign a letter grade based on a student’s score: A (90-100), B
#  (80-89), C (70-79), D (60-69), F (below 60).

a = int(input("Enter the score of Student "))
if 90 <= a <= 100:
    print("Grade A")
elif 80 <= a <=89:
    print("Grade B")
elif 70 <= a <=79:
    print("Grade C")
elif 60 <= a <=69:
    print("Grade D")
elif a<=60:
    print("Pdne m kamjor h")
else:
    print("Please enter valid Score")
