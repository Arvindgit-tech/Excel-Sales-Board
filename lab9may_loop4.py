
# for i in range(1,52):
#     pass

n= int(input("enter the number "))
for i in range (1, 101):
    if i%5==0:
        continue
    print(f' {n}*{i}={n*i}')
    