import os
again = "y"
while (again.lower() == 'y'):   

    print("------------------------------------------------------------------------------------------")
    print("|                            DATA MASKAPAI PENERBANGAN                                   |")
    print("------------------------------------------------------------------------------------------")
    print("|                                                                                        |")
    print("|                                                                                        |")
    print("| Kode Maskapai     Nama Maskapai     Kode Kelas      Nama Kelas           Harga         |")
    print("|-                                                                                      -|")
    print("|      A               Garuda             1            Eksekutif        Rp.3.000.000     |")
    print("|                                         2            Bisnis           Rp.2.000.000     |")
    print("|                                         3            Ekonomi          Rp.1.000.000     |")
    print("|      B               Lion Air           1            Eksekutif        Rp.2.500.000     |")
    print("|                                         2            Bisnis           Rp.1.500.000     |")
    print("|                                         3            Ekonomi          Rp.800.000       |")
    print("|                                                                                        |")
    print("|----------------------------------------------------------------------------------------|")

 # Input
    nama = (input("Masukkan Nama Pemesan          :"))
    kode_maskapai = (input("Masukkan Kode Maskapai [A/B]   :"))
    kode_kelas = (input("Masukkan Kode Kelas   [1/2/3] :"))
    beli = int (input("Masukkan Jumlah Beli           :"))

 # Proses

    if (kode_maskapai == "A") or (kode_maskapai == "a"):
        nama_maskapai = "Garuda Airlines"
        if (kode_kelas == "1"):
            nama_kelas = "Eksekutif"
            harga = 3000000
        elif (kode_kelas == "2"):
            nama_kelas = "Bisnis"
            harga = 2000000
        elif (kode_kelas == "3"):
            nama_kelas = "Ekonomi"
            harga = 1000000
        else:
            kode_kelas = "Kode kelas tidak di temukan!"

    if (kode_maskapai == "B") or (kode_maskapai == "b"):
        nama_maskapai = "Lion Air"
        if (kode_kelas == "1"):
            nama_kelas = "Eksekutif"
            harga = 2500000
        elif (kode_kelas == "2"):
            nama_kelas = "Bisnis"
            harga = 1500000
        elif (kode_kelas == "3"):
            nama_kelas = "Ekonomi"
            harga = 800000
        else:
            kode_kelas = "Kode kelas tidak di temukan!"


 # Output
    print("---------------------------------------------------------------------------------------")
    print(              "DATA PEMBAYARAN PEMESANAN TIKET PENERBANGAN KE YOGYAKARTA"                )
    print("---------------------------------------------------------------------------------------")
    print("Maskapai penerbangan yang anda pilih adalah :",nama_maskapai)
    print("dengan kelas penerbangan",nama_kelas)
    print("Jumlah Tiket yang di pesan :",beli)
    print("Harga Satuan Tiket         :", harga)
    print("Total Pembayaran           :",harga*beli)
    print("---------------------------------------------------------------------------------------")
    print(f"Terima Kasih {nama} atas transaksi yang anda lakukan")
    print(">>>\n")

    again = input("Apakah anda ingin memesan tiket lagi? [y/n] ")
    if (again.lower() == 'y'):
         os.system("cls")
         continue
    elif (again.lower() == 'n'):
         print(f"Terima kasih!")
         os.system("cls")