#UTS-CLO2.3

start_game = str(input("Mulai permainan? (y/t)"))

while(start_game == "y"):
    print("Batu, Kertas, Gunting - Jankenpon !!!")
    print("")
    print("Pilihlah senjata: [B]atu, [K]ertas, [G]unting")
    anda = str(input("Anda memilih: "))
    saya = str(input("Saya memilih: "))

    if(saya == "K" and anda == "G"):
        print("Anda menang!")  
        start_again = str(input("Lanjutkan permainan? (y/t)"))
        if(start_again == "y"): 
            continue
        elif(start_again == "t"):
            break
        else:
            print("Input salah!")
    elif(saya == "G" and anda == "K"):
        print("Saya menang!")
        print("Anda menang!")  
        start_again = str(input("Lanjutkan permainan? (y/t)"))
        if(start_again == "y"): 
            continue
        elif(start_again == "t"):
            break
        else:
            print("Input salah!")
    elif(saya == "G" and anda == "B"):
        print("Anda menang!")
        print("Anda menang!")  
        start_again = str(input("Lanjutkan permainan? (y/t)"))
        if(start_again == "y"): 
            continue
        elif(start_again == "t"):
            break
        else:
            print("Input salah!")
    elif(saya == "B" and anda == "G"):
        print("Batu mengalahkan Gunting, Saya menang!")
        print("Anda menang!")  
        start_again = str(input("Lanjutkan permainan? (y/t)"))
        if(start_again == "y"): 
            continue
        elif(start_again == "t"):
            break
        else:
            print("Input salah!")
    elif(saya == "K" and anda == "B"):
        print("Kertas mengalahkan Batu, Saya menang!")
        print("Anda menang!")  
        start_again = str(input("Lanjutkan permainan? (y/t)"))
        if(start_again == "y"): 
            continue
        elif(start_again == "t"):
            break
        else:
            print("Input salah!")
    elif(saya == "B" and anda == "K"): 
        print("Batu mengalahkan Kertas, Anda menang!")
        print("Anda menang!")  
        start_again = str(input("Lanjutkan permainan? (y/t)"))
        if(start_again == "y"): 
            continue
        elif(start_again == "t"):
            break
        else:
            print("Input salah!")
    elif(saya == "K" and anda == "K"):
        print("Draw, tidak menang dan tidak kalah!")
        print("Anda menang!")  
        start_again = str(input("Lanjutkan permainan? (y/t)"))
        if(start_again == "y"): 
            continue
        elif(start_again == "t"):
            break
        else:
            print("Input salah!")
    elif(saya == "B" and anda == "B"):
        print("Draw, tidak menang dan tidak kalah!")
        print("Anda menang!")  
        start_again = str(input("Lanjutkan permainan? (y/t)"))
        if(start_again == "y"): 
            continue
        elif(start_again == "t"):
            break
        else:
            print("Input salah!")
    elif(saya == "G" and anda == "G"):
        print("Draw, tidak menang dan tidak kalah!")
        print("Anda menang!")  
        start_again = str(input("Lanjutkan permainan? (y/t)"))
        if(start_again == "y"): 
            continue
        elif(start_again == "t"):
            break
        else:
            print("Input salah!")