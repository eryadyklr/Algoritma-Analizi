import sys

my_L_1 = []
size_1 = sys.getsizeof(my_L_1)
print("Başlangıç Boyutu: " , size_1)

for i in range(10):
    my_L_1.append(str(i+1) + ".test")
    if(size_1 != sys.getsizeof(my_L_1)):
        print("Dizi yer değiştirdi" , end=" ~~ ")
        size_1 = sys.getsizeof(my_L_1)
        print("Size: " , size_1)
print(my_L_1)
