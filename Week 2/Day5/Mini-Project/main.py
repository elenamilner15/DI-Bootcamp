# Mini-Project - Tic Tac Toe
board=list(range(1,10))


def display_board():
    print("-" * 13)    
    for i in range(3):         
        print("|", board[i*3+0], "|", board[i*3+1], "|", board[i*3+2],"|")
        print("-" * 13)

def player_input(player):
    while True:
        value = int(input("In which cell to put " +player +"?\n"))
        
        if value not in range(1,10):
            print("Error. Please enter the number 1..9")
            continue
        else:
            #value=int(value)
            if str(board[value-1]) =="x" or str(board[value-1]) =="o":
                print("This cell is occupied")
                continue
            board[value-1]=player
            break

def check_win(board, player):
    for row in range(0, 9, 3):      
        if all([board[row + i] == player for i in range(3)]):
            return True

    for col in range(3):       
        if all([board[row + col] == player for row in range(0, 9, 3)]):
            return True

    if all([board[i] == player for i in range(0, 9, 4)]) or all([board[i] == player for i in range(2, 7, 2)]):
        return True

    return False    
 #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

players = ["x", "o"]

def play():
    counter=0   
    while True:        
        display_board()        
        if counter %2 ==0:
            player='x'         
        else:
            player='o'            
        player_input(player)
        
        if counter >3:
            winner=check_win(board, player) #!!!!!!!!!!!!!!!!!!
            if winner:
                display_board()
                print(player, "won")
                break
        counter +=1
        if counter >8:
            display_board()
            print("Nobody won")
            break
play()
                
                   
                
       


