def determinant(mat):
    n = len(mat)
    if (n > 2):
        i = 1
        t = 0
        toplam = 0
        while t <= n-1:
            d = {}
            t1 = 1
            while t1 <= n-1:
                m = 0
                d[t1] = []
                while m <= n-1:
                    if (m == t):
                        u=0
                    else:
                        d[t1].append(mat[t1][m])
                    m += 1
                t1 += 1
            mat1 = [d[x] for x in d]
            toplam = toplam + i*(mat[0][t])*(det(mat1))
            i = i*(-1)
            t += 1
        return toplam
    else:
        return (mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0])

matris = [[5,3,2],[1,2,1],[1,2,3]]
determinant(matris)
