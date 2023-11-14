import os
while True:
    jumlah = int(input("Masukkan jumlah anak ayam :"))
    for i in range (jumlah,1,-1):
        print(f"Anak ayam turunlah {i} mati satu tinggal lah {i-1}")
    print(f"Anak ayam turun lah {i-1} mati satu tinggal induknya")

    again = input("apakah anda ingin mengulang lagu anak ayam? [y/n] ")
    if again.lower() == "n":
        print("Terima Kasih")
        break
    elif again.lower == "y":
        os.system ("clear")
        continue