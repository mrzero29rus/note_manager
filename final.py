username = input("Введите ваше имя: ")
title1 = input("Введите название заметки: ")
title2 = input("Введите название заметки: ")
content = input("Введите содержание заметки: ")
created_date = input("Введите дату создания: ")
issue_date = input("Введите дату выполнения: ")

note = [username, [title1, title2], content, created_date[:5], issue_date[:5]]

print("Имя пользовател: ", note[0])
print("Заголовки: ", note[1])
print("Содержание: ", note[2])
print("Дата создания: ", note[3])
print("Дата выполнения: ", note[4])