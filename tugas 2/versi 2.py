semua_con = {}
def ambil_data():
	banyak_data = int(input("Berapa banyak data yang ingin dimasukkan: "))
	for i in range(banyak_data):
		print("+==========================+")
		input_nama = str(input("Nama Kontak: "))
		input_no = input("Nomor Telpon: ")
		semua_con[input_nama] = input_no
		print("Kontak Berhasil Ditambahkan!")
def tunjuk_data():
	for i in semua_con:
		print('+====================+')
		print(f"Nama Kontak: {i}")
		print(f"No Telpon: {semua_con[i]}")
while True:
	print("----Menu----")
	print("1. Daftar Kontak")
	print("2. Lihat Kontak")
	print("3. Keluar")
	print( )
	pilihan = int(input("Pilih Menu: "))
	if pilihan == 1:
		ambil_data()
	elif pilihan == 2:
		tunjuk_data()
	elif pilihan == 3:
		print("Program Selesai, Sampai Jumpa!")
		break
	else:
		print("Menu Tidak Ditemukan!")
		pass