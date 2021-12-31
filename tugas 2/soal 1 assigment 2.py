# Assignment 2 21 Februari 2021
nama = []
telepon = []


def show_menu():
    print("=================")
    print("[DATABASE KONTAK]")
    print("[1] Daftar Kontak")
    print("[2] Tambah Kontak")
    print("[3] Keluar")
    print("-----------------")
    select_menu = int(input("Pilih menu: "))

    if(select_menu == 1):
        show_data()
    elif(select_menu == 2):
        req_data()
    elif(select_menu == 3):
        print("Program selesai, sampai jumpa!")
        exit()
    else:
        print("Menu tidak tersedia")
        show_menu()


def show_data():
    if (len(nama) > 0):
        for i in range(len(nama)):
            print("Daftar Kontak:")
            print("Nama: ", nama[i])
            print("No. Telepon: ", telepon[i])
    else:
        print("Belum ada data. Silahkan pilih menu 2!")


def req_data():
    print("Isi data di bawah ini:")
    req_nama = str(input("Nama Anda: "))
    nama.append(req_nama)
    req_telepon = int(input("No. Telepon: "))
    telepon.append(req_telepon)
    print("Kontak berhasil ditambahkan!")


while True:
    show_menu()
# finsih