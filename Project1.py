import os
import random
import string
from datetime import datetime
os.system("cls")

data_pesanan = {}

def tambah_pesanan() :
    global data_pesanan

    NP = input("Masukan Nama Pemesan : ")
    NM = input("Masukan Nama Menu : ")
    H = int(input("Masukan Harga : "))
    W = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    ascii = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))

    data_pesanan[ascii] = {
        "Nama Pemesan" : NP,
        "Nama Menu" : NM,
        "Harga" : H,
        "Waktu" : W, 
    }
    print("Data Pesanan Berhasil Ditambahkan!")

def lihat_pesanan() :
    global data_pesanan

    print(f'{"ID":<8} {"Nama Pemesan":<20} {"Nama Menu":<20} {"Harga":<9} {"Waktu":<15}')
    print("-"*100)
    for keys, nilai in data_pesanan.items() :
        print(f'{keys:<9}{nilai["Nama Pemesan"]:<21}{nilai["Nama Menu"]:<21}{nilai["Harga"]:<10}{nilai["Waktu"]:<5}')

def total_pendapatan() :
    global data_pesanan

    total = 0

    for keys, nilai in data_pesanan.items() :
        total += nilai["Harga"] 
    print(f'Total Pendapatan adalah Rp.{total}')
 



while True :
    print("-"*40)
    print('Ketik "1" untuk tambah pesanan')
    print('Ketik "2" untuk lihat pesanan')
    print('Ketik "3" untuk total pendapatan')
    print('Ketik "4" untuk keluar')
    print("-"*40)
    
    input_user = input("Masukan Nomor ? ")

    if input_user == "1" :
        tambah_pesanan()
    elif input_user == "2" :
        lihat_pesanan()
    elif input_user == "3" :
        total_pendapatan()
    elif input_user == "4" :
        print("Terima kasih!")
        break


