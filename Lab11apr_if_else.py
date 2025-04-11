# Problem: Check if a password is “Weak”, “Medium”, or “Strong”. 
# Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("enter the value ")
password_length = len(password)
print(password_length)
if password_length < 6:
    print("Weak")
elif password_length <=10:
    print("Medium")
elif password_length >10:
    print("Strong")
