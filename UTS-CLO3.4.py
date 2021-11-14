from random import randrange
import time

def show_instruction():
    
    print("Selamat datang di permainan Tic-Tac-Toe!")
    print("Anda akan bermain sebagai 'X' dan komputer akan bermain sebagai 'O'. Pilih nomor dibawah untuk bermain")
    print("-"*30)
    print(" ")

kotak1 = False
kotak2 = False
kotak3 = False
kotak4 = False
kotak5 = False
kotak6 = False
kotak7 = False
kotak8 = False
kotak9 = False

def check_kotak():
    if(kotak1 != False and kotak2 != False and kotak3 != False and kotak4 != False and kotak5 != False and kotak6 != False and kotak7 != False and kotak8 != False and kotak9 != False):
        return False
    else:
        return True

def isian_kotak(kotak):
    if(kotak == 1 and kotak1 != False):
        return kotak1
    elif(kotak == 2 and kotak2 != False):
        return kotak2
    elif(kotak == 3 and kotak3 != False):
        return kotak3
    elif(kotak == 4 and kotak4 != False):
        return kotak4
    elif(kotak == 5 and kotak5 != False):
        return kotak5
    elif(kotak == 6 and kotak6 != False):
        return kotak6
    elif(kotak == 7 and kotak7 != False):
        return kotak7
    elif(kotak == 8 and kotak8 != False):
        return kotak8
    elif(kotak == 9 and kotak9 != False):
        return kotak9
    else:
        return str(kotak)

def winner_check():
    if(kotak1 == kotak2 == kotak3):
        return kotak1
    elif(kotak4 == kotak5 == kotak6):
        return kotak4
    elif(kotak7 == kotak8 == kotak9):
        return kotak7
    elif(kotak1 == kotak4 == kotak7):
        return kotak1
    elif(kotak2 == kotak5 == kotak8):
        return kotak2
    elif(kotak3 == kotak6 == kotak9):
        return kotak3
    elif(kotak1 == kotak5 == kotak9):
        return kotak1
    elif(kotak3 == kotak5 == kotak7):
        return kotak3
    else:
        return False
    

def papan_tictactoe():
    """papan tictactoe"""

    print("| ", isian_kotak(1), " | ", isian_kotak(2), " | ", isian_kotak(3), " |")
    print("-------------------")
    print("| ", isian_kotak(4), " | ", isian_kotak(5), " | ", isian_kotak(6), " |")
    print("-------------------")
    print("| ", isian_kotak(7), " | ", isian_kotak(8), " | ", isian_kotak(9), " |")

show_instruction()

while(check_kotak() and winner_check() == False):
    papan_tictactoe()
    

    while True:  
        input_pengguna = input("Mana kotak yang ingin anda isi? (1-9)")
        if(input_pengguna == "1" and kotak1 == False):
            kotak1 = "X"
            break
        elif(input_pengguna == "2" and kotak2 == False):
            kotak2 = "X"
            break
        elif(input_pengguna == "3" and kotak3 == False):
            kotak3 = "X"
            break
        elif(input_pengguna == "4" and kotak4 == False):
            kotak4 = "X"
            break
        elif(input_pengguna == "5"and kotak5 == False):
            kotak5 = "X"
            break
        elif(input_pengguna == "6" and kotak6 == False):
            kotak6 = "X"
            break
        elif(input_pengguna == "7" and kotak7 == False):
            kotak7 = "X"
            break
        elif(input_pengguna == "8" and kotak8 == False):
            kotak8 = "X"
            break
        elif(input_pengguna == "9" and kotak9 == False):
            kotak9 = "X"
            break
        else:
            print("Kotak sudah diisi!")
    
    while True:  
        input_komputer = str(randrange(1,9))
        if(input_komputer == "1" and kotak1 == False):
            kotak1 = "O"
            time.sleep(1)
            break
        elif(input_komputer == "2" and kotak2 == False):
            kotak2 = "O"
            time.sleep(1)
            break
        elif(input_komputer == "3" and kotak3 == False):
            kotak3 = "O"
            time.sleep(1)
            break
        elif(input_komputer == "4" and kotak4 == False):
            kotak4 = "O"
            time.sleep(1)
            break
        elif(input_komputer == "5"and kotak5 == False):
            kotak5 = "O"
            time.sleep(1)
            break
        elif(input_komputer == "6" and kotak6 == False):
            kotak6 = "O"
            time.sleep(1)
            break
        elif(input_komputer == "7" and kotak7 == False):
            kotak7 = "O"
            time.sleep(1)
            break
        elif(input_komputer == "8" and kotak8 == False):
            kotak8 = "O"
            time.sleep(1)
            break
        elif(input_komputer == "9" and kotak9 == False):
            kotak9 = "O"
            time.sleep(1)
            break

pemenang = ""
if(winner_check() == "X"):
    pemenang = "Pemain"
elif(winner_check() == "O"):
    pemenang = "Komputer"

papan_tictactoe()
print("Pemenangnya adalah = " + pemenang + "!")