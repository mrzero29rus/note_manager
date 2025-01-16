notes = [
    {"Имя пользователя" : "Артем",   "Заголовок" : ["Список покупок"]},
    {"Имя пользователя" : "Татьяна", "Заголовок" : "Рецепт пирога"},
    {"Имя пользователя" : "Артем",   "Заголовок" : "Инструкция"}
]

def delete_note_function():
    value = input("Введите имя пользователя или заголовок для удаления заметки: ")
    for i in reversed(range(len(notes))):
        if notes[i]["Имя пользователя"].lower() == value.lower() or notes[i]["Заголовок"].lower() == value.lower():
            del notes[i]

def print_note_function():
    for note in notes:
        print()
        for keys, values in note.items():
            print(keys,":",values)


delete_note_function()
print_note_function()

