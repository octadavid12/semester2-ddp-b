import random, string

# Membuka file 
Klien   = open('nasabah.txt','r+')
dataKlien   = {}
for line in Klien:
  arr = line.split(',')
  dataKlien[arr[0]] = arr

Transfer = open('transfer.txt','r+')
dataTransfer = {}
for line in Transfer:
  arr = line.split(',')
  dataTransfer[arr[1]] = arr

# ----- Fungsi operasi pada file -----
# - Fungsi menulis data baru ke file -
def overwrite():
  Klien.seek(0)
  for data in dataKlien.values():
    Klien.write(f"{data[0]},{data[1]},{int(data[2])}\n")
  Transfer.seek(0)
  for data in dataTransfer.values():
    Transfer.write(f"{data[0]},{data[1]},{data[2]},{int(data[3])}\n")

# ----- Fungsi fitur pada menu utama -----
# - Fungsi Buka Rekening -
def buka_rekening():
  print("\n*** BUKA REKENING ***")
  nama  = input("Masukkan nama: ")
  saldo = int(input("Masukkan setoran awal: "))
  norek = "REK" + ''.join(random.choice(string.digits) for _ in range(3))
  dataKlien[norek] = [norek,nama,saldo]
  overwrite()
  print(f"Pembukaan rekening dengan nomor {norek} atas nama {nama} berhasil.\n")
  main()

# - Fungsi Setoran Tunai -
def setor_tunai():
  print("\n*** SETORAN TUNAI ***")
  norek = input("Masukkan nomor rekening: ").upper()
  saldo = int(input("Masukkan nominal yang akan disetor: "))
  data = dataKlien.get(norek,False)
  if data != False:
    dataKlien[norek][2] = int(data[2]) + saldo
    overwrite()
    print(f"Setoran tunai sebesar {saldo} ke rekening {norek} berhasil.\n")
  else:
    print("Nomor rekening tidak terdaftar. Setoran tunai gagal.\n")
  main()

# - Fungsi Tarik Tunai -
def tarik_tunai():
  print("\n*** TARIK TUNAI ***")
  norek = input("Masukkan nomor rekening: ").upper()
  saldo = int(input("Masukkan nominal yang akan ditarik: "))
  data = dataKlien.get(norek,False)
  if data != False:
    if int(data[2]) >= saldo:
      dataKlien[norek][2] = int(data[2]) - saldo
      overwrite()
      print(f"Tarik tunai sebesar {saldo} dari rekening {norek} berhasil.")
    else:
      print("Saldo tidak mencukupi. Tarik tunai gagal.")
  else:
    print("Nomor rekening tidak terdaftar. Tarik tunai gagal.\n")
  main()

# - Fungsi Transfer -
def transfer_uang():
  print("\n*** TRANSFER ***")
  norek0 = input("Masukkan nomor rekening sumber: ").upper()
  norek1 = input("Masukkan nomor rekening tujuan: ").upper()
  saldo  = int(input("Masukkan nominal yang akan ditransfer: "))
  trf    = "TRF" + ''.join(random.choice(string.digits) for _ in range(3))
  data0  = dataKlien.get(norek0,False)
  data1  = dataKlien.get(norek1,False)
  if data0 != False:
    if data1 != False:
      if int(data0[2]) >= saldo:
        dataKlien[norek0][2], dataKlien[norek1][2] = int(data0[2]) - saldo, int(data1[2]) + saldo
        dataTransfer[norek0] = [trf,norek0,norek1,saldo]
        overwrite()
        print(f"Transfer sebesar {saldo} dari rekening {norek0} ke rekening {norek1} berhasil.\n")
      else:
        print("Saldo tidak mencukupi. Transfer gagal.\n")
    else:
      print("Nomor rekening tujuan tidak terdaftar. Transfer gagal.\n")
  else:
    print("Nomor rekening sumber tidak terdaftar. Transfer gagal.\n")
  main()

# - Fungsi Daftar data Transfer -
def daftar_transfer():
  print("\n*** LIHAT DATA TRANSFER ***")
  norek = input("Masukkan nomor rekening sumber transfer: ").upper()
  data0 = dataKlien.get(norek,False)
  data1 = dataTransfer.get(norek,False)
  if data0 != False:
    if data1 != False:
      print(f"Daftar transfer dari rekening {norek} :")
      print(f"{data1[0]} {data1[1]} {data1[2]} {int(data1[3])}\n")
    else:
      print("Tidak ada data yang ditampilkan.\n")
  else:
    print("Nomor rekening sumber tidak terdaftar.\n")
  main()

# - fungsi sisa saldo nasabah - #
def sisa_saldo():
  print("\n*** LIHAT SISA SALDO ***")
  norek = input("masukan nomor rekening sumber : ").upper()
  data = dataKlien.get(norek,False)
  if data != False:
    print(f"Lihat Sisa saldo terkini {norek} :")
    print(f"{data[0]} {data[1]} {data[2]} \n")
  else:
    print("Nomor rekening sumber tidak terdaftar. \n")
  main()


# - Fungsi Keluar dan Menutup File -
def keluar():
  Klien.close()
  Transfer.close()
  print("Terima kasih atas kunjungan Anda...")

# - Fungsi Menu Utama -
def main():
  print("***** SELAMAT DATANG DI NF BANK *****\nMENU:\n[1] Buka rekening\n[2] Setoran tunai\n[3] Tarik tunai\n[4] Transfer\n[5] Lihat daftar transfer\n[6] lihat saldo\n[7] keluar")
  option = input("Masukkan menu pilihan anda: ")
  while option not in ['1','2','3','4','5','6','7']:
    option = input("Pilihan Anda salah. Ulangi.\nMasukkan menu pilihan anda: ")
  switch = {'1': buka_rekening, '2': setor_tunai, '3': tarik_tunai, '4':transfer_uang, '5': daftar_transfer, '6': sisa_saldo, '7': keluar}
  switch[option]()

if __name__ == "__main__":
  main()