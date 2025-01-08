username = input("Введите ваше имя: ")

title1 = input("Заголовок 1: ")
title2 = input("Заголовок 2: ")
title3 = input("Заголовок 3: ")
titles_list = [title1, title2, title3]

titles = titles_list
content = input("Введите содержание заметки: ")
status = "В процессе",
created_date = input("Введите дату создания (дд-мм-гггг): ")
issue_date = input("Введите дату выполнения (дд-мм-гггг): ")

note = [
    username,
    titles,
    content,
    status,
    created_date,
    issue_date,
]

print(f"Текущий статуст заметки: {status}")

print("Выберите новый статус для вашей заметки и нажмите Enter:"
      "\n1 - В процессе \n2 - Выполнено \n3 - Отложено")
while True:
    num = input("Ответ: ")
    if num == "1":
        note[status] = "В процессе"
        break
    elif num == "2":
        note[status] = "Выполнено"
        break
    elif num == "3":
        note[status] = "Отложено"
        break
    else:
        print("Ошибка, поторите ввод")

print(note)