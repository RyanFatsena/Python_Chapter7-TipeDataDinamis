#Project5

def kuadrat(bil) :
    
    bilSquare = []

    for r in range(len(bil)) :

        perkalian = bil[r] * bil[r]
        bilSquare.append(perkalian)
        
    return bilSquare

databil = [2, 4, 5, 6, 12]
hasil = kuadrat(databil)
print (hasil)
