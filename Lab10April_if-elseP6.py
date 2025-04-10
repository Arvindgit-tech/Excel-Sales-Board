# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color.
#  (e.g., Banana: Green- Unripe, Yellow- Ripe, Brown- Overripe)


fruit = input("enter Fruit name ").upper()
color=input("enter the color").upper()
print(color, fruit)
if fruit== "BANANA":
    if color== "GREEN":
        print("Unripe")
    elif color== "YELLOW":
        print("Ripe")
    elif color == "BROWN":
        print("overripe")
    else :
        print("Enter the valid color ")
else:
    print("Please enter fruit as BANANA")