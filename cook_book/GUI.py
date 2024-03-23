from cook_book.string import *
from ctypes import windll

k = windll.kernel32
k.SetConsoleMode(k.GetStdHandle(-11), 7)


def info_mess() -> None:
    print(f'\033[32mINFO:', end='\t')


def look_mess() -> None:
    print(f'\033[35mLOOK:', end='\t')


def user_input() -> None :
    print(f'\033[36mUSER:', end='\t')


def error_mess() -> None:
    print(f'\033[31mERROR:', end='\t')


def clear_color_console() -> None:
    print('\033[0m', end='')


def error_create_folder() -> None:
    error_mess()
    input("Ошибка при создании системных файлов. Нажмите Enter для выхода из приложения...")


def start_work() -> None:
    look_mess()
    print(start_text)
    clear_color_console()


def input_user() -> str:
    user_input()
    clear_color_console()
    return input()


def output_info_mess(mess) -> None:
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
    error_mess()
    print(mess)
    clear_color_console()


def output_look_mess(mess) -> None:
    look_mess()
    print(mess)
    clear_color_console()


def end_soft() -> None:
    look_mess()
    input('Работа приложения успешно завершена...\n\t\tНажмите Enter для закрытия консоли!')


