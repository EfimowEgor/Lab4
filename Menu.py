class Menu:

    @staticmethod
    def choose_empty_existing_menu():
        print('1. Open an existing file')
        print('2. Continue with a new file')
        print('0. Exit')

    @staticmethod
    def empty_file_menu():
        print('1. Add product')
        print('2. Add supplier')
        print('0. Exit')

    @staticmethod
    def big_menu():
        print('1. Add product')
        print('2. Add supplier')
        print('3. Delete product')
        print('4. Delete supplier')
        print('5. Edit product')
        print('6. Edit supplier')
        print('7. Print data')
        print('0. Exit')

    @staticmethod
    def print_data_menu():
        print('1. Print all products')
        print('2. Print all suppliers')
        print('3. Print products by selected parameter')
        print('4. Print the supplier by name')
        print('0. Back')

    @staticmethod
    def edit_supplier_menu():
        print('1. Edit supplier name')
        print('2. Add a product to the history')
        print('3. Delete a product from the history')
        print('4. Edit delivery date')
        print('5. Edit the place of delivery')
        print('0. Back')
