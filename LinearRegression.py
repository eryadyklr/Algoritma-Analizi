import numpy as np
import matplotlib.pyplot as plt

def ortalama(gelen_sayilar):
    miktar = len(gelen_sayilar)
    toplam = 0
    for i in gelen_sayilar:
        toplam += i
    return toplam/miktar

def linearRegression(list1, list2):
    n = 5
    ort_x = ortalama(list1)
    ort_y = ortalama(list2)
    xy = np.sum(list2*list1 - n*ort_y*ort_x)
    xx = np.sum(list1*list1 - n*ort_x*ort_x)
    a = xy / xx
    b = ort_y - a*ort_x
    return(a, b)

def cizdir(list1, list2, linearReturn):
    plt.scatter(list1, list2, color = "m", marker = "o", s = 30)
    y_pred = linearReturn[1] + linearReturn[0]*list1
    plt.plot(list1, y_pred, color = "g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

a = np.array([3, 3, 2, 2, 1])
b = np.array([3, 5, 1, 4, 2])
linear = linearRegression(a, b)
print("Sonuç:  y = a * x + b\n\ty =", linear[0], "* x +", linear[1])
cizdir(a, b, linear)
