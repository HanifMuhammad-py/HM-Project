import os
import random
import string
os.system("cls")

main_table = {}

def header() :
    print(f'{"SVORPROJECT004":^40}')
    print(f'{"Sistem Manajemen Data Pelanggan":^40}')
    print(f'{"="*40:^40}\n')

def input_data() :
    global main_table
    
    nama = input("Masukan Nama : ")
    no_hp = input("Masukan No.HP : ")
    layanan = input("Masukan Jenis Layanan : ")

    
    
    main_table[ascii] = {
        "NM" : nama,
        "NO" : no_hp,
        "LN" : layanan
    }
    print("Data Berhasil Disimpan, Terima Kasih!")

def table() :
    print(f'{"ID":<9}{"Nama":<15}{"No.HP":<20}{"Layanan":<15}')
    print("="*60)

    for keys, value in main_table.items() :
        print(f'{keys:<9}{value["NM"]:<15}{value["NO"]:<20}{value["LN"]:<15}')

def search() :
    
    search = input("Masukan Nama Pelanggan (SEARCH) : ")
    correct = False
    print(f'{"ID":<9}{"Nama":<15}{"No.HP":<20}{"Layanan":<15}')
    print("="*60)

    for keys, value in main_table.items() :
        if search.lower() in value["NM"].lower() :
            print(f'{keys:<9}{value["NM"]:<15}{value["NO"]:<20}{value["LN"]:<15}')
            correct = True
    if correct == False :
        print("Data Tidak Ditemukan!")


def delete() :
    global main_table
    
    delete_id = input("Masukan ID Pelanggan (DELETE) : ")
    
    if delete_id in main_table :
        main_table.pop(delete_id)
        print(f"Data pelanggan dengan ID {delete_id} berhasil di hapus")
    else :
        print("ID Pelanggan Tidak Ditemukan!")

        
while True :
    print('Ketik "1" Untuk Menambahkan Data Pelanggan')
    print('Ketik "2" lihat Data Pelanggan')
    print('Ketik "3" Cari Data Pelanggan')
    print('Ketik "4" Lihat Data Pelanggan')
    print("="*60)

    input_nomor = input("Mohon Masukan Nomor = ")
    if input_nomor == "1" :
        input_data()
    elif input_nomor == "2" :
        table()
    elif input_nomor == "3" :
        search()
    elif input_nomor == "4" :
        delete()

