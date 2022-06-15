class login:
    def __init__(self, id, pas):
        self.id = id
        self.pas = pas

    def check(self, id, pas):
   
        if self.id == id and self.pas == pas:
            print ("Login success!")
        else:
            exit()
log = login("Hamdan123", "123")
user=input("Enter Username : " )
passw=input("Enter password : ")
log.check(user,passw)
        

class mahasiswa:
    def __init__ (self,nama,no_peserta,tgl_lahir,asal_sma,prodi1, prodi2):
        self.nama=nama
        self.no_peserta = no_peserta
        self.tgl_lahir= tgl_lahir
        self.asal_sma= asal_sma
        self.prodi1= prodi1
        self.prodi2= prodi2

    def tampil(self):
        print('\t')
        print("\n=====KARTU UJIAN MANDIRI UNIVERSITAS INDONESIA======")
        print(f'Nama : {self.nama}')
        print(f'No Peserta : {self.no_peserta}')
        print(f'Tanggal Lahir : {self.tgl_lahir}')
        print(f'Asal Sekolah : {self.asal_sma}')
        print(f'Pilihan Prodi 1 : {self.prodi1}')
        print(f'Pilihan Prodi 2 : {self.prodi2}')
        print('=======================================================')

class Informasi:
    def __init__(self,hari,lokasi,jam,pusat,ruangan,alamat):
        self.hari = hari
        self.lok = lokasi
        self.jam = jam
        self.pusat = pusat
        self.ruangan = ruangan
        self.alamat = alamat

    def jadwal(self):
        print('\t')
        print('=============JADWAL UJIAN===============')
        print(f'Hari : {self.hari}')
        print(f'Jam : {self.jam}')
        print(f'=======================================') 
        print('\t')
        print('===========LOKASI UJIAN=================')
        print(f'Pusat Ujian : {self.pusat}')
        print(f'Lokasi Ujian : {self.lok}')
        print(f'Alamat : {self.alamat}')
        print(f'Ruangan : {self.ruangan}')
        print(f'========================================')







