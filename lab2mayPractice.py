
# Write a program to find the highest product of any two numbers in a LIST
# INPUT: [-1,2,4,-2,6,-5]
# Output : 24

List1 = [-1,2,4,-2,6,-5]
List1.sort()
print(List1)
H_Product1= List1[0]*List1[1]
print(H_Product1)
H_Product2= List1[-1]*List1[-2]
print(H_Product2)

if H_Product1 > H_Product2:
    print("Highest Product is", H_Product1)
else:
     print("Highest Product is", H_Product2)



H_Product= (List1[0]*List1[1], List1[-1]*List1[-2])
print(H_Product)
print(max(H_Product))