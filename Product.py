from typing import ClassVar
from operations import get_storage_conditions, get_int_positive_number


class Product:
    products_collection: list[ClassVar] = []
    id_collection: [int] = set()

    def __init__(self, prod_id, product_name, storage_conditions, expiration_date):
        """
        :param prod_id: ID продукта
        :param product_name: Наименование товара
        :param storage_conditions: Условия хранения
        :param expiration_date: Срок годности
        """
        self.prod_id = prod_id
        self.product_name = product_name
        # Storage conditions are indicated by an integer - the storage temperature
        self.storage_conditions = storage_conditions
        # The expiration date indicates in days
        self.expiration_date = expiration_date
        Product.products_collection.append(self.__dict__)
        Product.id_collection.add(self.prod_id)

    def __str__(self):
        return f'{self.prod_id}, {self.product_name}, {self.storage_conditions}, {self.expiration_date}'

    @staticmethod
    def print_prod_id(identifier):
        if identifier in Product.id_collection:
            for elem in Product.products_collection:
                if elem['prod_id'] == identifier:
                    print('id: ' + str(elem['prod_id']))
                    print('Name: ' + str(elem['product_name']))
                    print('Storage conditions:', elem['storage_conditions'])
                    print('Expiration date:', elem['expiration_date'])
        else:
            print('There is no product with this id in the database')

    @staticmethod
    def print_prods_params():
        something_was_found = False
        params_dict = {'id': 'prod_id', 'Name': 'product_name', 'Storage': 'storage_conditions',
                       'Date': 'expiration_date'}
        param = input('Specify by which parameter to search for products: id, Name, Storage, Date: ').strip()
        param_value = input('Enter the desired value: ').strip()
        if param in params_dict:
            for elem in Product.products_collection:
                if str(elem[params_dict[param]]) == param_value:
                    print('id: ' + str(elem['prod_id']))
                    print('Name: ' + str(elem['product_name']))
                    print('Storage conditions:', elem['storage_conditions'])
                    print('Expiration date:', elem['expiration_date'])
                something_was_found = True
            if not something_was_found:
                print('There is no product in the database with such a parameter value:', param)
        else:
            print('Incorrect parameter')

    @staticmethod
    def print_prods():
        print('Products: \n')
        for elem in Product.products_collection:
            print('id: ' + str(elem['prod_id']))
            print('Name: ' + str(elem['product_name']))
            print('Storage conditions:', elem['storage_conditions'])
            print('Expiration date:', elem['expiration_date'])
            print()

    @staticmethod
    def edit_product(identifier, param):
        something_was_found = False
        params_dict = {'Name': 'product_name', 'Storage': 'storage_conditions', 'Date': 'expiration_date'}
        if param in params_dict and identifier in Product.id_collection:
            for elem in Product.products_collection:
                if elem['prod_id'] == identifier:
                    if param == 'Name':
                        elem[params_dict[param]] = input('Enter a new product name: ')
                    elif param == 'Storage':
                        elem[params_dict[param]] = get_storage_conditions()
                    elif param == 'Date':
                        elem[params_dict[param]] = get_int_positive_number('Enter a new expiration date: ')
                    else:
                        print('Incorrect parameter')
                    something_was_found = True
            if not something_was_found:
                print('There is no product with this id in the database')
        else:
            print('There is no supplier with this id in database')
