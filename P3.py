#Project3

dataNama = []
r = True

while(r == True) :
    nama = input('Masukkan nama :')
    dataNama.append(nama)

    lanjut = input('Apakah ingin menginput nama lagi ? (y/n)')

    if(lanjut == 'y') :
        r = True

    elif(lanjut == 'n') :
        r = False

    else :
        print('Input tidak valid')
        break

print()
dataNama.sort()

for r in range(len(dataNama)) :
    print(dataNama[r], '(', len(dataNama[r]), 'karakter )')
