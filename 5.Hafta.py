from random import randint
def create_A_vector(size):
    my_vector=[]
    for i in range(size):
        my_vector.append(randint(0,9))
    return my_vector

def vector_inner_product(v1,v2):
    if(len(v1) != len(v2)):
        print("vektörler eşit değil")
        return 
    result = 0
    for i in range(len(v1)):
        result = result+v1[i]*v2[i]
    return result
    
def create_A_matrix(m,n):
    my_matrix=[]
    for i in range(m):
        my_matrix.append(create_A_vector(n))
    return my_matrix

def matrix_multiplication(a,b):
    m=len(a)
    n=len(a[0])
    p=len(b[0])
    my_matrix_sonuc = create_A_matrix(m,p)
    for i in range(m):
        for j in range(p):
            vector_1=a[i]
            vector_2=[i[j] for i in b]
            my_matrix_sonuc[i][j]=vector_inner_product(vector_1,vector_2)
    return my_matrix_sonuc,m*n*p

my_vector_1=create_A_vector(10)
my_vector_2=create_A_vector(10)

vector_product=vector_inner_product(my_vector_1,my_vector_2)

my_matrix_1=create_A_matrix(3,5)
my_matrix_2=create_A_matrix(5,10)
c=matrix_multiplication(my_matrix_1,my_matrix_2)
c
#([[139, 117, 108, 128, 120, 67, 74, 82, 117, 84],
  [132, 99, 102, 104, 115, 55, 82, 75, 104, 88],
  [22, 24, 30, 26, 27, 20, 13, 25, 16, 13]],
 150)

a_1=create_A_matrix(1,10)
a_2=create_A_matrix(10,1000)
a_3=create_A_matrix(1000,1)
a_4=create_A_matrix(1,5)
a_5=create_A_matrix(5,3)

islem_sayisi=0
r_1=matrix_multiplication(a_1,a_2)
islem_sayisi=islem_sayisi+r_1[1]

r_1=matrix_multiplication(r_1[0],a_3)
islem_sayisi=islem_sayisi+r_1[1]

r_1=matrix_multiplication(r_1[0],a_4)
islem_sayisi=islem_sayisi+r_1[1]

r_1=matrix_multiplication(r_1[0],a_5)
islem_sayisi=islem_sayisi+r_1[1]

print(r_1,"toplam islem sayisi:",islem_sayisi)
#([[114523605, 110281990, 79742362]], 15) toplam islem sayisi: 11020
