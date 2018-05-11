def altdizi(liste):
    if not liste:
        return [[]]
    birinciDahil = [[liste[0]] + k for k in altdizi(liste[1:])]
    birinciDahilDegil = altdizi(liste[1:])
    return birinciDahil + birinciDahilDegil
    
altdizi([0,1,2,3])
