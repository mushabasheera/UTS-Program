#UTS-CLO1.2

pilihan_operator = str(input("Pilih: 1[+] / 2[-] / 3[x] / 4[/]: "))

if(pilihan_operator == "1"):
    angka_pertama = float(input("Angka pertama: "))
    angka_kedua   = float(input("angka kedua: "))
    print(angka_pertama + angka_kedua)
elif(pilihan_operator == "2"):
    angka_pertama = float(input("Angka pertama: "))
    angka_kedua   = float(input("angka kedua: "))
    print(angka_pertama - angka_kedua)
elif(pilihan_operator == "3"):
    angka_pertama = float(input("Angka pertama: "))
    angka_kedua   = float(input("angka kedua: "))
    print(angka_pertama * angka_kedua)
elif(pilihan_operator == "4"):
    angka_pertama = float(input("Angka pertama: "))
    angka_kedua   = float(input("angka kedua: "))
    print(angka_pertama // angka_kedua)
else:
        print("Salah inputan!")
    
pilihan_lanjutan = str(input("Lanjutkan lagi? (y/t)"))
#if(pilihan_lanjutan == "y"):
#    continue
#if(pilihan_lanjutan == "t"):
#    break

