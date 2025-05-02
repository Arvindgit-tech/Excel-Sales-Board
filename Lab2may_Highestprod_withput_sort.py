# Write a program to find the highest product of any two numbers in a LIST
# INPUT: [-1,2,4,-2,6,-5]
# Output : 24


def highest_product_function(numbers):
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    for n in numbers:
        if n > max1:
            max2=max1
            max1=n
            
            
        elif n> max2:
            max2=n

        if n < min1:
            min2=min1
            min1=n

        elif n< min2:
            min2=n

    return max(max1*max2, min1*min2)

List1= [-1,2,4,-2,6,-5]
highest_product_function(List1)
print(highest_product_function(List1))