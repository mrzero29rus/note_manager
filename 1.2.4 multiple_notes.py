notes = []

# сборка заметки
def create_note_function():
    data = [
        input("Введите имя пользоватея: "),
        input("Введите заголовок: "),
        input("Введите содеержание: "),
        input("Введите статус: "),
        input("Введите дату создания: "),
        input("Введите даду выполнения:и")
    ]
    note = {
        "Имя пользователя:": data[0],
        "Заголовок": data[1],
        "Содержание": data[2],
        "Статус": data[3],
        "Дата создания": data[4],
        "Дата выполнения": data[5]
    }
    notes.append(note)

# функция печати заметки
def print_note_function():
    for note in notes:
        print()
        for key, values in note.items():
            print(key, ":", values)

# цикл добавления заметок
print("Добро пожаловать в \"Менеджер заметок\"! Вы можете добавить новую заметку.")
while True:
    print("\nХотите добавить заметку: 1 - Да; 2 - Нет.")
    answer = input("Ответ: ")
    if answer == "1":
        create_note_function()
        print("\nЗаметка сохранена")
    elif answer == "2":
        print("\nСписок заметок:")
        print_note_function()
    else:
        print("Ошибка, повторите ввод")