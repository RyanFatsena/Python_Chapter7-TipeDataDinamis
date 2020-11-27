print('='*25,'PRAKTIKUM 8','='*25)

#1
a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

#2
a.insert(3,10)
b.insert(2,15)

#3
a.append(4)
b.append(8)

#4
a.sort()
b.sort()

#5
c = a[0:8]
d = b[2:10]

#6
e = []
for i in range(len(c)) :
    element = c[i] + d[i]
    e.append(element)

#7
dataTuple = tuple(e)

#8
minTuple = min(dataTuple)
maksTuple = max(dataTuple)
sumTuple = sum(dataTuple)

#9
myString = "python adalah bahasa pemrograman yang menyenangkan"

#10
charPenyusun = set(myString)

#11
listPenyusun = list(charPenyusun)
listPenyusun.sort()
