#Project13

def nilaiTertinggi(nilaiMhs):
    nilaiIyan = 0
    
    for r in nilaiMhs:
        nilaiMid = r.get('mid')
        nilaiAkhr = r.get('uas')
        nilaiTotalAkhir = (nilaiMid + 2*nilaiAkhr)/3
        
        if(nilaiTotalAkhir > nilaiIyan):
            nilaiIyan = nilaiTotalAkhir
            data = {}
            data['nim'] = r.get('nim')
            data['nama'] = r.get('nama')
    return data

nilaiMhs = [{'nim' : 'A01',
             'nama': 'Amir',
             'mid' : 50,
             'uas' : 80},
            {'nim' : 'A02',
             'nama': 'Budi',
             'mid' : 40,
             'uas' : 90},
            {'nim' : 'A03',
             'nama': 'Cici',
             'mid' : 50,
             'uas' : 50},
            {'nim' : 'A04',
             'nama': 'Dedi',
             'mid' : 20,
             'uas' : 30},
            {'nim' : 'A05',
             'nama': 'Fifi',
             'mid' : 70,
             'uas' : 40}]

nilaiTinggi = nilaiTertinggi(nilaiMhs)
print('Mahasiswa dengan nama {0} dan NIM {1} mendapat nilai akhir tertinggi'.format(nilaiTinggi['nama'], nilaiTinggi['nim']))
