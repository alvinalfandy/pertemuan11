list = {}

def garis():
    '''Fungsi garis'''
    print("~"*78)

    # Menambahkan data inputan 
def tambah():
    print("Tambah data :\n")
    nama    = input("Nama           : ")
    nim     = int(input("NIM            : "))
    uts     = int(input("Nilai UTS      : "))
    uas     = int(input("Nilai UAS      : "))
    tugas   = int(input("Nilai Tugas    : "))
    akhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)
    list[nama] = [nim, tugas, uts, uas, akhir]

    # Mengubah data inputan
def ubah():
    print("Ubah Data :")
    nama = input("\nMasukkan Nama  : ")
    if nama in list.keys():
        nim     = int(input("NIM            : "))
        uts     = int(input("Nilai UTS      : "))
        uas     = int(input("Nilai UAS      : "))
        tugas   = int(input("Nilai Tugas    : "))
        akhir = (tugas * 30/100) + (uts * 35/100) + (uas * 35/100)
        list[nama] = [nim, tugas, uts, uas, akhir]
    else:
        print("NAMA {0} TIDAK ADA!".format(nama))

    # Menghapus inputan Nama
def hapus():
    print("Hapus berdasarkan nama inputan :")
    nama = input("\nMasukkan Nama  : ")
    if nama in list.keys():
        del list[nama]
        print("\nData {0} berhasil di hapus".format(nama))
    else:
        print("NAMA {0} TIDAK ADA!".format(nama))
    
    # Mencari data yg sudah di input
def cari():
    print("Cari data berdasarkan nama inputan :")
    nama = input("\nMasukkan Nama : ")
    if nama in list.keys():
        print(f"\nNama        : {nama}")
        print(f"NIM         : {list[nama][0]}")
        print(f"Nilai UTS   : {list[nama][2]}")
        print(f"Nilai UAS   : {list[nama][3]}")
        print(f"Nilai Tugas : {list[nama][1]}")                  
        print(f"Nilai Akhir : {list[nama][4]}") 
    else:
        print("NAMA {0} TIDAK ADA!".format(nama))
    
    # Menampilkan seluruh data 
def lihat():
    if list.items():
        print("-"*78)
        print("|                               Daftar Mahasiswa                             |")
        print("-"*78)                 
        print("| No |       Nama      |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
        print("="*78)
        i = 0
        for data in list.items():
            i += 1
            print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                .format(data[0][:13], data[1][0], data[1][2], data[1][3], data[1][1], data[1][4], no=i))
            print("-"*78)
    else:
        print("-"*78)
        print("|                               Daftar Mahasiswa                             |")
        print("-"*78)
        print("|No. | Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
        print("-"*78)
        print("|                       TIDAK ADA DATA! Silakan tambah data                  |")
        print("-"*78)


print("="*20)
print("|PROGRAM INPUT DATA|")
print("="*20)

while True: 
    print()
    menu = input("[(T)ambah, (U)bah, (H)apus, (C)ari, (L)ihat, (K)eluar] : ")
    garis()
    print()

    if menu.lower() == 't':
        tambah()

    elif menu.lower() == 'u':
        ubah()       

    elif menu.lower() == "h":
        hapus() 

    elif menu.lower() == "c":
        cari()

    elif menu.lower() == "l":
        lihat() 

    elif menu.lower() == "k":
        print("Program selesai, Terima Kasih :) ")
        break

    else:
        print("\n INPUT {} TIDAK ADA!, Silakan pilih [T/U/H/C/L] untuk menjalankan program!".format(menu))