
def Greet(Name):
    print(f"Hello {Name}")


Greet("Arvind")

def hello ():
    print("This is funtions welcome you")

hello()


def square (Num):
    return Num **2

print(square (8))


def greet(name = "Dear"):
 return f"good Morning {name}"
print(greet("Arvind"))


def add(*hii): # *args
 return sum (hii)
print(add(232,43435,4,54,5,4,6,56))


def factorial(n):
 if n == 1:
    return 1
 else:
    return n * factorial(n-1)
print(factorial(6))