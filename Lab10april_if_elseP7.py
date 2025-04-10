# Problem: Suggest an activity based on the weather (e.g., Sunny- Go for a
#  walk, Rainy- Read a book, Snowy- Build a snowman).

W = input("enter the weather").capitalize()
if W == "Sunny":
    print("Go for a Walk ")
elif W == "Rainy":
    print("Read a Book")
elif W == "Snowy":
    print("Build a Snowman")
else:
    print("Invalid")