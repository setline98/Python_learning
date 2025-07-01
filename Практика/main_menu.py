# main_menu.py
# Главное консольное меню


import importlib


SCRIPTS = {
    '1': 'task1',
    '2': 'task2',
    '3': 'task3',
    '4': 'task4',
    '5': 'task5',
}


def main():
    while True:
        choice = input('\nВыберите задание (1-5) или 0 для выхода: ').strip()
        if choice == '0':
            print('Выход.')
            break
        if choice in SCRIPTS:
            module_name = SCRIPTS[choice]
            try:
                module = importlib.import_module(module_name)
                if hasattr(module, 'main'):
                    module.main()
                else:
                    print('У выбранного скрипта нет функции main().')
            except Exception as exc:
                print(f'Ошибка запуска {module_name}: {exc}')
        else:
            print('Некорректный выбор. Введите число от 1 до 5 или 0.')


if __name__ == '__main__':
    main()
