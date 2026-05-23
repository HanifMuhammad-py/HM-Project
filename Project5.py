# Project 005

'''IMPORT'''
from datetime import datetime as dt
import random
import string
import os
os.system("cls")

'''DICT DATA KOSONG'''
data_modul_pemesanan = {}
data_modul_keuangan = {}
data_modul_Customer = {}
data_modul_inventoris = {}
data_modul_laporan_harian = {}


'''HEADER'''
def header() :
    print(f'\n{"SVORPROJECT005":^40}')
    print(f'{"Several Oracles Business Suite":^40}')
    print(f'{"="*40}\n')


'''WHILE TRUE : MODUL PEMESANAN'''
def Hitung_total (HM, JM) :
    return  HM * JM 

def Tambah_Pesanan() :
    global data_modul_pemesanan

    NP = input("Masukan Nama Pelanggan : ")
    NM = input("Masukan Nama Menu : ")
    HM = int(input("Masukan Harga Menu : "))
    JM = int(input("Masukan Jumlah Menu : "))
    WB = dt.now().strftime(":%Y/%M/%d %H:%M:%S")
    TL = Hitung_total (HM, JM)

    ascii = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_modul_pemesanan[ascii] = {
        "Nama Pelanggan"    :NP,
        "Nama Menu"         :NM,
        "Harga Menu"        :HM,
        "Jumlah Menu"       :JM,
        "Waktu Beli"        :WB,
        "Total Harga"       :TL
    }
    
def Lihat_Pesanan() :
    print(f'{"ID":<6} {"Nama Pelanggan":<15} {"Nama Menu":<11} {"Harga Menu":<10} {"Jumlah Menu":<12} {"Total Harga":<8} {"Waktu Pembelian":<25}')
    print(f'{"="*80}\n')

    for keys, value in data_modul_pemesanan.items() :
        print(f'{keys:<6} {value["Nama Pelanggan"]:<15} {value["Nama Menu"]:<11} {value["Harga Menu"]:<10} {value["Jumlah Menu"]:<12} {value["Total Harga"]:<8} {value["Waktu Beli"]:<25}')

def Cari_Pesanan() :
    search = input("Masukan Nama Menu : ")
    correct = False

    print(f'{"ID":<6} {"Nama Pelanggan":<15} {"Nama Menu":<11} {"Harga Menu":<7} {"Jumlah Menu":<5} {"Total Harga":<8} {"Waktu Pembelian":<25}')
    print(f'{"="*80}')

    for keys, value in data_modul_pemesanan.items() :
        if search.lower() == value["Nama Menu"] :
            print(f'{keys:<6} {value["Nama Pelanggan"]:<15} {value["Nama Menu"]:<11} {value["Harga Menu"]:<7} {value["Jumlah Menu"]} {value["Total Harga"]:<8} {value["Waktu Beli"]:<25}')
            print("Data Ditemukan!")
            correct = True
    if correct == False :
        print("Data Tidak Ditemukan!") 

def Hapus_Pesanan() :
    global data_modul_pemesanan
    search_to_delete = input("Masukan ID Pelanggan (6 Digit ID Huruf CAPIITAL) : ")
    
    print("Data Yang Akan Dihapus : ")
    print(f'{"ID":<6} {"Nama Pelanggan":<15} {"Nama Menu":<11} {"Harga Menu":<7} {"Jumlah Menu":<5} {"Total Harga":<8} {"Waktu Pembelian":<25}')
    print(f'{"="*80}\n')

    if search_to_delete in data_modul_pemesanan :
        data_modul_pemesanan.pop(search_to_delete)
        print("Data Pesanan Berhasil Dihapus!")
    else :
        print("Data Tidak Ditemukan!")


'''WHILE TRUE : MODUL KEUANGAN''' 
def Catat_Pengeluaran() :
    global data_modul_keuangan
    
    IP = input("Masukan Jenis Pengeluaran : ")
    NP = int(input("Masukan Nominal pengeluaran : "))

    ascii = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_modul_keuangan[ascii] = {
       "Jenis Pengeluaran"     :IP,
       "Nominal Pengeluaran"   :NP  
    } 

    for keys, value in data_modul_keuangan.items() : 
        print(f'{keys:<6} {value["Jenis Pengeluaran"]:<15} {value["Nominal Pengeluaran"]:<11}')
        print(f'{"="*80}')

def Lihat_Laporan_Keuangan() :
    global data_modul_pemesanan
    global data_modul_keuangan
    
    '''TOTAL PEMASUKAN'''    
    print(f'{"ID":<6} {"Pelanggan":<15} {"Menu":<11} {"Total Pemasukan":<11}')
    print(f'{"="*80}')

    for keys, value in data_modul_pemesanan.items() : 
        print(f'{keys:<6} {value["Nama Pelanggan"]:<15} {value["Nama Menu"]:<11} {value["Total Harga"]:<11}')

    total_pemasukan = 0
    for keys, value in data_modul_pemesanan.items() : 
        total_pemasukan += value["Harga Menu"]
    print (f'Pemasukan Hari ini adalah = {total_pemasukan}\n')

    '''TOTAL PENGELUARAN'''
    print(f'{"ID":<6} {"Keterangan":<15} {"Menu":<11} {"Jumlah":<11}')
    print(f'{"="*80}')

    for keys, value in data_modul_keuangan.items() : 
        print(f'{keys:<6} {value["Jenis Pengeluaran"]:<15} {value["Nominal Pengeluaran"]:<11}')


    total_pengeluaran = 0
    for keys, value in data_modul_keuangan.items() : 
        total_pengeluaran += value["Nominal Pengeluaran"]
    print (f'Total Pengeluaran Hari ini adalah = {total_pengeluaran}')

    '''NET PROFIT'''
    print(f'{"="*80}\n')
    net_profit = total_pemasukan - total_pengeluaran
    
    print(f'Total Pendapatan Hari ini adalah Rp.{net_profit}')
    if net_profit > 0 :
        print("✅ UNTUNG")
    if net_profit < 0 :
        print("❌ RUGI")
    print(f'{"="*80}\n')


'''WHILE TRUE : MODUL CUSTOMER'''
def Tambah_Data_Customer () :
    global data_modul_Customer
    
    NC = input("Masukan Nama Customer :")
    NOC = input("Masukan No.HP Customer :")
    AC = input("Masukan Alamat Customer :")
    JL = input("Masukan Jenis Layanan :")

    ascii =  ''.join((random.choice(string.ascii_uppercase)for i in range(6)))
    data_modul_Customer[ascii] = {
        "Nama Customer"     : NC,
        "No. HP Customer"   : NOC,
        "Alamat Customer"   : AC,
        "Jenis Layanan"     : JL
    }           

def Lihat_Data_Customer() :
    print(f'{"ID":<6} {"Nama Customer":<6} {"No. HP":<6} {"Alamat":<6} {"Jenis Layanan":<6}')
    print(f'{"="*80}')

    for keys, value in data_modul_Customer.items() :
        print(f'{keys:<6} {value["Nama Customer"]:<6} {value["No. HP Customer"]:<6} {value["Alamat Customer"]:<6} {value["Jenis Layanan"]:<6}')


def  Cari_Data_Customer() :
    search_customer = input("Masukan Nama Customer : ")
    correct = False

    print(f'{"ID":<6} {"Nama Customer":<19} {"No. HP":<32} {"Alamat":<36} {"Jenis Layanan":<45}')
    print(f'{"="*80}')
    for keys, value in data_modul_Customer.items():
        if search_customer.lower() == value["Nama Customer"] :
            print(f'{keys:<6} {value["Nama Customer"]:<19} {value["No. HP Customer"]:<32} {value["Alamat Customer"]::<36} {value["Jenis Layanan"]:<45}')
            correct = True
    if correct == False :
        print("Data Customer Tidak Ditemukan!")

def Update_Data_Customer() :
    global data_modul_Customer
    correct = False

    Search_data_customer = input("Masukan Nama Customer :")
        
    print('Ketik "1" Untuk Update No. HP Customer')
    print('Ketik "2" Untuk Update Alamat Customer')
    print('Ketik "3" Untuk Update Jenis Layanan Customer')
    print('Ketik "3" EXIT\n')
        
    for keys, value in data_modul_Customer.items() :
        input_indt_update = input("Mohon Masukan Nomor :")
        if input_indt_update == "1" : 
            if Search_data_customer.lower() in value["Nama Customer"].lower() :
                print(f'Nama Customer : {value["Nama Customer"]}')
                print(f'No. HP Customer : {value["No. HP Customer"]}\n')

                Input_No_Baru = int(input("Masukan No. HP Customer Yang Terbaru : ")) 
                value["No. HP Customer"] = Input_No_Baru
                print("No. HP Customer Berhasil Diupdate!")
                correct = True         
            if correct == False :
                print("Data Tidak Ditemukan!")
        elif input_indt_update == "2" :
            if Search_data_customer.lower() in value["Nama Customer"].lower() :
                print(f'Nama Customer : {value["Nama Customer"]}')
                print(f'Alamat Customer : {value["Alamat Customer"]}\n')

                Input_Alamat_Baru = input("Masukan Alamat Customer Yang Terbaru : ") 
                value["Alamat Customer"] = Input_Alamat_Baru
                print("Alamat Customer Berhasil Diupdate!")
                correct = True         
            if correct == False :
                print("Data Tidak Ditemukan!")
        elif input_indt_update == "3" :
            if Search_data_customer.lower() in value["Nama Customer"].lower() :
                print(f'Nama Customer : {value["Nama Customer"]}')
                print(f'Jenis Layanan : {value["Jenis Layanan"]}\n')

                Input_Jenis_Layanan_Baru = input("Masukan Jenis Layanan Customer Yang Terbaru : ") 
                value["Alamat Customer"] = Input_Jenis_Layanan_Baru
                print("Jenis Layanan Customer Berhasil Diupdate!")
                correct = True         
            if correct == False :
                print("Data Tidak Ditemukan!")
            

    print("Data Customer Yang Akan Dihapus : ")
    print(f'{"ID":<6} {"Nama Customer":<6} {"No. HP":<6} {"Alamat":<6} {"Jenis Layanan":<6}')
    print(f'{"="*80}')
    
    
def Hapus_Data_Customer() :
    global data_modul_Customer
    
    delete_data_customer = input("Masukan ID Pelanggan (6 Digit ID Huruf CAPIITAL) : ")
    
    print("Data Customer Yang Akan Dihapus : ")
    print(f'{"ID":<6} {"Nama Customer":<6} {"No. HP":<6} {"Alamat":<6} {"Jenis Layanan":<6}')
    print(f'{"="*80}')
        
    if delete_data_customer in data_modul_Customer :
        data_modul_Customer.pop(delete_data_customer)
        print("Data Berhasil Dihapus")
    else :
        print("Data Tidak Ditemukan : ")
        

'''WHILE  TRUE : MODUL INVENTORIS'''
def Tambah_Barang () :
    global data_modul_inventoris

    NBS = input("Masukan Nama Barang : ")
    SB = int(input("Masukan Stock Barang : "))
    print("Data Berhasil Ditambahkan!")

    ascii =  ''.join((random.choice(string.ascii_uppercase)for i in range(6)))
    data_modul_inventoris[ascii] = {
        "Nama Barang Stock" : NBS,
        "Stock Barang"      : SB 
    }
        
def Lihat_Data_Stock() :
    print(f'{"ID":<6} {"Nama Barang":<15} {"Stock Barang":<4}')
    print(f'{"="*40}')

    for keys, value in data_modul_inventoris.items() :
        print(f'{keys:<6} {value["Nama Barang Stock"]:<15} {value["Stock Barang"]:<4}')

def Update_Stock() :
    global data_modul_inventoris

    inp_update_barang = input("Masukan Nama Barang : ").lower()
    correct = False
    
    for keys, value in data_modul_inventoris.items() :
        if inp_update_barang in value["Nama Barang Stock"].lower() :
            print(f'\nNama Barang = {value["Nama Barang Stock"]}')
            print(f'Jumlah Stock = {value["Stock Barang"]}\n')
        
            tambahkurang_stock = (input("Ingin Menambah / Mengurangi Stock (t/k) : ")).lower()
            jumlah_stock = int(input("Masukan Jumlah : "))
            if tambahkurang_stock == "t" :
                value["Stock Barang"] += jumlah_stock
            elif tambahkurang_stock == "k" :
                value["Stock Barang"] -= jumlah_stock
            print("Data Berhasil terupdate!")
            correct = True
    if correct == False :
        print ("Data Tidak Ditemukan!")

def Check_Stock_Menipis() :
    print("\nStock Barang Yang Menipis : ")
    print(f'{"ID":<6} {"Nama Barang Stock":<15} {"Stock Barang":<4}')
    print(f'{"="*30}')
    correct = False
    
    for keys, value in data_modul_inventoris.items() :
        if value["Stock Barang"] < 5 :
            print(f'{keys:<6} {value["Nama Barang Stock"]:<15} {value["Stock Barang"]:<4}')
            correct = True
    if correct == False :
        print("Data Tidak Ditemukan!")

'''WHILE TRUE : MODUL LAPORAN HARIAN'''
def Laporan_Harian() :
    
    print(f'{"="*50}')
    print(f'{"LAPORAN HARIAN":^50}')
    print(f'{"="*50}')
    print(f'Dibuat : {dt.now().strftime("%d/%m/%Y %H:%M:%S")}\n')

    total_pemasukan = sum(value["Total Harga"] for value in data_modul_pemesanan.values())
    total_pengeluaran = sum(value["Nominal Pengeluaran"] for value in data_modul_keuangan.values())
    saldo = total_pemasukan - total_pengeluaran
    barang_tipis = [value["Nama Barang Stock"] for value in data_modul_inventoris.values() if value["Stock Barang"] < 5]

    print(f'Total Pesanan      : {len(data_modul_pemesanan)} pesanan')
    print(f'Total Pemasukan    : Rp.{total_pemasukan}')
    print(f'Total Pengeluaran  : Rp.{total_pengeluaran}')
    print(f'Saldo              : Rp.{saldo} {"✅ UNTUNG" if saldo > 0 else "❌ RUGI"}')
    print(f'Total Pelanggan    : {len(data_modul_Customer)} orang')
    print(f'Total Barang       : {len(data_modul_inventoris)} item')
    print(f'Stok Menipis       : {len(barang_tipis)} item → {", ".join(barang_tipis) if barang_tipis else "Aman"}')


while True :
    '''MAIN MENU'''
    print('\nMasukan "1" Untuk Modul Pemesanan')
    print('Masukan "2" Untuk Modul Keuangan')
    print('Masukan "3" Untuk Modul Pelanggan')
    print('Masukan "4" Untuk Modul Inventories')
    print('Masukan "5" Untuk Laporan Harian')
    print('Masukan "6" Untuk EXIT')
    print(f'{"="*50:<25}\n')

    main_menu = input("Mohon Masukan Angka : ")
    
    if main_menu == "1" :
        print('\nMasukan "1" Untuk Tambah Pesanan')
        print('Masukan "2" Untuk Lihat Pesanan')
        print('Masukan "3" Untuk Cari Pesanan')
        print('Masukan "4" Untuk Hapus Pesanan')
        print('Masukan "5" Untuk Kembali Ke Menu utama')
        print(f'{"="*50}\n')

        input_modul_pemesanan = input("Mohon Masukan Angka : ")
        if input_modul_pemesanan == "1" :
            Tambah_Pesanan()
        elif input_modul_pemesanan == "2" :
            Lihat_Pesanan()
        elif input_modul_pemesanan == "3" :
            Cari_Pesanan()
        elif input_modul_pemesanan == "4" :
            Hapus_Pesanan()
        elif input_modul_pemesanan == "5" :
          pass
    elif main_menu == "2" :
        print('Masukan "1" Untuk Catat Pengeluaran')
        print('Masukan "2" Untuk Semua Transaksi & Laporan Keuangan')
        print('Masukan "3" Untuk Kembali Ke Menu Utama')
        print(f'{"="*50}\n')

        input_modul_keuangan = input("Mohon Masukan Angka : ")
        if input_modul_keuangan == "1" :
            Catat_Pengeluaran()
        elif input_modul_keuangan == "2" :
            Lihat_Laporan_Keuangan() 
        elif input_modul_keuangan == "3" :
            pass
    elif main_menu == "3" :
        print('Masukan "1" Untuk Tambah Data Customer')
        print('Masukan "2" Untuk lihat & Cari Data Customer')
        print('Masukan "3" Untuk Update Data Customer')
        print('Masukan "4" Untuk Hapus Data Customer')
        print('Masukan "5" Untuk Kembali Ke Menu Utama')
        print(f'{"="*50}\n')

        input_modul_Customer = input("Mohon Masukan Angka :")
        if input_modul_Customer == "1" :
            Tambah_Data_Customer()
        elif input_modul_Customer == "2" :
            print('Masukan "1" Untuk Lihat Data Customer')
            print('Masukan "2" Untuk Cari Data Customer')
            
            input_LdanC = input("Mohon Masukan Angka :")
            if input_LdanC == "1" :
                Lihat_Data_Customer()
            elif input_LdanC == "2" :
                Cari_Data_Customer()
        elif input_modul_Customer == "3" :
            Update_Data_Customer()
        elif input_modul_Customer == "4" :
            Hapus_Data_Customer()
        elif input_modul_Customer == "5" :
            pass
    elif main_menu == "4" :
        print('Masukan "1" Untuk Tambah Barang')
        print('Masukan "2" Untuk Lihat Sisa Stock')
        print('Masukan "3" Untuk Update Jumlah Stock')
        print('Masukan "4" Untuk Melihat Sisa Stock Yang Menipis')
        print('Masukan "5" Untuk Kembali Ke Menu Utama')
        print(f'{"="*50}\n')

        input_modul_inventoris = input("Mohon Masukan Angka : ")
        if input_modul_inventoris == "1" :
            Tambah_Barang()
        elif input_modul_inventoris == "2" :
            Lihat_Data_Stock()
        elif input_modul_inventoris == "3" :
            Update_Stock()
        elif input_modul_inventoris == "4" :
            Check_Stock_Menipis()
        elif main_menu == "5" :
            pass
    elif main_menu == "5" :
        Laporan_Harian()
    elif main_menu == "6" :
        break