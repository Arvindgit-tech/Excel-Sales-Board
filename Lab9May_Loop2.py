

# Problem: Print the multiplication table for a given number upto 10,but
#  skip the fifth iteration.

# n= int(input("enter the number "))
# for i in range (1, 11):
#     temp= n*i
#     if i!=5:
#         print(f' {n}*{i}={temp}')


# Problem: Print the multiplication table for a given number upto 10,but
# #  skip the fifth multiple iteration.

n= int(input("enter the number "))
for i in range (1, 101):
    temp= n*i
    if i%5!=0:
        print(f' {n}*{i}={temp}')

        