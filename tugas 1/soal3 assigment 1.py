ujian_teori = int(input("masukkan nilai teori: "))
ujian_praktek = int(input("masukkan nilai praktek: "))
if ujian_teori >= 70 and ujian_praktek >= 70:
    print("selamat anda lulus!")
elif ujian_teori >= 70 and ujian_praktek < 70:
    print("anda harus mengulang ujian praktek!!.")
elif ujian_teori < 70 and ujian_praktek >= 70:
    print("anda harus mengulang ujian teori!!")
else:
    print("anda harus mengulang ujian teori dan praktek!!!.")