from datetime import datetime

# функция ввода заголовков
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

# функция получения текущей даты
def current_date_function():
    current_date = datetime.strftime(datetime.today(), "%d-%m-%Y")
    return current_date

# функция получения от пользователя даты выполнения
def input_issue_date_function():
    issue_date = datetime.strptime(str(input("Введите дату выполнения (дд-мм-гггг): ")), "%d-%m-%Y")
    print("Дата выполнения:", datetime.strftime(issue_date, "%d-%m-%Y"))
    return issue_date

# функция расчета дней до даты выполнения, дней просрочки
def delta_function():
    issue_date = datetime.strptime(str(input("Введите дату выполнения (дд-мм-гггг): ")), "%d-%m-%Y").date()
    delta = issue_date - datetime.today().date()
    print("\nДата выполнения: ", datetime.strftime(issue_date, "%d-%m-%Y"))
    if delta.days > 1:
        print("До даты выполнения:", delta.days, "дней")
    elif delta.days == 0:
        print("Внимание! Дата выполнения сегодня!")
    else:
        print("\Внимание! Дата выполнения истекла", delta.days, "дней назад")
# return print???

note = [
    input("Введите ваше имя: "),
    input_titles(),
    input("Введите содержание заметки: "),
    "Новая",
    current_date_function(),
    input_issue_date_function()
]

# изменение статуса заметки
print("Текущий статуст заметки:", note[3])
def update_status_function():
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