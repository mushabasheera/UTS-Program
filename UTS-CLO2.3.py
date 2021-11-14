#UTS-CLO2.3

while True:
    print("Batu, Kertas, Gunting - Jankenpon !!!")
    print("")
    print("Pilihlah senjata: [B]atu, [K]ertas, [G]unting")

    #variabel input dari user
    anda = str(input("Anda memilih: ")).upper()
    saya = str(input("Saya memilih: ")).upper()

    #penentuan kalah dan menang
    if(saya == "K" and anda == "G"):
        print("Gunting mengalahkan Kertas, Anda menang!")  
    elif(saya == "G" and anda == "K"):
        print("Gunting mengalahkan Kertas, Saya menang!")
    elif(saya == "G" and anda == "B"):
        print("Batu mengalahkan Gunting, Anda menang!")
    elif(saya == "B" and anda == "G"):
        print("Batu mengalahkan Gunting, Saya menang!")
    elif(saya == "K" and anda == "B"):
        print("Kertas mengalahkan Batu, Saya menang!")
    elif(saya == "B" and anda == "K"): 
        print("kertas mengalahkan Batu, Anda menang!")
    elif(saya == "K" and anda == "K"):
        print("Draw, tidak menang dan tidak kalah!")
    elif(saya == "B" and anda == "B"):
        print("Draw, tidak menang dan tidak kalah!")
    elif(saya == "G" and anda == "G"):
        print("Draw, tidak menang dan tidak kalah!")
    else:
        print("Input salah")
    
    #berfungsi untuk membuat pemisah antar game
    print("-" * 60)
    print("")