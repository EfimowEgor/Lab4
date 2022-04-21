# Grocery
from Product import Product
from Supplier import Supplier
from json import dump, loads, decoder
from operations import get_id, get_int_positive_number, get_storage_conditions, get_int_range, \
     get_number_of_prods_history
from tkinter import filedialog, Tk
from Menu import Menu
from sys import exit


class DataBase:
    data = {'Products': Product.products_collection, 'Suppliers': Supplier.suppliers_collection}

    @staticmethod
    def add_product():
        id_unique = get_unique_id_for_product()
        new_prod = Product(id_unique, input('Enter the product name: '), get_storage_conditions(),
                           get_int_positive_number('Enter the expiration date in days: '))
        DataBase.add_to_base()

    @staticmethod
    def add_supplier():
        name_unique = Supplier.get_unique_supplier_name()
        new_sup = Supplier(name_unique)
        DataBase.add_to_base()
        number_of_prods_history = get_number_of_prods_history()
        for i in range(number_of_prods_history):
            new_sup.get_history
            DataBase.add_to_base()

    @staticmethod
    def add_to_base():
        with open('out.json', 'w', encoding='utf-8') as out:
            dump(DataBase.data, out, indent=4, default=str, ensure_ascii=False)

    @staticmethod
    def delete_product():
        something_was_deleted = False
        if len(Product.products_collection) == 0:
            print('There are no products in the database')
        else:
            id_to_delete = get_id('Enter the id: ')
            # Passage through all products of the database
            for i, prod in enumerate(DataBase.data['Products']):
                if prod['prod_id'] == id_to_delete:
                    del DataBase.data['Products'][i]
                    Product.id_collection.remove(prod['prod_id'])

                    # Каскадное удаление
                    for k, sup in reversed(list(enumerate(DataBase.data['Suppliers']))):
                        for j, hist_elem in reversed(list(enumerate(sup['products_history']))):
                            if hist_elem['id'] == id_to_delete:
                                del DataBase.data['Suppliers'][k]['products_history'][j]

                    something_was_deleted = True
                    DataBase.add_to_base()
            if not something_was_deleted:
                print('There is no product with this id in the database')

    @staticmethod
    def delete_supplier():
        something_was_deleted = False
        if len(Supplier.suppliers_collection) == 0:
            print('There are no suppliers in the database')
        else:
            name_to_delete = input('Enter the name of the supplier you want to delete: ')
            # Passage through all suppliers of the database
            for i, sup in enumerate(DataBase.data['Suppliers']):
                if sup['supplier_name'] == name_to_delete:
                    del DataBase.data['Suppliers'][i]
                    Supplier.suppliers_names_collection.remove(sup['supplier_name'])
                    something_was_deleted = True
                    DataBase.add_to_base()
            if not something_was_deleted:
                print('There is no supplier with this name in the database')

    @staticmethod
    def print_data(option):
        match option:
            case 1:
                Product.print_prods()
                work_with_data_print_menu()
            case 2:
                Supplier.print_sups()
                work_with_data_print_menu()
            case 3:
                Product.print_prods_params()
                work_with_data_print_menu()
            case 4:
                Supplier.print_sup_name()
                work_with_data_print_menu()
            case 0:
                work_with_big_menu()

    @staticmethod
    def edit_product():
        tmp_id = get_id('Enter the product id you want to edit: ')
        tmp_param = input('Which product field to change: Name, Storage, Date: ')
        Product.edit_product(tmp_id, tmp_param)
        DataBase.add_to_base()

    @staticmethod
    def edit_supplier(option):
        match option:
            case 1:
                sup_name_to_edit = input('Enter the name you want to edit: ')
                Supplier.edit_supplier_name(sup_name_to_edit)
                DataBase.add_to_base()
                work_with_edit_supplier_menu()
            case 2:
                sup_name_to_edit = input('Enter the name of the supplier to whose history you want to add the product: ')
                Supplier.edit_supplier_history_add_product(sup_name_to_edit)
                DataBase.add_to_base()
                work_with_edit_supplier_menu()
            case 3:
                sup_name_to_edit = input('Enter the name of the supplier from whose history you want to delete the product: ')
                id_to_remove = get_id('Enter the id of the product you want to remove from the history: ')
                Supplier.edit_supplier_history_delete_product(sup_name_to_edit, id_to_remove)
                DataBase.add_to_base()
                work_with_edit_supplier_menu()
            case 4:
                sup_name_to_edit = input('Enter the name of the supplier whose delivery date you want to change: ')
                id_to_find = get_id('Enter the id of the product whose delivery date you want to change: ')
                Supplier.edit_supplier_date(sup_name_to_edit, id_to_find)
                DataBase.add_to_base()
                work_with_edit_supplier_menu()
            case 5:
                sup_name_to_edit = input('Enter the name of the supplier whose delivery place you want to change: ')
                id_to_find = get_id('Enter the id of the product whose delivery place you want to change: ')
                Supplier.edit_supplier_place(sup_name_to_edit, id_to_find)
                DataBase.add_to_base()
                work_with_edit_supplier_menu()
            case 0:
                work_with_big_menu()


def get_prod_ids_from_data(tmp_dict):
    for elem in tmp_dict['Products']:
        if elem['prod_id'] not in Product.id_collection:
            Product.id_collection.add(elem['prod_id'])
        else:
            raise KeyError


def get_sup_names_from_data(tmp_dict):
    for elem in tmp_dict['Suppliers']:
        if elem['supplier_name'] not in Supplier.suppliers_names_collection:
            Supplier.suppliers_names_collection.add(elem['supplier_name'])
        else:
            raise KeyError


def get_unique_id_for_product() -> int:
    while True:
        tmp_id = get_id('Enter the id: ')
        if tmp_id not in Product.id_collection:
            Product.id_collection.add(tmp_id)
            return tmp_id
        else:
            print('The product with this id is already in the database')


def open_file() -> str:
    # Create object window
    root = Tk()
    # Hide object window
    root.withdraw()
    # Window stay above all others windows
    root.attributes("-topmost", True)
    # Create a dialog window and return the selected filename
    filepath = filedialog.askopenfilename()
    # Destroy object window
    root.destroy()
    return filepath


def read_data_from_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            tmp_res = loads(file.read())
            get_prod_ids_from_data(tmp_res)
            get_sup_names_from_data(tmp_res)
            if len(tmp_res) != 2 or ('Products' not in dict(tmp_res).keys() or 'Suppliers' not in dict(tmp_res).keys()):
                raise decoder.JSONDecodeError
            else:
                DataBase.data = tmp_res
                Product.products_collection = tmp_res['Products']
                Supplier.suppliers_collection = tmp_res['Suppliers']
                DataBase.add_to_base()
                file.seek(0)
    except (decoder.JSONDecodeError, TypeError, FileNotFoundError):
        DataBase.add_to_base()
        print('Empty or incorrect File')
        print('Products and Suppliers are set to empty values')


def start_work_mode_selection():
    Menu.choose_empty_existing_menu()
    get_option = get_int_range(0, 2)
    if get_option == 1:
        read_data_from_file(open_file())
        if len(DataBase.data['Products']) == 0 and len(DataBase.data['Suppliers']) == 0:
            work_with_empty_db()
        else:
            work_with_big_menu()
    elif get_option == 2:
        # Default prod = [] sup = [], so no need to add something
        DataBase.add_to_base()
        work_with_empty_db()
    else:
        # exit from sys module to terminate program
        exit()


def work_with_empty_db():
    Menu.empty_file_menu()
    get_option = get_int_range(0, 2)
    if get_option == 1:
        DataBase.add_product()
        DataBase.add_to_base()
        work_with_big_menu()
    elif get_option == 2:
        DataBase.add_supplier()
        DataBase.add_to_base()
        work_with_big_menu()
    else:
        exit()


def work_with_big_menu():
    Menu.big_menu()
    get_option = get_int_range(0, 7)
    if get_option == 1:
        DataBase.add_product()
        work_with_big_menu()
    elif get_option == 2:
        DataBase.add_supplier()
        work_with_big_menu()
    elif get_option == 3:
        DataBase.delete_product()
        work_with_big_menu()
    elif get_option == 4:
        DataBase.delete_supplier()
        work_with_big_menu()
    elif get_option == 5:
        work_with_edit_product_menu()
        work_with_big_menu()
    elif get_option == 6:
        work_with_edit_supplier_menu()
    elif get_option == 7:
        work_with_data_print_menu()
    else:
        exit()


def work_with_data_print_menu():
    Menu.print_data_menu()
    get_data_print_option = get_int_range(0, 4)
    DataBase.print_data(get_data_print_option)


def work_with_edit_product_menu():
    DataBase.edit_product()


def work_with_edit_supplier_menu():
    Menu.edit_supplier_menu()
    get_edit_supplier_option = get_int_range(0, 5)
    DataBase.edit_supplier(get_edit_supplier_option)


start_work_mode_selection()
