#Project9

fruit = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }

def jumlahFruit():
    jumlah =int(input('Berapa Kg yang dibeli  :'))

    print('-------------------------------')
    print('Total Harga            :',fruit.get(namaFruit,0)*jumlah)

print('Daftar fruit dan harga :')

for x,y in fruit.items() :
    print('.', x, ':', y)

while True :
    
    namaFruit = input('Nama fruit yang dibeli :')
    
    if(namaFruit not in fruit.keys()) :
        print('Mohon maaf, fruit yang anda masukkan tidak ada')
        continue

    else :
        while True :
            try :
                jumlahFruit()
                break
            
            except ValueError :
                continue
        break
