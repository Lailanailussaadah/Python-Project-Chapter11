from datetime import*

def dataBuku(kode, nama, judul):
    data = open('data peminjaman buku.txt', 'a')
    tgl = datetime.date(datetime.now())
    tglKembali = tgl + timedelta(days = 7)
    listData = [kode, nama, judul, str(tgl), str(tglKembali)]
    data.write('|'.join(listData) +'\n')
    data.close()
   

ulang = 'y'
while ulang == 'y':
    kode = input('Masukkan Kode Member : ')
    nama = input('Masukkan Nama Member : ')
    judul = input('Masukkan Judul Buku  : ')
    dataBuku(kode, nama, judul)
    data = ('data peminjaman buku.txt', 'a')
    ulang = input('\nUlangi input lagi (y/n)? ')
    print('')
    if ulang == 'n':
        break
 
