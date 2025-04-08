# Classify a person’s age group: Child (< 13), Teenager (13-19), Adult (20
# 59), Senior (60+)

# age =int(input("enter your age"))
# if (age<13):
#     print("Child")
# elif age > 13 and age< 19:
#     print("teenager")
# elif age>= 19 and age <=59:
#     print("Adult")
# else :
#     print("Senior")

# Movie tickets are priced based on age: $ 12 for adults (18 and
#  over), $ 8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("age"))
Day = input("Day")
if Day == "Wed":
    if age <18:
        print('Ticket_Price $6')
    elif age >18:
        print('Ticket_Price $10')
elif Day == "Sun" and "Mon" and "Tue" and "Thurs" and "Fri" and "Sat":
    if age <18:
     print('Ticket_Price $8')
    elif age >18:
     print('Ticket_Price $12')
else:
   print ("Plese enter valid Day")



