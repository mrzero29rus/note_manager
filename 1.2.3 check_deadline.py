from datetime import datetime

# функция для получения текущей даты
def current_date_function():
    print("Текущая дата:", datetime.strftime(datetime.today(), "%d-%m-%Y"))

# функция для обработки пользовательского ввода
def input_issue_date_function():
    issue_date = datetime.strptime(str(input("Введите дату выполнения (дд-мм-гггг): ")), "%d-%m-%Y")
    print("Дата выполнения:", datetime.strftime(issue_date, "%d-%m-%Y"))

# функция для расчёта разницы между датами
def delta_function():
    issue_date = datetime.strptime(str(input("Введите дату выполнения (дд-мм-гггг): ")), "%d-%m-%Y").date()
    delta = issue_date - datetime.today().date()
    print("Дата выполнения: ", datetime.strftime(issue_date, "%d-%m-%Y"))
    if delta.days > 1:
        print("До даты выполнения:", delta.days, "дней")
    elif delta.days == 0:
        print("Внимание! Дата выполнения сегодня!")
    else:
        print("\Внимание! Дата выполнения истекла", delta.days, "дней назад")

current_date_function()
print()
input_issue_date_function()
print()
delta_function()








# print("Текущая дата: ", datetime.strftime(current_date, "%d-%m-%Y"))
# print("Дата выполнения: ", datetime.strftime(issue_date, "%d-%m-%Y"))