Text= "Hello" \
" World"

print(Text.capitalize())
print(Text.title())
print(Text.casefold())

Text2 = "RAVI MALIK"

print(Text2.casefold())
print(Text2.lower())

print(Text2.center(30,'+'))

print(Text2.rjust(30, '='))

print(Text2.ljust(30, '='))

print(Text2.endswith("K"))
print(Text2.startswith("K"))
print(Text2.find("Z")) 

"""find() will return -1 if the substring is not found.
index() will raise a ValueError if the substring is not found."""
try:
    print(Text2.index("Z"))
except:
    print("handling error")
print(Text2.count("I"))

print("My Name is {0} and age is {1}".format ("Arvind", 32))

Name = "Arvind"
Age= 32
print(f"My Name is {Name} and I am {Age} old")

print(" ".join(["arvind", "Ravi", "Malik"]))
print(Text2.partition("A"))
print(Text2.rpartition("A"))

print(Text2.replace("MALIK", "Singh"))

print(dir(str))

print(Text2.swapcase())
print(Text.swapcase())
print(Text.strip())
print(Text.strip())
print(Text.split())



Name= "Ravi Malik"
byte_date= Name.encode()
print(byte_date)