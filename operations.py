from datetime import datetime


def get_int_range(min_val: int, max_val: int) -> int:
    """
    :param min_val: Минимальное значение, которое может ввести пользователь
    :param max_val: Максимальное значение, которое может ввести пользователь
    :return: Пункт меню
    """
    while True:
        try:
            tmp_res = int(input('Select a menu item: '))
            if tmp_res < min_val or tmp_res > max_val:
                raise ValueError
            return tmp_res
        except ValueError:
            print('Incorrect input')


def get_int(msg: str = '') -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('Incorrect input')


def get_number_of_prods_history() -> int:
    while True:
        try:
            tmp_val = get_int('Enter the number of products in the supplier history: ')
            if tmp_val < 0:
                raise ValueError
            return tmp_val
        except ValueError:
            print('Incorrect input')


def get_storage_conditions():
    """
    :return: Целое число - температура хранения продукта
    """
    return get_int('Enter the storage temperature: ')


def get_id(msg: str = '') -> int:
    """
    :return: Возвращает целое число - идентификатор продукта
    """
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('Incorrect input')


def get_product_delivery_time():
    while True:
        try:
            return datetime.strptime(input('Enter the delivery date of the product: '), '%d.%m.%Y')
        except ValueError:
            print('Incorrect input')


def get_int_positive_number(msg: str = '') -> int:
    while True:
        try:
            a = int(input(msg))
            if a <= 0:
                raise ValueError
            return a
        except ValueError:
            print('Incorrect input')
