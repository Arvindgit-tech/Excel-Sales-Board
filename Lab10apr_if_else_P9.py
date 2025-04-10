# Problem: Customize a coffee order: “Small”, “Medium”, or “Large” with
#  an option for “Extra shot” of espresso.

Coffee_Type = input("enter the type").capitalize()

Size = input("enter the size").capitalize()

if Coffee_Type == "Normal":
    if Size== "Small":
        print(f"your {Coffee_Type} coffee with {Size} is ready ")
    elif Size == 'Medium':
        print(f"your {Coffee_Type} coffee with {Size} is ready ")
    elif Size == "Large":
        print(f"your {Coffee_Type} coffee with {Size} is ready ")
elif  Coffee_Type == "Extra shot":
    if Size== "Small":
        print(f"your {Coffee_Type} coffee with {Size} is ready ")
    elif Size == 'Medium':
        print(f"your {Coffee_Type} coffee with {Size} is ready ")
    elif Size == "Large":
        print(f"your {Coffee_Type} coffee with {Size} is ready ")
else:
    print("Please select either Normal or Extra shot ")
    