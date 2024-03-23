def check_input_symbol(string) -> bool:
    from cook_book.string import not_usage_symbol_list

    for i in not_usage_symbol_list:
        if i in string:
            return False
    return True


def save_recipe(info: list, file) -> bool:
    from cook_book.string import path
    try:
        path_catalog = path + f'\\{file}.vitalson'
        writing_file = open(path_catalog, 'a', encoding='utf8')
        text = '~'.join(info)
        writing_file.write(text)
        writing_file.close()
        return True
    except Exception:
        return False


def search_in_recipe(lst: list) -> list:
    lst1 = []

    for i in range(1, len(lst) - 1, 5):
        lst2 = [lst[i], lst[i + 1], lst[i + 2], lst[i + 3], lst[i + 4]]
        lst1.append(lst2)
    return lst1


def is_print_search_recipe(index: int, lst1: list, name: str) -> bool:
    search = False
    for i in lst1:
        if name in i[index]:
            search = True
            print_recipe(i)
    return search


def print_recipe(recipe) -> None:
    print(f'\033[37m\tНазвание рецепта: \n\t  {recipe[0]}')
    print(f'\tСостав рецепта: \n\t  {recipe[1]}')
    print(f'\tКраткое описание рецепта: \n\t  {recipe[2]}')
    print(f'\tВремя приготовления: \n\t  {recipe[3]}')
    print(f'\tДата создания рецепта: \n\t  {recipe[4]}')
    print('----------------------------------------------------------------------------\033[0m')


def is_del_recipe(name_catalog, name: str, lst: list) -> bool:
    from cook_book.string import path

    deleted = False
    lst1 = []

    for i in range(1, len(lst) - 1, 5):
        lst1.append([lst[i], lst[i + 1], lst[i + 2], lst[i + 3], lst[i + 4]])

    for i in range(len(lst1)):
        if lst1[i][0] == name:
            index = i
            deleted = True

    if deleted:
        lst1.pop(index)

        for i in range(len(lst1)):
            recipe = '~'.join(lst1[i])
            lst1[i] = recipe

        write_data = lst[0] + '~' + '~'.join(lst1)

        with open(path + f'\\{name_catalog}.vitalson', 'w', encoding='utf-8') as f:
            f.write(write_data)

    return deleted


def sort_cooking_time_recipe(lst1: list) -> None:
    sort_list = []
    count = 0
    while len(sort_list) != len(lst1):
        min = lst1[count]
        for i in range(len(lst1)):
            if int(min[3]) > int(lst1[i][3]) and lst1[i] not in sort_list:
                min = lst1[i]
        sort_list.append(min)
        for i in range(len(lst1)):
            if not (lst1[i] in sort_list):
                count = i
                break

    for i in sort_list:
        print_recipe(i)


def is_check_existence_catalog(name_catalog: str) -> bool:  # проверка на существование каталога
    import os
    from cook_book.string import path

    if os.path.exists(path + f'\\{name_catalog}.vitalson'):
        return True
    return False


def create_new_catalog(file: str) -> None:
    from datetime import datetime
    from cook_book.string import path

    catalog_path = path + f'\\{file}.vitalson'
    file1 = open(catalog_path, 'w', encoding='utf8')
    today = datetime.today()
    date = f'Дата создания каталога: {today:%d-%m-%Y}~'
    file1.write(date)
    file1.close()


def current_time() -> str:
    from datetime import datetime

    today = datetime.today()
    date = f'{today:%d-%m-%Y}~'

    return date


def open_file(name_catalog: str) -> str:
    from cook_book.string import path

    with open(path + f'\\{name_catalog}.vitalson', 'r', encoding='utf-8') as f:
        return f.read()


def is_delete_file(name: str) -> bool:
    import os
    from cook_book.string import path

    if os.path.exists(path + f'\\{name}.vitalson'):
        os.remove(path + f'\\{name}.vitalson')
        return True
    return False


def print_list_catalogs() -> None:
    import os

    path = os.environ['USERPROFILE'] + '\\Documents\\Cookbook\\'
    l = os.listdir(path)
    li = [x.split('.')[0] for x in l]

    print('\033[37m', end='')
    for i in range(len(li)):
        print(f"\t{i + 1}) {li[i]};")
    print('\033[0m', end='')


def print_recept_date_and_count(name_catalog) -> list:
    lst = open_file(name_catalog).split('~')
    date_create_catalog = lst[0]
    count = len(lst) // 5

    print('\033[37m', end='')
    print(f'\t{date_create_catalog}')
    print(f'\tКоличество рецептов в каталоге: {count}')
    print('----------------------------------------------------------------------------')
    print('\033[0m', end='')
    return lst


def print_name_recipe_list(lst: list) -> None:
    name_recipe = []

    for i in range(1, len(lst) - 1, 5):
        name_recipe.append(lst[i])

    print('\033[37m', end='')
    for j in range(len(name_recipe)):
        print(f'\t{j + 1}) {name_recipe[j]}')
    print('\033[0m', end='')


def print_recept_list(lst: list) -> None:
    lst1 = []

    print('\033[37m', end='')
    for i in range(1, len(lst) - 1, 5):
        lst2 = [lst[i], lst[i + 1], lst[i + 2], lst[i + 3], lst[i + 4]]
        lst1.append(lst2)
        print_recipe(lst2)


def sort_recipe_time(path) -> None:
    lst = open_file(path).split('~')
    sort_lst = search_in_recipe(lst)
    print_recept_date_and_count(lst)
    sort_cooking_time_recipe(sort_lst)


def del_recipe(path: str, target) -> None:
    from cook_book import GUI

    lst = open_file(path).split('~')
    if not is_del_recipe(path, target, lst):
        GUI.output_error_mess('Такой рецепт не найден')
    else:
        GUI.output_info_mess('Рецепт успешно удален!')


def search_name(path: str, target, index: int) -> bool:
    lst = open_file(path).split('~')
    lst1 = search_in_recipe(lst)
    if not is_print_search_recipe(index, lst1, target):
        return False
    return True
