"""
Description: This program is a console-based management system for Lory's Cafe, implemented in Python. 
It utilizes the LorysCafeManagementSystem class to handle dynamic modifications to the cafe's menu items and customer records. 
Users can add, remove, update, and search for items in the menu, as well as manage customer records, including details like name,
 email, phone number, and age. The system incorporates exception handling and allows users to gracefully exit using stop words such as 'q', 'quit', or 'stop'. 
Overall, it provides an interactive and versatile interface for efficient management of both menu items and customer records at Lory's Cafe. 

Author: Lauriane Houndjahoue

"""
class LorysCafeManagementSystem:
    def __init__(self, menu, records):
        self.menu = menu
        self.records = records

    def add_menu_item(self, section, item_name, item_price):
        try:
            item_name = item_name.lower()
            item_price = float(item_price)
            self.menu[section][item_name] = item_price
            print(f"{item_name} has been added to {section}.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for item price.")

    def remove_menu_item(self, section, item_name):
        try:
            item_name = item_name.lower()
            del self.menu[section][item_name]
            print(f"{item_name} has been removed from {section}.")
        except KeyError:
            print(f"{item_name} is not a valid item in {section}.")

    def update_menu_item(self, section, item_name, new_price):
        try:
            item_name = item_name.lower()
            new_price = float(new_price)
            self.menu[section][item_name] = new_price
            print(f"{item_name} has been updated to {new_price}.")
        except KeyError:
            print(f"{item_name} is not a valid item in {section}.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric value for the new price.")

    def search_menu_item(self, item_to_search):
        try:
            if item_to_search.lower() == 'all':
                print('\nMenu:\n')
                for section, items in self.menu.items():
                    print(f'{section.capitalize()}: {", ".join(items)}')
            else:
                found = False
                for section, items in self.menu.items():
                    if item_to_search.lower() in items:
                        print(f'\nItem "{item_to_search.capitalize()}" found in {section.capitalize()}!')
                        found = True
                if not found:
                    print(f'"{item_to_search.capitalize()}" does not exist.\nTry again or type "All" to see all available items.')
        except Exception as e:
            print(f"An error occurred: {e}")

    def add_customer_record(self, record_id, record_data):
        try:
            self.records[record_id] = record_data
            print(f"Customer record for ID {record_id} has been added.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def remove_customer_record(self, record_id):
        try:
            record_id = int(record_id)
            del self.records[record_id]
            print(f"Customer record for ID {record_id} has been removed.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for record ID.")
        except KeyError:
            print(f"Customer record for ID {record_id} does not exist.")

    def update_customer_record(self, record_id, column_name, new_value):
        try:
            if record_id in self.records and column_name in self.records[record_id]:
                self.records[record_id][column_name] = new_value
                print("Customer record updated successfully.")
            else:
                raise KeyError
        except KeyError:
            print("Invalid record ID or column name.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def search_customer_record(self, record_id):
        try:
            record_id = int(record_id)
            if record_id in self.records:
                print(f"Customer Record for ID {record_id}: {self.records[record_id]}")
            else:
                raise KeyError
        except ValueError:
            print("Invalid input. Please enter a numeric value for record ID.")
        except KeyError:
            print(f"Customer Record for ID {record_id} does not exist.")

def welcome_message(user_name):
    print(f"\nWelcoming {user_name} to Lory's Cafe Management System!")
    print("===========================================================\n")

def main():
    # Database for menu
    menu_lorys_cafe = {
        "drinks": {"Boba Milk Tea": 2, "Sunset Milk Tea": 4, "Chai Latte": 3, "Caramel Macchiato": 4, "Watermelon Slushie": 2, "Water": 1.5},
        "desserts": {"Chocolate Eclair": 8, "Fruit Tarte": 7, "Strawberry Shortcake": 10, "Cheesecake": 9, "Panna Cotta": 6, "Croissant": 10, "Oreo Croffle": 7, "Choco-Mousse": 12},
        "meals": {"Hot Honey Chicken Plate": 12, "Miso Glazed Salmon Plate": 13, "Chicken Nugget": 8, "Corn Dog": 3, "Bibimbap": 14, "Chicken Salad": 8.5},
        "sides": {"French Fries": 3, "White Rice": 2, "Garlic French Fries": 4.5, "Roasted Sweet Potatoes": 3.5, "Toppokki": 6.5}
    }

    # Database for customer record
    customer_records = {
        123: {"ID": 123, "name": "John Doe", "email": "john@example.com", "phone number": "123-456-7890", "age": 25},
        456: {"ID": 456, "name": "Jane Smith", "email": "jane@example.com", "phone number": "987-654-3210", "age": 30},
        789: {"ID": 789, "name": "Lauriane Houndjahoue", "email": "lauri@example.com", "phone number": "111-222-3333", "age": 22},
    }

    stop_words = ("q", "quit", "stop","Stop","Q","Quit")

    lorys_cafe_system = LorysCafeManagementSystem(menu_lorys_cafe, customer_records)

    user_name = input("What's your name? ")
    welcome_message(user_name)

    while True:
        database_choice = input("What would you like to do (add, remove, update, search, quit)? ").lower()
        if database_choice == 'add' or database_choice == 'remove' or database_choice == 'update':
            data_type = input("Enter the data type to perform the action (menu, records): ").lower()
            if data_type == 'menu':
                section = input("Enter the section to perform the action (drinks, desserts, meals, sides): ").lower()
                item_name = input("Enter the name of the item: ")
                try:
                    if database_choice == 'add':
                        item_price = input("Enter item price: ")
                        lorys_cafe_system.add_menu_item(section, item_name, item_price)
                    elif database_choice == 'remove':
                        lorys_cafe_system.remove_menu_item(section, item_name)
                    elif database_choice == 'update':
                        new_price = input("Enter the new price: ")
                        lorys_cafe_system.update_menu_item(section, item_name, new_price)
                except Exception as e:
                    print(f"An error occurred: {e}")
            elif data_type == 'records':
                record_id = input("Enter the record ID: ")
                try:
                    if database_choice == 'add':
                        record_data = {
                            "ID": int(record_id),
                            "name": input("Enter the customer's name: "),
                            "email": input("Enter the customer's email: "),
                            "phone number": input("Enter the customer's phone number: "),
                            "age": input("Enter the customer's age: "),
                        }
                        lorys_cafe_system.add_customer_record(int(record_id), record_data)
                    elif database_choice == 'remove':
                        lorys_cafe_system.remove_customer_record(record_id)
                    elif database_choice == 'update':
                        column_name = input("Enter the name of the column you want to update: ").lower()
                        new_value = input("Enter the new value: ")
                        lorys_cafe_system.update_customer_record(int(record_id), column_name, new_value)
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("Invalid data type. Please enter 'menu' or 'records'.")

        elif database_choice == 'search':
            data_type = input("Enter the data type to search (menu, records): ").lower()
            if data_type == 'menu':
                item_to_search = input("\nEnter the name of the item you want to find (type 'all' to see all items): ")
                try:
                    lorys_cafe_system.search_menu_item(item_to_search)
                except Exception as e:
                    print(f"An error occurred: {e}")
            elif data_type == 'records':
                record_id = input("Enter the record ID to search: ")
                try:
                    lorys_cafe_system.search_customer_record(int(record_id))
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("Invalid data type. Please enter 'menu' or 'records'.")

        elif database_choice in stop_words:
            break
        else:
            print("Invalid command. Please enter 'add', 'remove', 'update', 'search', or 'quit'.")

if __name__ == "__main__":
    main()