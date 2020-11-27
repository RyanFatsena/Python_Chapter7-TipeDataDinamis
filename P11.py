#Project11

fruit = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }

def printDataFruit(databaseFruit):
    print('Data fruit:')
    for i, j in databaseFruit.items():
        print('- {0} (Harga Rp{1} / kg)'.format(i,j))
        print('')

def checkOut(databaseFruit,namaFruit,banyakKilo):
    hargaFruit = databaseFruit.get(namaFruit)
    totalHarga = hargaFruit * banyakKilo
    return totalHarga

while True:
    print('Menu :\nA. Tambah Data Fruit\nB. Beli Fruit\nC. Keluar')
    opsi = None
    
    while opsi not in('A','B','C'):
        opsi = str(input("Pilihan Menu: "))
        
        if(opsi == 'A'):
            printDataFruit(fruit)
            namaFruitTambahan = str(input('Masukkan nama fruit yang ingin ditambahkan: '))

            if namaFruitTambahan in fruit.keys():
                print('Nama fruit telah terdaftar dalam database')

            else:
                while True:
                    try:
                        hargaFruitTambahan = int(input('Masukkan harga fruit (hanya angka): '))
                    except ValueError:
                        print('Mohon masukkan hanya angka')
                        continue
                    else:
                        break
                fruit[namaFruitTambahan] = hargaFruitTambahan
                print('{0} dengan harga {1} telah ditambahkan dalam database'.format(namaFruitTambahan,hargaFruitTambahan))
                print('')
                printDataFruit(fruit)
                
        elif(opsi == 'B'):
            printDataFruit(fruit)
            totalHarga = 0
            selesai = False
            
            while not(selesai):
                while True:
                    namaFruit = str(input('Nama fruit yang akan dibeli              : '))
                    if(not(namaFruit in fruit.keys())):
                        print('Nama fruit tidak ditemukan')
                        continue
                    else:
                        break
                    
                while True:
                    try:
                        perkilo = float(input('Berapa kg (jika desimal gunakan titik)   : '))
                    except ValueError:
                        print('Mohon masukkan hanya angka')
                        continue
                    else:
                        break
                    
                totalHarga = totalHarga + checkOut(fruit,namaFruit,perkilo)
                opsi = None
                
                while opsi not in('y','n'):
                    opsi = str(input('Beli lagi (y/n)?: '))
                    if(opsi == 'y'):
                        selesai = False
                        print('')
                        
                    elif(opsi == 'n'):
                        selesai = True
                        
                    else:
                        print('Mohon masukkan pilihan (y/n)')
                        
                print('------------------------------------------------')
                print('Total harga                              : {0}'.format(totalHarga))
                
        elif(opsi == 'C'):
            exit()
            
        else:
            print('Mohon masukkan pilihan yang tersedia')
