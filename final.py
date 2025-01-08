# создание списка для хранения информации о заметке
# заголовки добавлены в отдельный вложенный список внутри основного списка

username = input("Введите ваше имя: ")

title1 = input("Заголовок 1: ")
title2 = input("Заголовок 2: ")
title3 = input("Заголовок 3: ")
titles_list = [title1, title2, title3]

titles = titles_list
content = input("Введите содержание заметки: ")
status = input("Введите статус заметки: "),
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

print("Имя пользователя:", note[0],
      "Заголовки:", note[1],
      "Содержание:", note[2],
      "Статус:", note[3],
      "Дата создания:", note[4],
      "Дата выполнения:",note[5])