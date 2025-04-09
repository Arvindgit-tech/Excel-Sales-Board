# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color.
#  (e.g., Banana: Green- Unripe, Yellow- Ripe, Brown- Overripe)

color = input(" Enter the color ").upper()
if color== "GREEN":
    print("Unripe")
elif color== "YELLOW":
    print("Ripe")
elif color == "BROWN":
    print("Overripe")
else:
    print("Please enter the color among GREEN, YELLOW , BROWN")
