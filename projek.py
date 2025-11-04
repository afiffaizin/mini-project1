
def tampil_menu():
    print("\nMenu")
    print("1. Array 1D")
    print("2. Array 2D (belum dibuat)")
    print("3. Exit")


def array_1d():
    while True:  # perulangan khusus untuk array 1D
        jumlahData = []
        nilai = int(input("Masukkan jumlah data: "))
        for i in range(nilai):
            data = int(input(f"Masukkan data ke-{i+1}: "))
            jumlahData.append(data)

        print("\nData yang dimasukkan:")
        for i in range(len(jumlahData)):
            print(f"Data angka ke-{i+1}: {jumlahData[i]}")

        total = sum(jumlahData)
        print(f"Total data: {total}")
        rata = total / len(jumlahData)
        print(f"Rata-rata data: {rata}")
        nilaiMax = max(jumlahData)
        nilaiMin = min(jumlahData)

        print (f"nilai max adalah: {nilaiMax}")
        print (f"nilai min adalah: {nilaiMin}")

        ulang = input("\nUlangi input Array 1D? (y/t): ").lower()
        if ulang != "y":
            break   # keluar dari menu Array 1D



def array_2():
    matrix = []
    baris = int(input("Masukkan jumlah baris: "))
    kolom = int(input("Masukkan jumlah kolom: "))

    for i in range(baris):
        row = []  # buat list kosong untuk baris baru
        for j in range(kolom):
            elemen = int(input(f"Masukkan baris ke [{i+1}] dan kolom ke[{j+1}]: "))
            row.append(elemen)  # setiap input dimasukkan ke baris
        matrix.append(row)  # setelah selesai 1 baris, masukkan ke matrix

    print("\nMatriks yang dimasukkan:")
    for r in matrix:
        print(r)

    total = sum(sum(row) for row in matrix)
    print(f"total semua elemen adalah: {total}")
    rata = total / (len(matrix) * len(matrix[0]))
    print(f"rata rata adalah: {rata}")
    nilaiMax = max(max(row) for row in matrix)
    print (f"nilai max adalah: {nilaiMax}")


    
        


# --- Program utama ---
while True:
    tampil_menu()
    pilihan = int(input("Masukkan pilihan Anda (1/2/3): "))

    match pilihan:
        case 1:
            array_1d()
            
        case 2:
            array_2()
        case 3:
            print("Terima kasih! Program selesai.")
            break
        case x :
            print("Pilihan tidak valid, coba lagi.")
            
