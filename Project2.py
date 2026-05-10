
# MINI PROJECT 002
# CashFlow Tracker - Daily Income & Expense Recorder

import random
import string
import os
os.system("cls")

new_list = {}

def header() :
    print(f'{"SVORPROJECT002":^40}')
    print(f'{"SISTEM PENCATATAN KEUANGAN HARIAN":^40}')
    print(f'{"="*40:^40}')


def income() :
    global new_list

    K= input("Masukan jenis pemasukan = ")
    H= int(input("Masukan jumlah pemasukan = "))
    ascii = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))

    new_list[ascii] = {
        "Tipe"  : "Pemasukan",
        "keterangan" : K,
        "harga" : H,
    }

def outcome() :
    global new_list

    K = input("Masukan jenis pengeluaran = ")
    H = int(input("Masukan jumlah pengeluaran = "))
    ascii = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))

    new_list[ascii] = {
        "Tipe"  : "Pengeluaran",
        "keterangan" : K,
        "harga" : H,
    }

def Lihat_transaksi() :
    global new_list
    
    print(f'{"ID":<7} {"Tipe":<12} {"Jenis":<15} {"Jumlah":<12}')
    print("="*50)

    for keys, nilai in new_list.items() :
        print(f'{keys:<7} {nilai["Tipe"]:<12} {nilai["keterangan"]:<15} {nilai["harga"]:<9}')


def total_pendapatan() :
    global new_list
    
    total_pemasukan = 0
    total_pengeluaran = 0

    for keys, nilai in new_list.items() :
        if nilai["Tipe"] == "Pemasukan" :
            total_pemasukan += nilai["harga"]
        elif nilai["Tipe"] == "Pengeluaran" :
            total_pengeluaran += nilai["harga"]
    print(f'Total Pemasukan Hari Ini Adalah = Rp.{total_pemasukan}')
    print(f'Total Pengeluaran Hari Ini Adalah = Rp.{total_pengeluaran}')
    print(f"{'='*50}")

    saldo = total_pemasukan - total_pengeluaran
    if saldo > 0 :
        print(f"Pendapatan hari ini = ✅ UNTUNG")
    elif saldo < 0 :
        print(f'Pendapatan hari ini = ❌ RUGI')
    else :
        print(f'Pendapatan hari ini = IMPAS')
    print(f'Sisa Saldo Akhir = {saldo}')
        


while True :
    header()
    print('ketik "1" Untuk input Pemasukan dan Pengeluaran')
    print('ketik "2" Untuk Lihat Data Transaksi')
    print('ketik "3" Untuk Laporan Hari ini')
    print(f'{"="*40}\n')

    input_nomor = input('Mohon Masukan Nomor = ')
    if input_nomor == "1" :
        in_out = input("input Pemasukan / pengeluaran (i/o) = ")
        if in_out == "i" :
            income()
        elif in_out == "o" :
            outcome()
    elif input_nomor == "2" :
        Lihat_transaksi()
    elif input_nomor == "3" :
        total_pendapatan()

            
    