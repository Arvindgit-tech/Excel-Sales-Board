
# for i in range (1, 101):
#     print(i)

string1 = "ravi malik"
for x in string1:
    print(x)

count = 0
while count< 10:
    print(count)
    count= count+1

#  Problem: Given a list of numbers,count how many are positive.
#   numbers=[1,-2,3,-4,5,6,-7,-8,9,10]

numbers=[1,-2,3,-4,5,6,-7,-8,9,10, 12, 13, -12]
positive_counter=0
Negative_counter=0
for i in numbers:
    if (i>0):
        positive_counter+=1 
    elif (i<0):
        Negative_counter+=1

print("positive_Numbers" , positive_counter)
print("Negative_Numbers" , Negative_counter)


#  Problem: Calculate the sum of even numbers upto a given number n.
sum=0
n=50
even_number_count=0
for i in range (1, 51):
    if i%2==0:
        print(i)
        even_number_count+=1
        sum+=i
print("Sum", sum)

