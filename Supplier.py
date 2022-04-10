from typing import ClassVar
from operations import get_id, get_product_delivery_time
from Product import Product


class Supplier:
    suppliers_collection: list[ClassVar] = []
    suppliers_names_collection: [str] = set()

    def __init__(self, supplier_name):
        """
        :param supplier_name: Наименование поставщика
        """
        self.supplier_name = supplier_name
        self.products_history = []
        # Adding a new supplier to the list of suppliers in the form of a dictionary
        Supplier.suppliers_collection.append(self.__dict__)

    def __str__(self):
        return f'{self.supplier_name}\t{self.products_history}'

    @staticmethod
    def get_unique_supplier_name() -> str:
        while True:
            tmp_sup_name = input('Enter the name of the supplier: ')
            if tmp_sup_name not in Supplier.suppliers_names_collection:
                Supplier.suppliers_names_collection.add(tmp_sup_name)
                return tmp_sup_name
            else:
                print('The supplier with this name is already in the database')

    @staticmethod
    def print_sup_name():
        something_was_found = False
        tmp_name = input('Specify the name of the supplier you want to find: ').strip()
        for elem in Supplier.suppliers_collection:
            if elem['supplier_name'] == tmp_name:
                print('Name:', elem['supplier_name'])
                print('History: ')
                for hist_elem in elem['products_history']:
                    if hist_elem['id'] in Product.id_collection:
                        Product.print_prod_id(hist_elem['id'])
                    else:
                        print('id:', hist_elem['id'])
                    print('Delivery date:', hist_elem['Delivery date'])
                    print('Place:', hist_elem['Place'])
                    print()
                something_was_found = True
        if not something_was_found:
            print('There is no supplier with this name in the database')

    @staticmethod
    def print_sups():
        print('Suppliers: ')
        for elem in Supplier.suppliers_collection:
            print('Name:', elem['supplier_name'])
            print('History: ')
            for hist_elem in elem['products_history']:
                if hist_elem['id'] in Product.id_collection:
                    Product.print_prod_id(hist_elem['id'])
                else:
                    print('id:', hist_elem['id'])
                print('Delivery date:', hist_elem['Delivery date'])
                print('Place:', hist_elem['Place'])
            print()

    @staticmethod
    def edit_supplier_name(sup_name):
        tmp_sup_name = Supplier.get_unique_supplier_name()
        if sup_name in Supplier.suppliers_names_collection:
            for elem in Supplier.suppliers_collection:
                if str(elem['supplier_name']) == sup_name:
                    elem['supplier_name'] = tmp_sup_name
        else:
            print('There is no supplier with this name in the database')

    @staticmethod
    def edit_supplier_date(sup_name, identifier):
        id_was_found = False
        tmp_sup_name = get_product_delivery_time()
        if sup_name in Supplier.suppliers_names_collection:
            for elem in Supplier.suppliers_collection:
                if str(elem['supplier_name']) == sup_name:
                    for hist_elem in elem['products_history']:
                        if hist_elem['id'] == identifier:
                            hist_elem['Delivery date'] = tmp_sup_name
                            id_was_found = True
            if not id_was_found:
                print('There is no product with this id in the supplier history')
        else:
            print('There is no supplier with this name in the database')

    @staticmethod
    def edit_supplier_place(sup_name, identifier):
        id_was_found = False
        tmp_sup_name = input('Enter a new delivery location: ').strip()
        if sup_name in Supplier.suppliers_names_collection:
            for elem in Supplier.suppliers_collection:
                if str(elem['supplier_name']) == sup_name:
                    for hist_elem in elem['products_history']:
                        if hist_elem['id'] == identifier:
                            hist_elem['Place'] = tmp_sup_name
                            id_was_found = True
            if not id_was_found:
                print('There is no product with this id in the supplier history')
        else:
            print('There is no supplier with this name in the database')

    @staticmethod
    def edit_supplier_history_add_product(sup_name):
        if len(Supplier.suppliers_collection) == 0:
            print('There are no suppliers in the database')
        else:
            if sup_name in Supplier.suppliers_names_collection:
                tmp_id = get_id('Enter the id: ')
                delivery_date = get_product_delivery_time()
                place = input('Enter the place of delivery: ')
                for elem in Supplier.suppliers_collection:
                    if str(elem['supplier_name']) == sup_name:
                        elem['products_history'].append({'id': tmp_id, 'Delivery date': delivery_date, 'Place': place})
            else:
                print('There is no supplier with this name in the database')

    @staticmethod
    def edit_supplier_history_delete_product(sup_name, identifier):
        if len(Supplier.suppliers_collection) == 0:
            print('There are no suppliers in the database')
        else:
            id_was_found = False
            if sup_name in Supplier.suppliers_names_collection:
                for i, sup in enumerate(Supplier.suppliers_collection):
                    if sup['supplier_name'] == sup_name:
                        for j, hist_sup in enumerate(sup['products_history']):
                            if hist_sup['id'] == identifier:
                                del Supplier.suppliers_collection[i]['products_history'][j]
                                id_was_found = True
                if not id_was_found:
                    print('Here is no product with this id in the supplier history')
            else:
                print('There is no supplier with this name in the database')

    @property
    def get_history(self):
        tmp_dict = {'id': get_id('Enter the id: '), 'Delivery date': get_product_delivery_time(),
                    'Place': input('Enter the place of delivery: ').strip()}
        return self.products_history.append(tmp_dict)
