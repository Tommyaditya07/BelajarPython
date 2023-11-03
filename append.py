import os
pajak = 0.15
again = True
while again:
    print("==================================================")
    print(" KODE HOTEL                  NAMA HOTEL       ")
    print("      1                   Hotel Maju Mundur   ")
    print("      2                   Hotel Tanpa Nama    ")
    print("==================================================")
    print(" KODE KAMAR         JENIS KAMAR            HARGA  ")
    print("     1                   VP              Rp.500.000")
    print("     2                  VIP              Rp.750.000")
    print("     3                 VVIP              Rp.2.500.000")
    print("==================================================")
    
    kode_hotel = []
    kode_kamar = []
    banyak_kamar = []
    lama = []
    banyak_jenis = int(input("Masukkan banyak jenis :"))
    
    for i in range (banyak_jenis):
        # Input
        print(f"Pesanan ke-{i+1}")
        kode_hotel.append(input("Masukkan kode Hotel :"))
        kode_kamar.append(input("Masukkan kode kamar :"))
        banyak_kamar.append(int(input("Masukkan banyak kamar :")))
        lama.append(int(input("Berapa lama anda ingin menginap? :"))) 

        # Proses
        if kode_hotel [i] == "1":
            nama_hotel ="Hotel Maju Mundur"
            if kode_kamar [i] == "1":
                jenis_kamar = "VP"
                harga = int(500000)
            elif kode_kamar [i] == "2":
                jenis_kamar = "VIP"
                harga = int(750000)
            elif kode_kamar.append [i] == "3":
                jenis_kamar = "VVIP"
                harga = int(2500000)
            else:
                print("Kode kamar tidak di temukan!")

        elif kode_hotel [i] == "2":
            nama_hotel = "Hotel Maju Mundur"
            if kode_kamar [i] == "1":
                jenis_kamar = "VP"
                harga = int(500000)
            elif kode_kamar [i] == "2":
                jenis_kamar = "VIP"
                harga = int(750000)
            elif kode_kamar [i] == "3":
                jenis_kamar = "VVIP"
                harga = int(2500000)
            else:
                kode_kamar = "Kode kamar tidak di temukan!"
                break

        else:
            print("Kode hotel tidak di temukan!")
            continue

        # Menghitung lama
        if (lama[i]) > 3:
            diskon = int (harga*0.03) - harga
        elif (lama[i]) > 5:
            diskon = int (harga*0.07) - harga
        else:
            diskon = 0

        # Proses Hitung Harga
        total_harga = int(lama[i] * banyak_kamar[i] * harga)
        total_bayar = int (total_harga * pajak) - diskon
        
        print("====================================================================")
        print("                         STRUK PEMBAYARAN                           ")
        print("====================================================================")
        print(f"Anda memesan kamar di {nama_hotel} dengan jenis kamar {jenis_kamar}")
        print(f"Harga satuan kamar hotel sebesar Rp.{harga}")
        print(f"Anda memesan {banyak_kamar} kamar")
        print(f"Harga yang harus anda bayar sebesar Rp.{total_bayar}")
        print("====================================================================")
        ubay = int(input("Masukkan uang bayar Rp."))
        ukem = total_bayar - ubay
        print(f"Uang kembalian anda Rp.{ukem}")
    
    again = input("Apakah anda ingin memesan hotel lagi? [y/n]")
    if (again.lower() == "n"):
        print("Terima kasih!")
        os.system ("cls")
        break
    elif (again.lower() == "y"):
        print("Terima kasih!")
        os.system ("cls")
        continue
