import random
import string
import os

os.system("cls")

def header() :
    print(f'\n{"SVORPROJECT004":^40}')
    print(f'{"Sistem Manajemen Inventaris Toko":^40}')
    print(f'{"="*40:^40}\n')


main_data = {}

def input_barang() :
    global main_data
    ascii = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))

    NAB = input("Masukan Nama Barang : ")
    KTB = input("Masukan Kategori Barang : ")
    HRB = input("Masukan Harga Barang : ")
    STB = int(input("Masukan Stock Barang : "))

    main_data[ascii] = {
        "Nama Barang"       :NAB,
        "Kategori Barang"    :KTB,
        "Harga Barang"      :HRB,
        "Stock Barang"      :STB
    }
    print("Data Barang Berhasil Ditambahkan, Terima Kasih!")


def Table() :
    print(f'{"ID":<7} {"Nama Barang":<17} {"Kategori Barang":<21} {"Harga Barang":<18} {"Sisa Stock":<17}')
    print("="*80)

    for keys, value in main_data.items() :
        print(f'{keys:7} {value["Nama Barang"]:<17} {value["Kategori Barang"]:<21} {value["Harga Barang"]:<18} {value["Stock Barang"]:<17}')
    
def search_update() :
    search = input("Masukan Nama Barang : ")
    correction = False
    
    print(f'{"ID":<7} {"Nama Barang":<17} {"Kategori Barang":<21} {"Harga Barang":<18} {"Sisa Stock":<17}')
    print(f'{"="*80}')

    for keys, value in main_data.items() :
        if search.lower() == value["Nama Barang"] : 
            print(f'{keys:7} {value["Nama Barang"]:<17} {value["Kategori Barang"]:<21} {value["Harga Barang"]:<18} {value["Stock Barang"]:<17}')
            print("Data Barang Ditemukan.")    
    if search.lower() == False :
        print("Data Barang Tidak Ditemukan!")

def stock_update () :
    update_stock = input("Masukan Nama Barang : ")
    ketemu = False
    
    for _, value in main_data.items() :
        if update_stock.lower() in value["Nama Barang"].lower() :
            print(f'Nama Barang : {value["Nama Barang"]}')
            print(f'Jumlah Stock : {value["Stock Barang"]}\n')
    
            Input_NB = input("Ingin Tambah Stock / Kurangi Stock (t/k) : ").lower()
            Input_SB = int(input(" Masukan Jumlah: \n").lower())

            if Input_NB == "t" :
                value["Stock Barang"] += Input_SB
            elif Input_NB == "k":
                value["Stock Barang"] -= Input_SB
            
            print("Update Stock Berhasil!")
            print(f'Jumlah Stock Terbaru : {value["Stock Barang"]}\n')
            ketemu = True
    if ketemu == False :
        print("Data Tidak Ditemukan!")


def Stock_Menipis () :
    print("Stock Barang Menipis : ")
    print(f'{"ID":<7} {"Nama Barang":<17} {"Sisa Stock":<21}')
    print(f'{"="*80}')
    
    ketemu = False

    for key, value in main_data.items() :
        
        if value["Stock Barang"]  < 5 :
            print(f'{key:<7} {value["Nama Barang"]:<17} {value["Stock Barang"]:<21}')
        ketemu = True
    if ketemu == False :
        print("Barang Tidak Ditemukan!")
    
            

while True :
    '''Main Data'''
    print('\nMasukan "1" Untuk Tambah Data Barang Baru.')
    print('Masukan "2" Untuk Lihat List dan Cari Data Barang.')
    print('Masukan "3" Untuk Update Stock Barang.')
    print('Masukan "4" Untuk Cek Stock Barang Menipis.')
    print('Masukan "5" Untuk Keluar.')
    print(f'{"="*50}\n')
    
    input_angka = input("Mohon Masukan Nomor : ")
    
    if input_angka == "1" :
        input_barang()
    elif input_angka == "2" :
        print('Masukan "1" untuk Lihat List Data Barang')
        print('Masukan "2" untuk Cari Data Barang\n')

        cek_barang = input('Mohon Masukan Nomor :')
        if cek_barang == "1" :
            Table() 
        if cek_barang == "2" :
            search_update()
    elif input_angka == "3" :
            stock_update ()     
    elif input_angka == "4" :
        Stock_Menipis ()
    elif input_angka == "5" :
        print("Terima kasih!")
        break