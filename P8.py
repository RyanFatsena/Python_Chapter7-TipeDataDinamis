#Project8

fruit = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }

def rata2HargaFruit(fruit):
    totalHarga = 0
    jumlah = 0

    for r,y in buah.items():
        totalHarga += y
        jumlah += 1

    rata2 = totalHarga/jumlah
    return rata2

def ratarataHargaFruit(fruit):
    harga = list(fruit.values())
    rata = sum(harga)/len(harga)
    return rata

a = ratarataHargaFruit(fruit)
b = ratarataHargaFruit(fruit)

print('Rata-rata harga fruit adalah :',a)
print('Rata-rata harga fruit adalah :',b)
