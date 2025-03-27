#List------> Mutable (can be change)

list= ["Apple", "Mango", "Guvava", "PineApple", "Kiwi"]
print(list)
print(list[1])
try:
    print(list[5])
except:
    print("I know that this is Index error I will handle it later")
# exception handling using Try/Except Block
# if I having a error in code where I know that but I want to run my next code without taking care of it.
 

list1= ["Apple", "Mango", "Guvava", ["PineApple", "Kiwi"], 80, 90]
print(list1[3])
print(list1[4])
print(list1[3][1]) #in list we have to use indexing sepratly if we have list inside list.
print(list1[0:3])

mylist= ["Arvind", [89, 60, [70,80]],10,20,30]
#print(mylist[3][2][0]) #there is 2 element in this list so cant print 3.

mylist[1][2].remove(70)   #first changes in the list then print
print(mylist)

mylist.pop(-2)    #remove last value by default othervise remove a/c to index.
print(mylist)
mylist.pop(1)
print(mylist)

#del mylist(1)
print(mylist)


Fruits= [1,3,4,5,2,6,7]
print(len(Fruits))
Fruits.sort()
print(Fruits)
Fruits.reverse()
print(Fruits)
Fruits.insert(8,10)  #first index  then Value whatever we want to put.
print(Fruits)
Fruits.extend(mylist)
print(Fruits)



empty_list=[]
print(empty_list)
empty_list.append("Noida")
print(empty_list)
#print(dir(list))

