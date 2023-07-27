import random

class Game():
    def __init__() -> None:
        pass
list_items = ["r", "p", "s"]
game_results = []  # Initialize an empty list to store game results
# total_games = 0     # Initialize total_games variable
      
def get_user_item():    
    while True:
        try:     
            item = input("Input r - for rock, p - for paper, s - for scissors:  ")
            if item in list_items:
                print(item)
                return(item)            
            else:
                print("Invalid input. Try again")
                continue  
        except ValueError:
            print("Error: Please enter again.")


def get_computer_item():
    random_item = random.choice(list_items)
    # print(random_item)
    return(random_item)



def get_game_result(item, random_item):
    pair=[item, random_item]
   
    if pair in [["p", "r"],["s", "p"], ["r", "s"]]:
        return ("win")
    elif pair in [["r", "p"], ["p", "s"], ["s", "r"]]:
        return ("lose")
    else:
        return ("draw")
    
from rock_paper_scissors import get_user_menu_choice
from rock_paper_scissors import print_results

def play():    
    # global total_games  # Use the global variable total_games inside the function
    # total_games += 1    # Increment the total_games variable
    
    player_choice = get_user_item()
    print("You chose:", player_choice)
    computer_choice = get_computer_item()
    print("Computer selected:", computer_choice)
    result = get_game_result(player_choice, computer_choice)
    print(f"Result:  {result}")   
    game_results.append(result)
    
  
    
def main():
    while True:
        choice = get_user_menu_choice()
        if choice == "Play a new game":           
            play()
            
        elif choice == "Show scores and Quit":
            print_results(game_results) 
            break       
        else:
            print("Invalid choice.")
                

main()

  

