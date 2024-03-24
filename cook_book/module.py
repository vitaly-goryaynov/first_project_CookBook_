from cook_book import GUI
from cook_book import bl_upp


def start() -> None:
    """
    Функция запуска программы
    :return: Если создалась успешно созадалась директория, запуск программы
    """
    if not bl_upp.load():
        GUI.error_create_folder()
        return
    GUI.start_work()
    mainloop()
    GUI.end_soft()


def mainloop() -> None:
    """
    Функция командного меню
    :return: None
    """
    GUI.output_info_mess('info_main_menu')
    while True:
        command = GUI.input_user()
        if command == 'help':
            GUI.output_info_mess('info_main_menu')
            continue
        elif command == 'exit':
            return
        result = bl_upp.run_command(command)
        if result == 'exit':
            return
