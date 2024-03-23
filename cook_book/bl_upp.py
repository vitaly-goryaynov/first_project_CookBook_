from cook_book import GUI
from cook_book import bl_low


def load():
    return create_folder()


def create_folder() -> bool:  # создание системной папки Cookbook
    try:
        import os

        path = os.environ['USERPROFILE'] + '\\Documents'
        os.chdir(path)
        if not os.path.isdir('Cookbook'):
            os.mkdir('Cookbook')

        return True
    except Exception:
        return False


def run_command(command) -> bool or str:
    if command == 'list':
        bl_low.print_list_catalogs()
        return True
    elif command == 'add':
        result = created_catalog()
        if result:
            GUI.output_look_mess(result)
        else:
            GUI.output_info_mess('info_main_menu')
    elif command == 'open':
        check = work_with_catalog()
        if check == 'exit':
            return 'exit'
        GUI.output_info_mess('info_main_menu')
    elif command == 'check':
        command_search()
        GUI.output_info_mess('info_main_menu')
    elif command == 'del':
        path = input_path()
        if not bl_low.is_delete_file(path):
            GUI.output_error_mess("Такой каталог не обнаружен")
        else:
            GUI.output_look_mess('Каталог успешно удален!')
    else:
        GUI.output_error_mess('Не правильная команда, проверьте правильность ввода')


def input_path() -> str:
    GUI.output_info_mess('Введите название каталога')
    while True:
        name_catalog = GUI.input_user()
        if not bl_low.check_input_symbol(name_catalog):
            GUI.output_error_mess('Вы использовали недопустимый символ, повторите ввод')
            continue
        return name_catalog


def created_catalog() -> str or bool:
    name_catalog = input_path()

    if not bl_low.is_check_existence_catalog(name_catalog):
        bl_low.create_new_catalog(name_catalog)
        return 'Каталог создан!'
    else:
        return catalog_exist_menu(name_catalog)


def catalog_exist_menu(file: str) -> str or bool:  # выбор создать новый каталог ?
    from cook_book.string import catalog_is_exist
    GUI.output_look_mess(catalog_is_exist)

    while True:
        com = GUI.input_user()
        if com == 'no':
            return False

        elif com == 'yes':
            bl_low.create_new_catalog(file)
            return 'Каталог создан!'

        elif com == 'add':
            add_recipe(file)
            return False

        elif com == 'help':
            GUI.output_look_mess(catalog_is_exist)

        else:
            GUI.output_error_mess('Не правильный ввод!\n'
                                  '\t\t Повторите попытку')


def add_recipe(file: str) -> None:
    from cook_book.string import sample_recipe

    recipe_info = []
    for i in range(4):
        mess = f'Введите {sample_recipe[i]} рецепта'
        if i == 1:
            mess = mess + "\n\t\tВводить состав надо через запятую, а количество разделять пробелом"
        if i == 3:
            mess = mess + " в минутах"

        GUI.output_info_mess(mess)

        attribute = input_attribute(sample_recipe[i], i)

        recipe_info.append(attribute)

    recipe_info.append(bl_low.current_time())

    if bl_low.save_recipe(recipe_info, file):
        GUI.output_look_mess('Рецепт успешно добавлен в каталог!')

    GUI.output_info_mess('Добавить еще один рецепт?\n'
                         '\t\t yes - Добавить\n'
                         '\t\t no - Выход из добавления рецептов')
    while True:
        com = GUI.input_user()
        if com == 'yes':
            add_recipe(file)

        elif com == 'no':
            return

        elif com == 'help':
            GUI.output_info_mess('Добавить еще один рецепт?\n'
                                 '\t\t yes - Добавить\n'
                                 '\t\t no - Выход из добавления рецептов')

        else:
            GUI.output_error_mess('Введите yes или no')


def input_attribute(name, i):
    while True:
        attribute = GUI.input_user()
        if "~" in attribute:
            GUI.output_error_mess(f'В {name} рецепта нельзя использовать "~"\n'
                                  f'\t\tПовторите ввод')
            continue

        if i == 3 and not attribute.isdigit():
            GUI.output_error_mess('Ввод должен быть только из целых чисел, измеряется в минутах\n'
                                  '\t\tПовторите ввод')
            continue

        if attribute == '':
            return 'Поле не заполнено'
        return attribute


def command_search() -> None or str:
    path = input_path()
    if bl_low.is_check_existence_catalog(path):
        GUI.output_look_mess('Каталог найден!')
    else:
        GUI.output_error_mess('Каталога не существует!')


def work_with_catalog() -> str or None:
    GUI.output_info_mess('info recipe menu')
    while True:
        command = GUI.input_user()
        if command == 'name':  # Краткий писок рецептов в каталоге по дате создания
            name_catalog = input_path()
            if not bl_low.is_check_existence_catalog(name_catalog):
                GUI.output_error_mess('Такой каталог не существует')
                continue
            lst = bl_low.print_recept_date_and_count(name_catalog)
            bl_low.print_name_recipe_list(lst)

        elif command == 'all':  # Полный список рецептов по дате создания
            name_catalog = input_path()
            if not bl_low.is_check_existence_catalog(name_catalog):
                GUI.output_error_mess('Такой каталог не существует')
                continue
            lst = bl_low.print_recept_date_and_count(name_catalog)
            bl_low.print_recept_list(lst)

        elif command == 'add':  # Добавить рецепт в каталог
            name_catalog = input_path()
            if not bl_low.is_check_existence_catalog(name_catalog):
                GUI.output_error_mess('Такой каталог не существует')
                continue
            add_recipe(name_catalog)

        elif command == 'find':  # Найти рецепт по названию
            name_catalog = input_path()
            if not bl_low.is_check_existence_catalog(name_catalog):
                GUI.output_error_mess('Такой каталог не существует')
                continue

            GUI.output_info_mess('''По какому атрибуту искать?
\t\t 1 - По названию
\t\t 2 - По составу''')

            while True:
                index = GUI.input_user()
                if index == '1' or index == '2':
                    break
                elif index == 'back':
                    continue
                else:
                    GUI.output_error_mess('Не правильный атрибут поиска, введите 1 или 2 (back - выйти из поиска):')

            GUI.output_info_mess(f"Введите название {'рецепта' if index == '1' else 'ингридиента'}")
            target = GUI.input_user()

            if not bl_low.search_name(name_catalog, target, 0 if index == '1' else 1):
                GUI.output_look_mess('Рецептов не найдено')

        elif command == 'sort':  # Сортировка по времени приготовления
            name_catalog = input_path()
            if not bl_low.is_check_existence_catalog(name_catalog):
                GUI.output_error_mess('Такой каталог не существует')
                continue

            bl_low.sort_recipe_time(name_catalog)

        elif command == 'del':  # Удалить рецепт
            name_catalog = input_path()
            if not bl_low.is_check_existence_catalog(name_catalog):
                GUI.output_error_mess('Такой каталог не существует')
                continue

            GUI.output_info_mess("Введите название рецепта")
            target = GUI.input_user()

            bl_low.del_recipe(name_catalog, target)

        elif command == 'back':  # Вернуться в меню
            return

        elif command == 'info':
            GUI.output_info_mess('info recipe menu')

        elif command == 'exit':  # Выйти из программы
            GUI.output_look_mess('Вы действительно хотите выйти? (y для выхода)')

            if GUI.input_user().lower() == 'y':
                return 'exit'
        else:
            GUI.output_error_mess('Не правильная команда, проверьте правильность ввода')
