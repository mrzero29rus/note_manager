username = input("Введите ваше имя: ")
title1 = input("Введите название заметки: ")
title2 = input("Введите название заметки: ")
content = input("Введите содержание заметки: ")
created_date = input("Введите дату создания: ")
issue_date = input("Введите дату выполнения: ")

note = [
    username,
    [title1, title2],
    content,
    created_date,
    issue_date
]
print(note)