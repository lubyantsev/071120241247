def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for index, string in enumerate(strings, start=1):
            byte_position = file.tell()  # Получаем позицию в байтах перед записью
            file.write(string + '\n')  # Записываем строку в файл с переводом строки
            strings_positions[(index, byte_position)] = string  # Сохраняем данные в словарь

    return strings_positions


# Пример выполняемого кода
if __name__ == '__main__':
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)