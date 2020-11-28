print('='*25,'PRAKTIKUM 8','='*25)

#1
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print('List a\n',a)
print('List b\n',b)
print()

#2
a.insert(3,10)
b.insert(2,15)
print('List a setelah di sisipkan nilai 10 ke indeks 3\n',a)
print('List b setelah di sisipkan nilai 15 ke indeks 2\n',b)
print()

#3
a.append(4)
b.append(8)
print('List a setelah di sisipkan nilai 4 ke indeks terakhir\n',a)
print('List b setelah di sisipkan nilai 8 ke indeks terakhir\n',b)
print()

#4
a.sort()
b.sort()
print('List a setelah sorting secara ascending\n',a)
print('List a setelah sorting secara ascending\n',b)
print()

#5
c = a[0:8]
d = b[2:10]
print('List c atau sublist dari a(indeks 0-7)\n',c)
print('List d atau sublist dari b(indeks 2-9)\n',d)
print()

#6
e = []
for i in range(len(c)) :
    element = c[i] + d[i]
    e.append(element)
print('List e atau penjumlahan list c dan d\n',e)
print()

#7
dataTuple = tuple(e)
print('List e ke dalam tuple\n',dataTuple)
print()

#8
minTuple = min(dataTuple)
maxTuple = max(dataTuple)
sumTuple = sum(dataTuple)
print('Hasil min dari tuple e\n',minTuple)
print('Hasil max dari tuple e\n',maxTuple)
print('Hasil sum dari tuple e\n',sumTuple)
print()

#9
myString = "python adalah bahasa pemrograman yang menyenangkan"
print('Variable myString\n',myString)
print()

#10
charPenyusun = set(myString)
print('Karakter huruf myString\n',charPenyusun)
print()

#11
listPenyusun = list(charPenyusun)
listPenyusun.sort()
print('Urutan huruf alfabet myString setelah di sorting\n',listPenyusun)

