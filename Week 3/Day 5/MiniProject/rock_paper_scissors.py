def get_user_menu_choice():
    while True:
        print("Menu:")
        print("(g) Play a new game")
        print("(q) Show scores and Quit")

        choice = input("Enter your choice (g or q): ")

        if choice == "g":
            return "Play a new game"
        elif choice == "q":
            return "Show scores and Quit"            
        else:
            print("Invalid choice. Please enter g or q.")
           
# from game import play

def print_results(game_results):    
 
    win_count = game_results.count("win")
    lose_count = game_results.count("lose")
    draw_count = game_results.count("draw")
    
    game_results = (f"You won: {win_count},\n You lost: {lose_count},\n You drew {draw_count}")
    print("Game Results:")
    print(game_results)
  
 
    
    


