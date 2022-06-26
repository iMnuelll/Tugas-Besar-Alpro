import matplotlib.pyplot as plt
import numpy as np

januariPemasukan = []
februariPemasukan = []
maretPemasukan = []
aprilPemasukan = []
meiPemasukan = []
juniPemasukan = []
juliPemasukan = []
agustusPemasukan = []
septemberPemasukan = []
oktoberPemasukan = []
novemberPemasukan = []
desemberPemasukan = []


def mainMenu() :
    print("=== Menu Utama =====")
    print("""
    1. Input Pemasukan
    2. Tampilkan Grafik
    3. Exit
    """)
     

def keuntungan() :
    count = 0
    while count <= 11 :
        inputBulan = input("Silahkan masukkan bulan : ")
        if inputBulan == "Januari" :
            pemasukan = int(input("Masukkan keuntungan : "))
            januariPemasukan.append(pemasukan)
            print()
        elif inputBulan == "Februari" :
            pemasukan = int(input("Masukkan keuntungan : "))
            februariPemasukan.append(pemasukan)
            print()
        elif inputBulan == "Maret" :
            pemasukan = int(input("Masukkan keuntungan : "))
            maretPemasukan.append(pemasukan)
            print()
        elif inputBulan == "April" :
            pemasukan = int(input("Masukkan keuntungan : "))
            aprilPemasukan.append(pemasukan)
            print()
        elif inputBulan == "Mei" :
            pemasukan = int(input("Masukkan keuntungan : "))
            meiPemasukan.append(pemasukan)
            print()
        elif inputBulan == "Juni" :
            pemasukan = int(input("Masukkan keuntungan : "))
            juniPemasukan.append(pemasukan)
            print()
        elif inputBulan == "Juli" :
            pemasukan = int(input("Masukkan keuntungan : "))
            juliPemasukan.append(pemasukan)
            print()
        elif inputBulan == "Agustus" :
            pemasukan = int(input("Masukkan keuntungan : "))
            agustusPemasukan.append(pemasukan)
            print()
        elif inputBulan == "September" :
            pemasukan = int(input("Masukkan keuntungan : "))
            septemberPemasukan.append(pemasukan)
            print()
        elif inputBulan == "Oktober" :
            pemasukan = int(input("Masukkan keuntungan : "))
            oktoberPemasukan.append(pemasukan)
            print()
        elif inputBulan == "November" :
            pemasukan = int(input("Masukkan keuntungan : "))
            novemberPemasukan.append(pemasukan)
            print()
        elif inputBulan == "Desember" :
            pemasukan = int(input("Masukkan keuntungan : "))
            desemberPemasukan.append(pemasukan)
            print("Terimakasih...")
            print()
        count+=1
    
def statistik() :
    print(">>> STATISTIK KEUANGAN <<<")
    try :
      laba = [januariPemasukan[0],februariPemasukan[0],maretPemasukan[0],aprilPemasukan[0],meiPemasukan[0],juniPemasukan[0],juliPemasukan[0],agustusPemasukan[0],septemberPemasukan[0],oktoberPemasukan[0],novemberPemasukan[0],desemberPemasukan[0]]
      bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
      plt.bar(bulan, laba, color='blue', edgecolor='red')
      plt.title("Statistik Keuangan Perbulan")
      plt.ylabel("Laba (Juta)")
      plt.xlabel("Bulan")
      plt.show()
    except :
        print("Data tidak bisa ditampilkan, mohon masukkan semua laba di tiap bulannya")
        print()

count = 0

while count < 1000 :
        print("--- Program Pencatatan Laporan Keuangan Bulanan ---")
        print()
        mainMenu()
        pilihMenu = int(input("Pilih Menu : "))
        if pilihMenu == 1 :
            print()
            keuntungan()
        elif pilihMenu == 2 :
            print()
            statistik()
        elif pilihMenu == 3 :
            print("Terima Kasih")
            break
        count +=1