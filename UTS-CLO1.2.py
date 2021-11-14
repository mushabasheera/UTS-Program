#UTS-CLO1.2

while True: 
    print("Pilihlah Operasi pada Kalkulator: ", "1. Penjumlahan", "2. Pengurangan", "3. Perkalian", "4. Pembagian",sep="\n")
    pilihan_operator = str(input("Pilih: 1[+] / 2[-] / 3[x] / 4[/]: ")) #input untuk memilih pilihan_operator

    #sesuai dengan pilihan, 1 = angka_pertama ditambah angka_kedua
    if(pilihan_operator == "1"):
        angka_pertama = float(input("Angka pertama: "))
        angka_kedua   = float(input("angka kedua: "))
        print(angka_pertama + angka_kedua) 
    
    #pilihan nomor 2 = angka_pertama dikurang angka_kedua
    elif(pilihan_operator == "2"):
        angka_pertama = float(input("Angka pertama: "))
        angka_kedua   = float(input("angka kedua: "))
        print(angka_pertama - angka_kedua)  
    
    #pilihan nomor 3 = angka_pertama dikali angka_kedua
    elif(pilihan_operator == "3"):
        angka_pertama = float(input("Angka pertama: "))
        angka_kedua   = float(input("angka kedua: "))
        print(angka_pertama * angka_kedua) 

    #pilihan nomor 4 = angka_pertama dibagi angka_kedua
    elif(pilihan_operator == "4"):
        angka_pertama = float(input("Angka pertama: "))
        angka_kedua   = float(input("angka kedua: "))
        print(angka_pertama // angka_kedua) 
    
    #jika pilihan salah (bukan 1, 2, 3 atau 4 maka perintah else akan dijalankan)
    else:
        print("Salah input!")
        continue
    
    #setelah penghitungan selesai, user akan diberi pilihan untuk lanjut atau tidak
    pilihan_lanjutan = str(input("Lanjutkan lagi? (y/t)"))
    if(pilihan_lanjutan == "y"):
        continue                    #melanjutkan while
    elif(pilihan_lanjutan == "t"):
        break                       #membuat while berhenti