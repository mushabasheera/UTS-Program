#UTS-CLO2.3

while True:
    print("Batu, Kertas, Gunting - Jankenpon !!!")
    print("")
    print("Pilihlah senjata: [B]atu, [K]ertas, [G]unting")
    anda = str(input("Anda memilih: ")).upper()
    saya = str(input("Saya memilih: ")).upper()

    if(saya == "K" and anda == "G"):
        print("Anda menang!")  
    elif(saya == "G" and anda == "K"):
        print("Saya menang!")
    elif(saya == "G" and anda == "B"):
        print("Anda menang!")
    elif(saya == "B" and anda == "G"):
        print("Batu mengalahkan Gunting, Saya menang!")
    elif(saya == "K" and anda == "B"):
        print("Kertas mengalahkan Batu, Saya menang!")
    elif(saya == "B" and anda == "K"): 
        print("Batu mengalahkan Kertas, Anda menang!")
    elif(saya == "K" and anda == "K"):
        print("Draw, tidak menang dan tidak kalah!")
    elif(saya == "B" and anda == "B"):
        print("Draw, tidak menang dan tidak kalah!")
    elif(saya == "G" and anda == "G"):
        print("Draw, tidak menang dan tidak kalah!")