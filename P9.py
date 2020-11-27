#Project9

fruit = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }

def jumlahFruit():
    jumlah =int(input('Berapa Kg yang dibeli  :'))

    print('-------------------------------')
    print('Total Harga            :',fruit.get(namaFruit,0)*jumlah)

namaFruit = input('Nama fruit yang dibeli :')

try:
    if(namaFruit in fruit.keys()):
        jumlahFruit()

    else:
        print('Maaf,nama fruit yang anda masukkkan tidak ada')

except ValueError:
    print('Silakan jumlah fruit dengan benar')
    jumlahFruit()
