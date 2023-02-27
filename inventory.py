
# Start

#========Import Libraries========
from tabulate import tabulate

#=========================The beginning of the class=========================

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        pass
        '''
        In this function, I have initialised the following attributes:
        country, code, product, cost and quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return (f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity}.\n")


#=======Shoe list=======

shoe_list = []


#============================Functions outside the class============================

def read_shoes_data():
    pass
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. 
    '''
    try:
        with open("inventory.txt", "r") as inventory_read:
            lines = inventory_read.readlines()

            for i, line in enumerate(lines):
                # skips the first line of data in the file
                if i == 0:
                    continue

                country, code, product, cost, quantity = line.strip().split(",")
                cost = cost
                quantity = int(quantity)
                shoe = Shoe(country, code, product, cost, quantity)
                shoe_list.append(shoe)

        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        print("Shoes data has been read, chose what to do next. ")
    
    except FileNotFoundError:
        print("The file dosen't exist. ")

def capture_shoes():
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    if len(shoe_list) > 0:

        country = input("Enter the country: ")
        code = input("Enter the code: ")
        product = input("Enter the product: ")
        cost = float(input("Enter the cost: "))
        quantity = int(input("Enter the quantity: "))

        shoe = Shoe(country, code, product, cost, quantity)
        shoe_list.append(shoe)

        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        print(f"{product} has been captured. ")

    else:
        print("No shoes in inventory, read shoes data first. ")

def view_all():
    pass
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function.
    '''
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    if len(shoe_list) > 0:
        headers = ["Country", "Code", "Product", "Cost", "Quantity"]
        table = []

        for shoe in shoe_list:
            table.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.get_quantity()])
        print(tabulate(table, headers, tablefmt="fancy_grid"))

    else:
        print("No shoes in inventory, read shoes data first. ")

def re_stock():
    pass
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Asking the user if they
    want to add this quantity of shoes and then update it.
    '''
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    if len(shoe_list) > 0:

        lowest_quantity_shoe = None

        for shoe in shoe_list:
            if not lowest_quantity_shoe or shoe.get_quantity() < lowest_quantity_shoe.get_quantity():
                lowest_quantity_shoe = shoe

        if lowest_quantity_shoe and lowest_quantity_shoe.get_quantity() < 5:
            print(f"{lowest_quantity_shoe.product} is low on stock: {lowest_quantity_shoe.quantity}.\n")

            add_quantity = int(input(f"Enter the quantity to add for {lowest_quantity_shoe.product}: "))
            lowest_quantity_shoe.quantity += add_quantity

            with open("inventory.txt", "w") as file:
                file.write("country,code,product,cost,quantity\n")

                for shoe in shoe_list:
                    file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

            print(f"\n{lowest_quantity_shoe.product} has been restocked with {add_quantity} and now has {lowest_quantity_shoe.quantity}. ")
        
        else:
            print("All shoes have at least 5 of each in stock. ")

    else:
        print("No shoes in inventory, read shoes data first. ")

def search_shoe():
    pass
    '''
    This function will search for a shoe from the list
    using the shoe code and return this object so that it will be printed.
    '''
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    if len(shoe_list) > 0:

        while True:
            code = input("Enter the shoe code or 'exit' to exit: ")
            found = False

            if code == "exit" or code == "e":
                break

            for shoe in shoe_list:
                if shoe.code == code:
                    found = True
                    print(f"\n{shoe}")
                    break

            if not found:
                print("\nInvalid code, try again.\n")
                continue

    else:
        print("No shoes in inventory, read shoes data first. ")

def value_per_item():
    pass
    '''
    This function will calculate the total value for each item.
    The formula for value is: value = cost * quantity.
    '''
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    if len(shoe_list) > 0:

        for shoe in shoe_list:
            cost = float(shoe.get_cost())
            quantity = float(shoe.get_quantity())
            value = round(cost * quantity, 2)
            print(f"The value of stock for {shoe.product} is: {value:,.2f}. ")

    else:
        print("No shoes in inventory, read shoes data first. ")

def highest_qty():
    pass
    '''
    This function determines the product with the highest quantity and
    print this shoe as being for sale.
    '''
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    if len(shoe_list) > 0:
        highest_quantity_shoe = None

        for shoe in shoe_list:
            if not highest_quantity_shoe or shoe.get_quantity() > highest_quantity_shoe.get_quantity():
                highest_quantity_shoe = shoe

        if highest_quantity_shoe:
            print(f"The shoe with the highest quantity for sale is: {highest_quantity_shoe.product}, with {highest_quantity_shoe.get_quantity()}. ")

    else:
        print("No shoes in inventory, read shoes data first. ")


#=================Main Menu=================
'''
A menu that executes each function above.

'''
def show_menu():
    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("""
1.   Read shoes data
2.   Capture shoes
3.   View all shoes
4.   Re-stock shoes
5.   Search shoes
6.   Calculate value per item
7.   Get highest quantity shoe
8.   Quit
""")

def menu():
    while True:
        show_menu()

        try:
            option = int(input("Enter option: "))

            if option == 1:
                pass

                read_shoes_data()

            elif option == 2:
                pass

                capture_shoes()

            elif option == 3:
                pass

                view_all()

            elif option == 4:
                pass

                re_stock()

            elif option == 5:
                pass

                search_shoe()

            elif option == 6:
                pass

                value_per_item()

            elif option == 7:
                pass

                highest_qty()

            elif option == 8:
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                print("Goodbye!!! ")
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

                exit()

            else:
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                print("You have made a wrong choice, please try again. ")

        except ValueError:
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            print("Invalid option, please enter a number. ")

menu()

# Stop
