List1= [-1,-2,-4,-2,6,-5]

max1=max(List1)
print(max1)

List1.remove(max1)

max2=max(List1)
print(max2)

min1=min(List1)
List1.remove(min1)

min2= min(List1)

min_prod= min1*min2
max_prod= max1*max2

print(max(min_prod, max_prod))
