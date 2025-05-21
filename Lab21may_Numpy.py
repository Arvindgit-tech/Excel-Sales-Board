import numpy as np

two_d = np.array([[10,20,30],[60,50,90]])
print(two_d)

print(two_d.shape)

a3 = np.arange(8).reshape(2,2,2)
print(a3)

print(a3.size)
print(a3.itemsize)
print(a3.dtype)
print("--------------------")
k1 = np.random.random((3,5))
k1 = np.round(k1*100)
print(k1)

k2= np.random.randint(1, 6, size=(3, 3))  # 6 is exclusive, so this includes 1 to 5
print(k2)

print(np.std(k1))
print(np.std(k2))