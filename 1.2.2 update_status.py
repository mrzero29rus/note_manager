def input_titles():
    titles = []
    while True:
        title = input("Введите название заметки\n(введите \"Стоп\" или нажмите \"Enter\" чтобы закончить ввод): ")
        if title.lower() == "стоп" or title == "":
            break
        if title in titles:
            print("Такой заголовок уже существует!")
        else:
            titles.append(title)
    return titles

note = [
    input("Введите ваше имя: "),
    input_titles(),
    input("Введите содержание заметки: "),
    "Новая",
    input("Введите дату создания (дд-мм-гггг): "),
    input("Введите дату выполнения (дд-мм-гггг): ")
]

# изменение статуса заметки
print("\nТекущий статуст заметки:", note[3])
print("Выберите новый статус для вашей заметки и нажмите Enter:"
      "\n1 - В процессе \n2 - Выполнено \n3 - Отложено")
while True:
    num = input("Ответ: ")
    if num == "1":
        note[3] = "В процессе"
        break
    elif num == "2":
        note[3] = "Выполнено"
        break
    elif num == "3":
        note[3] = "Отложено"
        break
    else:
        print("Ошибка, повторите ввод")

print("\nИмя пользователя:", note[0],
      "\nЗаголовки:", note[1],
      "\nСодержание:", note[2],
      "\nСтатус:", note[3],
      "\nДата создания:", note[4],
      "\nДата выполнения:",note[5])