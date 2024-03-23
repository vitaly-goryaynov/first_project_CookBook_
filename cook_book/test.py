def check_input_symbol(string):
    from cook_book.string import not_usage_symbol_list


    for i in not_usage_symbol_list:
        if i in string:
            return False
    return True


while True:
    str = input(">> ")
    print(check_input_symbol(str))





