def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

number_to_work = str(40500002) # "Сырое" число на входе
symbol_to_remove = "0"

for symbol in symbol_to_remove:
    number_to_work = number_to_work.replace(symbol, "")

print(number_to_work) # Число без нолей
result = get_multiplied_digits(number_to_work) # Передаем число в функцию
print(result)