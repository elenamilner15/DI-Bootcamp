import psycopg2
from menu_item import MenuItem
from menu_manager import MenuManager
from db_connection import connect_to_db

def show_user_menu():
    print("Menu Options:")
    print("V: View an Item")
    print("A: Add an Item")
    print("D: Delete an Item")
    print("U: Update an Item")
    print("S: Show the Menu")

    choice = input("Enter your choice: \n").lower()
    
    if choice == 'v':
        show_item()
    elif choice == 'a':
        add_item_to_menu()
    elif choice == 'd':
        remove_item_from_menu()
    elif choice == 'u':
        update_item_from_menu()
    elif choice == 's':
        show_menu()
    else:
        print("Invalid choice. Please choose a valid option.")   
       
def add_item_to_menu():
    item_name = input("Enter the item name: ")
    item_price = int(input("Enter the item price: "))
    item = MenuItem(item_name, item_price)
    item.save()
    print("Item was added successfully.")

def remove_item_from_menu():
    item_name = input("Enter the item name to remove: ")
    item = MenuItem(item_name, None)
    item.delete()
    print("Item was deleted successfully.")

def update_item_from_menu():
    item_name = input("Enter the item name to update: ")
    item_price = int(input("Enter the current item price: "))
    new_item_name = input("Enter the new item name: ")
    new_item_price = int(input("Enter the new item price: "))
    
    item = MenuItem(item_name, item_price)
    item.update(new_item_name, new_item_price)
    print("Item was updated successfully.")    
    
def show_menu():
    menu_manager = MenuManager()
    menu_manager.all_items()
 

def show_item():
    item_name = input("Enter the name of a meal: ")
    menu_manager = MenuManager()
    menu_manager.one_item(item_name)
    
    
    
while True:
    show_user_menu()
    exit_choice = input("Do you want to exit? (Y/N): ").lower()
    if exit_choice.upper() == 'y':
        show_menu()
        break
   