# Problem: Determine if a year is a leap year. (Leap years are divisible by
#  4, but not by 100 unless also divisible by 400)

a= int(input("enter the year  "))
if (a%4 == 0 and a%100 !=0) or (a%400 == 0):    # != is not
    print("This is leap year")
else:
    print("This is not a leap year")

