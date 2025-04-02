
dict1= {x:x**2 for x in range (1, 11)}
print(dict1.values())
# for keys in dict1:
#     #clsprint(keys)
#     print(dict1.values())
    
# for items in range (1,1001) :
#     print(dict1.items())
#     print(items)

for key, value in dict1.items():
    print(f"{key,value}")

dict1.pop(5)
print(dict1)


dict1.popitem()
print(dict1)


dict1.update({10:121})
print(dict1)

dict1.update({5:25})
print(dict1)

#clear', 'copy', 'fromkeys', 'get', 'setdefault'

dict2=dict1.copy()
print(dict2)

print(dict2.setdefault(12))
print(dict2)
print(dict2.get(13))
print(dict2)

dict3=dict2.fromkeys({3},20)
print(dict3)

dict2.clear()
print(dict2)

del dict1[1]
print(dict1)