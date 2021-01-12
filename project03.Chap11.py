from datetime import*

def diffDate (x):
    x = x.split('-')
    listTgl = []
    tgl1 = date(int(x[0]), int(x[1]), int(x[2]))
    tgl2 = datetime.date(datetime.now())
    selisih = tgl1 - tgl2
    hasil = selisih.days
    return hasil

file = open('data peminjaman buku.txt', 'r')
isi = file.readlines()

mKode = input('Masukkan Kode Member : ')
print('')

for i in range(len(isi)):
    if(mKode in isi[i]):
        data = isi[i].split('|')
        status = 'ada'
        break
    else:
        status = 'tidak ada'
        continue

if(status == 'ada'):
    terlambat = diffDate(data[4])
    denda = 2000*abs(terlambat)
    hariIni = datetime.date(datetime.today())
    print('Data Peminjaman Buku')
    print('Kode Member : ' , data[0])
    print('Nama Member : ' , data[1])
    print('Judul Buku : ' , data[2])
    print('Tanggal Mulai Pinjam : ', data[3])
    print('Tanggal Maks Peminjaman : ', data[4], end ='')
    print('Tanggal Pengembalian : ', hariIni)
    if(terlambat >= 0):
        print('Terlambat : 0 hari')
        print('Denda : Rp 0')
    else:
        print('Terlambat : ', abs(terlambat))
        print('Denda : Rp', denda)
else:
    print('Data tidak di temukan')

    
        
