# username = input("Введите ваше имя: ")

titles = []
while True:
    title = input("Введите название заметки (введите \"Стоп\" или нажмите \"Enter\" чтобы закончить ввод): ")
    if title == "Стоп" or title == "":
        break
    else:
        titles.append(title)
print(titles)

# content = input("Введите содержание заметки: ")
# created_date = input("Введите дату создания: ")
# issue_date = input("Введите дату выполнения: ")
#
# note = [username, titles, content, created_date[:5], issue_date[:5]]
#
# print("Имя пользовател: ", note[0])
# print("Заголовки: ", note[1])
# print("Содержание: ", note[2])
# print("Дата создания: ", note[3])
# print("Дата выполнения: ", note[4])
