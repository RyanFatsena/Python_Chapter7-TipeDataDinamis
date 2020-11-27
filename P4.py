#Project4

sayur = ['bayam','kangkung','wortel','selada']

def tambahSayur() :
    sayurTambahan = input('Masukkan nama sayur yang ingin ditambahkan :')
    sayur.append(sayurTambahan)
    return sayur

def hapusSayur() :
    sayurHapus = input('Masukkan nama sayur yang ingin dihapus :')
    sayur.append(sayurHapus)
    return sayur

def readSayur() :
    print(sayur)

print('Apa yang dilakukan program :')
print('A. Tambah data sayur')
print('B. Hapus data sayur')
print('C. Tampilkan data sayur')
print('D. Keluar')

r = True
while(r == True) :
    print()
    opsi = input('Pilihan Anda :')

    if(opsi == 'A' or opsi == 'a') :
        tambahSayur()

    elif(opsi == 'B' or opsi == 'b') :
        hapusSayur()

    elif(opsi == 'C' or opsi == 'c') :
        tambahSayur()

    elif(opsi == 'D') :
        break

    else :
        print('Input tidak valid')
        continue
