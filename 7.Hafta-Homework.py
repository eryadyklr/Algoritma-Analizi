a = [[1, 0], [0, 1]]
b = [[5, 2], [1, 3]]

def carpim(liste, sayi):
    vektor=[]
    gecici=[]
    for i in liste:
        for j in range(len(i)):
            gecici.append((i[j]*sayi))
        vektor.append(gecici)
        gecici=[]
    return vektor
    
def kartezyen_carpim(a,b):
    matris=[]
    gecici=[]
    x=0
    for i in a:
        for j in b:
            for k in range(len(j)):
                gecici.append(i[x])
                gecici.append(j[k])
                matris.append(gecici)
                gecici=[]
            x=x+1
        x=0
    print(matris)
    
def dis_carpim(a,b):
    matris=[]
    gecici=[]
    for i in range(len(a)):
        for j in range(len(a[0])):
            gecici.append(carpim(b,a[i][j]))
        matris.append(gecici)
        gecici = []
    print(matris)
    
def ic_carpim(a,b):
    result=[]
    toplam=0
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                toplam += a[i][k] * b[k][j]
            result.append(toplam)
            toplam=0
    print(result)

ic_carpim(a,b)
#[5, 2, 1, 3]

dis_carpim(a,b)
#[[[[5, 2], [1, 3]], [[0, 0], [0, 0]]], [[[0, 0], [0, 0]], [[5, 2], [1, 3]]]]

kartezyen_carpim(a,b)
#[[1, 5], [1, 2], [0, 1], [0, 3], [0, 5], [0, 2], [1, 1], [1, 3]]
