username = input("Введите ваше имя: ")
title1 = input("Введите название заметки: ")
title2 = input("Введите название заметки: ")
content = input("Введите содержание заметки: ")
created_date = input("Введите дату создания: ")
issue_date = input("Введите дату выполнения: ")

note = [
    "Имя пользователя: ", username,
    "Заголовки: ", [title1, title2],
    "Содержание: ", content,
    "Дата создания: ", created_date[:5],
    "Дата выполнения: ", issue_date[:5]
]
print(note)