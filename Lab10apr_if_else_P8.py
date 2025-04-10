# Problem: Choose a mode of transportation based on the distance (e.g., <3
#  km: Walk, 3-15 km: Bike, >15 km: Car).

Dis = int(input("enter the Dis"))
T1 = "Walk"
T2 = "Bike"
T3 = "Car"
if Dis < 3 : 
    print(T1)
elif 3 <= Dis <= 15:
    print(T2)
else:
    print(T3)
