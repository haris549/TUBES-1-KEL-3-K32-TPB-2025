# Program Coffee Machine


# Kamus
# bahan : list[int]
# resep : list[list[int]]
# ulang : str
# x, res, index, mainten, refill, tambahan, isiulang : int


#Algoritma
bahan = [2000, 5000, 3000]  # [kopi (gram), air (ml), susu (ml)] 


# resep kopi: [kopi, air, susu]
resep = [
    [8, 30, 0],    # Espresso
    [16, 250, 0],   # Americano
    [16, 60, 228], # Latte
    [16, 60, 152]  # Cappuccino
]

x = 1 # Kondisi pengulangan

while x == 1:
    res = int(input("Masukkan jenis kopi: Espresso[1], Americano[2], Latte[3], Cappuccino[4]: "))               # Input Kode untuk menu kopi atau maintenance

    if 1 <= res <= 4:
        index = res - 1                                                                                         # Penyesuaian kode dengan syntax index pada array
        if (bahan[0] >= resep[index][0]) and (bahan[1] >= resep[index][1]) and (bahan[2] >= resep[index][2]):       
            bahan[0] -= resep[index][0]
            bahan[1] -= resep[index][1]
            bahan[2] -= resep[index][2]                                                                         # Eksekusi Pembuatan Kopi

            print("Kopi tersedia,", ["Espresso", "Americano", "Latte", "Cappuccino"][index], "siap disajikan")
            ulang = str(input("Apakah anda ingin membuat kopi lagi? (Y/N)\n"))
            if ulang == "Y":                                                                                    # Input user untuk mengulang program
                x = 1
            elif ulang == "N":
                x = 0
        else:
            print("*ERROR* Kopi tidak tersedia")
    
    elif res == 0:                                                                                              # Kode untuk maintenance
        mainten = int(input("Ketik 1 untuk refill bahan, ketik 2 untuk membersihkan mesin, ketik 3 untuk menampilkan storage \n"))
        if mainten == 1:    
            refill = int(input("Apa yang mau diisi ulang: Kopi[1], Susu[2], Air[3]: "))                         # Eksekusi isi ulang storage
            tambahan = int(input("Berapa banyak yang mau diisi?: "))
            if 1 <= refill <= 3:
                bahan[refill - 1] += tambahan
                if bahan[0] > 2000:
                    print("Kopi melebihi kapasitas mesin")
                    bahan[0] -= tambahan                                                     # Kondisi apabila melebihi kapasitas mesin
                if bahan[1] > 5000:
                    print("Air melebihi kapasitas mesin")
                    bahan[1] -= tambahan
                if bahan[2] > 3000:
                    print("Susu melebihi kapasitas mesin")
                    bahan[2] -= tambahan
    

        elif mainten == 2 and bahan[1] >= 1000:                                                                 # Eksekusi pembersihan mesin
            print("Self Cleaning selesai")
            bahan[1] -= 1000
        elif mainten == 2 and bahan[1] < 1000:
            print("Air tidak cukup, isi air dibutuhkan")
            while bahan[1] < 1000:
                isiulang = int(input(f"Masukkan air sebanyak {1000-bahan[1]}ml untuk proses pembersihan mesin: "))
                bahan[1] += isiulang
                
            print("Self Cleaning selesai")

        elif mainten == 3:                                                                                      # Eksekusi penampilan storage dari mesin
            print(f"Kopi : {bahan[0]} gram, Air : {bahan[1]} ml, Susu : {bahan[2]} ml")
        ulang = str(input("Apakah anda ingin membuat kopi? (Y/N)\n"))
        if ulang == "Y":
            x = 1
        elif ulang == "N":
            x = 0
        else:
            print("*ERROR* Kode yang dimasukkan tidak valid")
   
    else:
        print("*ERROR* Kode yang dimasukkan tidak valid")



print("Terimakasih telah menggunakan mesin kopi")                                                               # Terminasi
