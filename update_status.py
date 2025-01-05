# создаем заметку-словарь, начинаем заполнение
note = {}
note["Имя пользоватея"] = input("Введите ваше имя: ")
note["Содержание"] = input("Введите содержание заметки: ")
note["Статус"] = "В процессе"

# ввод любого количества заголовков с возможнотью завершить ввод
titles = []
while True:
    title = input('Введите название заметки (введите "Стоп" или нажмите "Enter" чтобы закончить ввод): ').lower()
    if title == "стоп" or title == "":
        break
    else:
        titles.append(title)
note["Заголовки"] = titles

# вывод текущего состояния заметки
print("\n", note)

# ввод нового статуса заметки
print("\nВыберите новый статус для вашей заметки и нажмите Enter:"
      "\n1 - В процессе \n2 - Выполнено \n3 - Отложено")
while True:
    status = input("Ответ: ")
    if status == "1":
        note["Статус"] = "В процессе"
        break
    elif status == "2":
        note["Статус"] = "Выполнено"
        break
    elif status == "3":
        note["Статус"] = "Отложено"
        break
    else:
        print("Ошибка, поторите ввод")

# вывод финального состояния заметки
print("\n", note)