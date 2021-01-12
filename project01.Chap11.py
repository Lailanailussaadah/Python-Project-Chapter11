from datetime import*

def diffDate(x):
    x = x.split('-')
    tgl1 = date(int(x[0]), int(x[1]), int(x[2]))
    tgl2 = datetime.date(datetime.now())
    selisih = tgl1 - tgl2
    hasil = selisih.days
    print('Tanggal sekarang       : ', tgl2)
    print('Tanggal yang dipanggil : ', tgl1)
    print('Selisih tanggal        : ', selisih, 'hari')
    return hasil

diffDate('2021-1-20')
