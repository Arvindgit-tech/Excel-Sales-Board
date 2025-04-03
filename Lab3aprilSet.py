# Set is an unoerdered and removed duplicate entries. (only unique)
My_Set= {1,21,23,42,4,35,54,4,46,21,7,77}
print(My_Set)

empty_set = set((10,20,60))
print(type(empty_set))
print(empty_set)

new_empty = set()
print(new_empty)

new_empty.add(10) #will add only one value at a time
print(new_empty)

Mix_set = {10,10,10,20,20,30,40,40}
print(Mix_set)

Mix_set.remove(10)   #remove One value only
print(Mix_set)


Mix_set.pop()
print(Mix_set)

Mix_set.pop() #delete from starts
print(Mix_set)

New_Set = {"age", 20, 30}
print(New_Set)
New_Set.pop()
print(New_Set)
a= New_Set.pop()
print(a)

New_Set.discard(50)
print(New_Set)

