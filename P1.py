#Project1

while True :
    try :
        n = int(input('Masukkan berapa banyak angka yang ingin anda input? :'))
        break
    except ValueError :
        print('Input tidak valid')
        continue

data = []

i = 0

while (i < n) :
    try :
        bil = int(input('Masukkan bilangan bulat yang anda inginkan : '))
        data.append(bil)
        i+= 1

    except ValueError :
        print("Input tidak valid")
        
data.sort(reverse = True)
print(data)
