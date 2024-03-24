from cook_book.string import *
from ctypes import windll

k = windll.kernel32
k.SetConsoleMode(k.GetStdHandle(-11), 7)


def info_mess() -> None:
    print(f'\033[32mINFO:', end='\t')


def look_mess() -> None:
    print(f'\033[35mLOOK:', end='\t')


def user_input() -> None:
    print(f'\033[36mUSER:', end='\t')


def error_mess() -> None:
    print(f'\033[31mERROR:', end='\t')


def clear_color_console() -> None:
    print('\033[0m', end='')


def error_create_folder() -> None:
    """
    Функция оповещения ошибки при создании директории
    :return: None
    """
    error_mess()
    input("Ошибка при создании системных файлов. Нажмите Enter для выхода из приложения...")


def start_work() -> None:
    """
    Функция запуска стартового оповещения
    :return: None
    """
    look_mess()
    print(start_text)
    clear_color_console()


def input_user() -> str:
    """
    Функция для выбора цвета текста пользователя
    :return: Ввод текста
    """
    user_input()
    clear_color_console()
    return input()


def output_info_mess(mess) -> None:
    """
    Функция запуска информационных сообщений
    :param mess: Команда от пользователя
    :return: None
    """
    info_mess()
    if mess == 'info_main_menu':
        print(info_com)
        return
    if mess == 'info recipe menu':
        print(info_recipe_com)
        return
    print(mess)
    clear_color_console()


def output_error_mess(mess) -> None:
    """
    Функция цвета текста при ошибке
    :param mess: Сообщение для вывода
    :return: None
    """
    error_mess()
    print(mess)
    clear_color_console()


def output_look_mess(mess) -> None:
    """
    Функция цвета текста оповещающих сообщений
    :param mess:
    :return:
    """
    look_mess()
    print(mess)
    clear_color_console()


def end_soft() -> None:
    """
    Функция вывода текста при завершении работы
    :return: None
    """
    look_mess()
    input('Работа приложения успешно завершена...\n\t\tНажмите Enter для закрытия консоли!')


