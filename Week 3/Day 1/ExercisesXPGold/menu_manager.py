# Exercise 3 : Restaurant Menu Manager
# The purpose of this exercise is to create a restaurant menu. The code will allow a manager to add and delete dishes.

# Create a python file called menu_manager.py.

# Create a class called MenuManager.

# Create a method __init__ that instantiates an attribute called menu. The menu attributes value will be all the current dishes (list of dictionaries). Each dish will be stored in a dictionary where the keys are name, price, spice level and gluten index (which value is a boolean).
# The dishes provided above should be the value of the menu attribute.

# Create a method called add_item(name, price, spice, gluten). This method will add new dishes to the menu.

# Create a method called update_item(name, price, spice, gluten). This method checks whether a dish is in the menu, if the dish exists then update it. If not notify the manager that the dish is not in the menu.

# Create a method called remove_item(name). This method should check if the dish is in the menu, if the dish exists then delete it and print the updated dictionary. If not notify the manager that the dish is not in the menu.

class Menu:
    def __init__(self):
        self.menu = [
            {"name": "Soup", "price": 10, "spice": "B", "gluten": False},
            {"name": "Hamburger", "price": 15, "spice": "A", "gluten": True},
            {"name": "Salad", "price": 18, "spice": "A", "gluten": False},
            {"name": "French Fries", "price": 5, "spice": "C", "gluten": False},
            {"name": "Beef bourguignon", "price": 25, "spice": "B", "gluten": True},
        ]

class MenuManager:
    def __init__(self, menu):
        self.menu=menu       
        
    def add_meal(self, name, price, spice, gluten):
        new_meal = {"name": name, "price": price, "spice": spice, "gluten": gluten}
        self.menu.append(new_meal)
        
    def update_meal(self, name, price, spice, gluten):      
        for item in self.menu:
            if item["name"] == name:
                item["price"] = price
                item["spice"] = spice
                item["gluten"] = gluten
                break
        else:
            print(f"{name} is not in the menu")
            
    def remove_meal(self, name):
        for item in self.menu:
            if item["name"] == name:
                self.menu.remove(item)
                print(f"{name} was removed from the menu")
                break
        else:
            print(f"{name} is not in the menu")


my_menu = Menu()

menu_manager = MenuManager(my_menu.menu)


meals_to_add = ["Lasagna", 20, "A", False]
menu_manager.add_meal(*meals_to_add)
menu_manager.update_meal("Hamburger", 18, "B", True)
menu_manager.remove_meal("Salad")

# Print the updated menu
print(menu_manager.menu)