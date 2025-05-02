dict0={"Arvind":7906}
dict1={"Ravi":8439}
print(dict0)
print(type(dict))

empty_dict={}
print(empty_dict)

dict2 = dict(name="pravesh",age = 35)
print(dict2)
print(type(dict2))

dict2['name']="Ramesh"
print(dict2)


keys = ["name","age","city"]
new_data = dict.fromkeys(keys,"Noida")
print(new_data)

print(dict2.items())
print(dict2.values())
print(dict2.keys())

Square={x:x**2 for x in range (1,11)}
print(Square)

#for keys in Squre:   print(keys)

for Square in Square.values():
    print(Square)