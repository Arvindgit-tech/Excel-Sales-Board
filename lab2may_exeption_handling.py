try:
 num = int(input("enter a number: "))
 result = 10/num
except ZeroDivisionError:
 print("you can't divide your value from zero!")
except ValueError:
 print("check your value!")
except TypeError:
 print("check your type again!")
else:
 print(result)