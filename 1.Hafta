import time
millis_1 = int(round(time.time()))
print(millis_1)
time.sleep(5)
millis_2 = int(round(time.time()))
print(millis_2)
print(millis_2 - millis_1)

def fibRec(n):
    if(n<2):
        return n
    else:
        return fibRec(n-1)+fibRec(n-2)
        
fibRec(0),fibRec(1),fibRec(2),fibRec(3),fibRec(4)

n=40
time_1 = int(round(time.time()))
fibRec(n)
time_2 = int(round(time.time()))
print(n, "için geçen süre:", time_2-time_1,"saniye")

for n in range(41):
    time_1 = int(round(time.time()))
    fibRec(n)
    time_2 = int(round(time.time()))
    print(n, "için geçen süre:", time_2-time_1,"saniye")
    
def fib(n):
    a, b = 0, 1
    while n>0:
        a, b = b, a+b
        n -= 1
    return a
    
print(fib(0), fib(1), fib(2), fib(3), fib(4))

n=1000000
time_3 = int(round(time.time()))
fib(n)
time_4 = int(round(time.time()))
print(n, "için geçen süre:", time_4-time_3,"saniye")

import matplotlib.pyplot as plt
for n in range(41):
    time_1 = int(round(time.time()))
    fib(n) #loop
    time_2 = int(round(time.time()))
    print(n, "için geçen süre (loop):", time_2-time_1, "saniye")
    time_A = time_2-time_1
    time_3 = int(round(time.time()))
    fibRec(n) #np
    time_4 = int(round(time.time()))
    print(n, "için geçen süre (np):", time_4-time_3, "saniye")
    time_B = time_4-time_3
    plt.plot([n,time_A])
    plt.plot([n,time_B])
    plt.xlabel('Blue: loop values\nOrange: np values')
    plt.ylabel('Saniye')
    plt.show()
