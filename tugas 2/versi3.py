semua_kontak = {}
# 0 2 4  6  8  10 12 14 16 18 20 22 <- total contacts
# 1 2 3  
#       -2 -3 -4 -5 -6 -7 -8 -9 -10 <- subtraction to get goal
#        4  5  6   7  8  9 10 11 12 <- Goal
# Final equation = x-(x/2-1)
def daftar_kon():
	banyak_data = int(input("Berapa banyak data yang ingin dimasukkan: "))
	for i in range(banyak_data):
		def math_func(x=len(semua_kontak)):
			# Equation = x - (x/2-1)
			return x - (x//2-1)
		print("+==========================+")
		input_nama = str(input("Nama Kontak: "))
		input_no = input("Nomor Telpon: ")
		semua_kontak["Nama"+str(math_func())] = input_nama
		semua_kontak["NoTelp"+str(math_func())] = input_no
		print("Kontak Berhasil Ditambahkan!")
def lihat_kontak():
	x,i = len(semua_kontak)//2,0 #Equation = (x/2)
	while i < x:
		i += 1
		print("+============================+")
		print("Nama: {}".format(semua_kontak['Nama'+str(i)]))
		print("No. Telepon: {}".format(semua_kontak['NoTelp'+str(i)]))
		print("+============================+")
print("Selamat Datang!")
while True:
	print("----Menu----")
	print("1. Daftar Kontak")
	print("2. Lihat Kontak")
	print("3. Keluar")
	print( )
	pilihan = int(input("Pilih Menu: "))
	if pilihan == 1:
		daftar_kon()
	elif pilihan == 2:
		lihat_kontak()
	elif pilihan == 3:
		print("Program Selesai, Sampai Jumpa!")
		break
	else:
		print("Menu Tidak Ditemukan!")
		pass