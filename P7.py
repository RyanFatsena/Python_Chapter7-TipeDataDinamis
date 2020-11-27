#Project7

fruit = { 'apel'  : 5000,
          'jeruk' : 8500,
          'mangga': 7800,
          'duku'  : 6500 }

def expensive(dictionary) :

    key = list(dictionary.keys())
    values = tuple(dictionary.values())

    hargaExpensive = max(values)

    indexHargaExpensive = values.index(hargaExpensive)

    print(key[indexHargaExpensive])

expensive(fruit)
