#Project2

def dataStat(x) :

    a = sum(x) / len(x)
    b = max(x)
    c = min(x)

    datasd = [a,b,c]

    return datasd

while True :
    try :
        n = int(input('Masukkan banyak angka yang ingin anda input ? :'))
        break
    except ValueError :
        print('Input tidak valid')
        continue

data = []

i = 0

while (i < n) :
    try :
        bil = int(input('Masukkan bilangan bulat yang anda inginkan :'))
        data.append(bil)
        i += 1

    except ValueError :
        print('Input tidak valid')

printData = dataStat(data)        
print(printData)
