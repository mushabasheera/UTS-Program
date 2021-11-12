#UTS-CLO2.3

def main_game():
    def start_again():
            """Berfungsi untuk menampilkan opsi lanjutkan permainan"""
            start_again = str(input("Lanjutkan permainan? (y/t)")).lower()
            if(start_again == "y"): 
                main_game()
        
    print("Batu, Kertas, Gunting - Jankenpon !!!")
    print("")
    print("Pilihlah senjata: [B]atu, [K]ertas, [G]unting")
        
    #Variabel 'anda' dan 'saya'
    anda = str(input("Anda memilih: ")).upper()
    saya = str(input("Saya memilih: ")).upper()
        
    if(saya == "K" and anda == "G"):
        print("Anda menang!")  
        start_again()

    elif(saya == "G" and anda == "K"):
        print("Saya menang!")
        start_again()

    elif(saya == "G" and anda == "B"):
        print("Anda menang!")
        start_again()

    elif(saya == "B" and anda == "G"):
        print("Batu mengalahkan Gunting, Saya menang!")
        start_again()
            
    elif(saya == "K" and anda == "B"):
        print("Kertas mengalahkan Batu, Saya menang!")
        start_again()

    elif(saya == "B" and anda == "K"): 
        print("Batu mengalahkan Kertas, Anda menang!")
        start_again()

    elif(saya == "K" and anda == "K"):
        print("Draw, tidak menang dan tidak kalah!")
        start_again

    elif(saya == "B" and anda == "B"):
        print("Draw, tidak menang dan tidak kalah!")
        start_again()

    elif(saya == "G" and anda == "G"):
        print("Draw, tidak menang dan tidak kalah!")
        start_again()

    elif(saya != "K" or saya != "G" or saya != "B" and anda != "K", anda != "B", anda != "G"):
        print("Input salah!")

#Execute the main command
main_game()