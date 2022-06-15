from biodata import mahasiswa
from biodata import Informasi

nama = input('Masukkan Nama : ')
nopst = input('Masukkan No Peserta : ')
tgl = input('Masukkan Tanggal Lahir : ')
asal = input('Masukkan Asal Sekolah : ')
prd1 = input('Masukkan Pilihan Prodi 1 : ')
prd2 = input('Masukkan Pilihan Prodi 2 : ')

    
tampil=mahasiswa(nama,nopst,tgl,asal,prd1,prd2)
tampil.tampil()

cek = Informasi('Senin','Departemen Bisnis dan Sekolah Vokasi','14.00 WIB - 16.00 WIB', 'UNIVERSITAS INDONESIA KAMPUS A', 'Gedung A Ruang 13', 'Jl. Tentara Pelajar, Depok' )
cek.jadwal()