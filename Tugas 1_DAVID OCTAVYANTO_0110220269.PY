#2
print('Kalkulator biaya kuliah bagi mahasiswa')

nim_kalkulator = input('masukan NIM :')
tahunmasuk_kalkulator = nim_kalkulator[5:7]

if(tahunmasuk_kalkulator =='20'):
    bop = 4000000
    biaya_sks = 200000
    print('mahasiswa yang masuk tahun 2020 memiliki BOP dasar sebesar Rp.',bop,'\n')
elif(tahunmasuk_kalkulator == '19'):
    bop = 3500000
    biaya_sks = 175000
    print('mahasiswa yang masuk tahun 2019 memiliki BOP dasar sebesar Rp.',bop,'\n')
elif(tahunmasuk_kalkulator == '18'):
    bop = 3200000
    biaya_sks = 150000
    print('mahasiswa yang masuk tahun 2018 memiliki BOP dasar sebesar Rp.',bop,'\n')
elif(tahunmasuk_kalkulator == '17'):
    bop = 2800000
    biaya_sks = 130000
    print('mahasiswa yang masuk tahun 2017 memiliki BOP dasar sebesar Rp.',bop,'\n')
else:
    print('tahun tidak diketahui\n')
sks_kalkulator = int(input( "jumlah sks yang diambil semester ini:" ))
if sks_kalkulator >= 15:
    totalbiaya = bop + (sks_kalkulator - 15) * biaya_sks
    print('biaya tambahan untuk',sks_kalkulator - 15,'SKS=',biaya_sks *(sks_kalkulator - 15 ))
    print("Total biaya kuliah : RP.", totalbiaya)

pilih_subsidi = input('Apakah  anda ingin mengajukan subsidi biaya kuliah? (Y/T):')
if (pilih_subsidi == 'Y'):
    semester = int(input("semester berapa anda sekarang :"))
    if (semester > 1 and semester < 9):
        ip_s1 = float(input('masukan ip semester 1:'))
        ip_s2 = float(input('masukan ip semester 2:'))
        ip_s3 = float(input('masukan ip semester 3:'))
        ratarataip = (ip_s1 + ip_s2 + ip_s3) / 3
        subsidi = (round(ratarataip, 2) / 4) * 1000000
        print('anda mendapatkan subsidi sebesar', subsidi)
        print('total biaya kuliah : RP. ', totalbiaya - subsidi)
    else:
        print('Anda Tidak bisa mengerjakan subsidi biaya kuliah')
else:
    print('penghitungan biaya kuliah selesai. \n')

// KOMENTAR //
// Itu saya mendapatkan code nya hasil diskusi bersama ASDOS NYA//