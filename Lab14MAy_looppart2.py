
# Problem: Compute the factorial of a number using a while loop.

num = 5
# print(f"your number is {num} ",end="")
factorial=1

while (num >0):
        factorial*=num   #factorial = factorial*number
      
        num-=1
        if num==1:
            
                print(f" and Result is {factorial}")