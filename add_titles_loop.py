username = input("Введите ваше имя: ")

titles = [] #инициальзация пустого списка
while True:
    title = input("Введите название заметки (введите \"Стоп\" или нажмите \"Enter\" чтобы закончить ввод): ")
    if title == "Стоп" or title == "":
        break #закончить цикл если введено "Стоп" или нажата клавиша "Enter"
    titles.append(title) #добавление в конец списка название введеной заметки

content = input("Введите содержание заметки: ")
created_date = input("Введите дату создания: ")
issue_date = input("Введите дату выполнения: ")

note = [username, titles, content, created_date[:5], issue_date[:5]] #формирование заметки

print("Имя пользовател: ", note[0])
print("Заголовки: ", note[1])
print("Содержание: ", note[2])
print("Дата создания: ", note[3])
print("Дата выполнения: ", note[4])