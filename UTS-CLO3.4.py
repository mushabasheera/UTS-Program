from random import randint
import datetime

print("-------------")
print("| 1 | 2 | 3 |")
print("-------------")
print("| 4 | 5 | 6 |")
print("-------------")
print("| 7 | 8 | 9 |")
print("-------------")
print("Selamat datang di permainan Tic-Tac-Toe!")
print("Anda akan bermain sebagai 'X' dan komputer akan bermain sebagai 'O'. Pilih nomor dibawah untuk bermain")

def papan_tictactoe():
    jawaban_pemain = [0,1,2,3,4,5,6,7,8,9]
    print("| ", jawaban_pemain([1]), " | ", jawaban_pemain([2]), " | ", jawaban_pemain([3]), " |")
    print("-------------")
    print("| ", jawaban_pemain([4]), " | ", jawaban_pemain([5]), " | ", jawaban_pemain([6]), " |")
    print("-------------")
    print("| ", jawaban_pemain([7]), " | ", jawaban_pemain([8]), " | ", jawaban_pemain([9]), " |")

def check_kotak():
    check = False
    while not check_kotak:
        
     check_kotak == False:
        print("Kotak sudah diisi!")

def winner():
    x = "Pemain"
    o = "Komputer"
    win_combos = [[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[3,6,9],[2,5,8]]
    
    
    

    


