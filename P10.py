#Project10

fruit = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }

def checkOut(databaseFruit,namaFruit,banyakKilo):
    hargaFruit = databaseFruit.get(namaFruit)
    totalHarga = hargaFruit * banyakKilo
    return totalHarga

print('Daftar fruit dan harga :')

for x,y in fruit.items() :
    print('.', x, ':', y)

totalHarga = 0

selesai = False

while not(selesai):
    while True:
        namaFruit = str(input('Nama fruit yang akan dibeli                    : '))
        
        if(not(namaFruit in fruit.keys())):
            print('Nama fruit tidak ditemukan')
            continue
        
        else:
            break
        
    while True:  
        try:
            perkilo = float(input('Berapa Kg (jika bilangan desimal gunakan titik): '))

        except ValueError:
            print('Mohon masukkan dengan angka')
            continue
        
        else:
            break
        
    totalHarga = totalHarga + checkOut(fruit,namaFruit,perkilo)
    
    choice = None
    
    while choice not in('y','n'):
        choice = str(input('Beli lagi (y/n)? '))
        
        if(choice == 'y'):
            selesai = False
            print('')
            
        elif(choice == 'n'):
            selesai = True
            
        else:
            print('Mohon masukkan pilihan (y/n)')
            
print('--------------------------------------------------------')
print('Total harga                                    : {0}'.format(totalHarga))
