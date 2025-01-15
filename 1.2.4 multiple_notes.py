from datetime import datetime

notes =[]

# функция ввода имени пользователя
def input_username_function():
    username = input("Введите имя пользователя: ")
    return username

# функция ввода заголовков
def input_titles_function():
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

# функция ввода содержания заметки
def input_content_function():
    content = input("Введите содержание заметки: ")
    return content

# изменение статуса заметки
def update_status_function():
    print("Текущий статус заметки: Новая")
    print("Выберите новый статус заметки и нажмите \"Enter\": 1 - В процессе; 2 - Выполнено; 3 - Отложено.")
    while True:
        answer = input("Ответ: ")
        if answer == "1":
            status = "В процессе"
            break
        elif answer == "2":
            status = "Выполнено"
            break
        elif answer == "3":
            status = "Отложено"
            break
        else:
            print("Ошибка, повторите ввод")
    return status

# функция получения текущей даты
def current_date_function():
    current_date = datetime.strftime(datetime.today(), "%d-%m-%Y")
    print("Текущая дата:",current_date)
    return current_date

# функция расчета дней до даты выполнения, дней просрочки
def input_issue_date_function():
    issue_date = datetime.strptime(str(input("Введите дату выполнения (дд-мм-гггг): ")), "%d-%m-%Y").date()
    delta = issue_date - datetime.today().date()
    issue_date = datetime.strftime(issue_date, "%d-%m-%Y")
    if delta.days > 1:
        print("До даты выполнения:", delta.days, "дней")
    elif delta.days == 0:
        print("Внимание! Дата выполнения сегодня!")
    else:
        print("Внимание! Дата выполнения истекла", delta.days, "дней назад")
    return issue_date

# сборка заметки
def create_note_function():
    username     = input_username_function()
    titles       = input_titles_function()
    content      = input_content_function()
    status       = update_status_function()
    current_date = current_date_function()
    issue_date   = input_issue_date_function()

    data = [username, titles, content, status, current_date, issue_date]

    note = {
        "Имя пользователя:" : data[0],
        "Заголовки"         : data[1],
        "Содержание"        : data[2],
        "Статус"            : data[3],
        "Дата создания"     : data[4],
        "Дата выполнения"   : data[5]
    }
    notes.append(note)

# функция печати заметки
def print_note_function(note):
    for key, values in note.items():
        print(key, ":", values)


print("Добро пожаловать в \"Менеджер заметок\"! Вы можете добавить новую заметку.")
while True:
    print("Хотите добавить заметку: 1 - Да; 2 - Нет.")
    answer = input("Ответ: ")
    if answer == "1":
        create_note_function()
        print("Заметка сохранена\n")
    elif answer == "2":
        print_note_function()
    else:
        print("Ошибка, повторите ввод")