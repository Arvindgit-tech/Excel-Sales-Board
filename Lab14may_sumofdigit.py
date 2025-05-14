
## Sum of Digits

num= int(input("enter your number " ))
Mode=0
while num>0:
    Mode= num%10+Mode
    num= num//10
print(Mode)
