# Разделите функциональность на функции:

# Функция для получения текущей даты
# Функция для расчёта разницы между датами
# Функция для обработки пользовательского ввода

from datetime import datetime

# функция получения текущей даты и конвертация в формат дд-мм-гггг
def current_date_function():
    current_date = datetime.strftime(datetime.today(), "%d-%m-%Y")
    return current_date

# запрос от пользователя ввода даты выполнения
def input_issue_date_function():
    issue_date = datetime.strptime(str(input("Введите дату выполнения (дд-мм-гггг): ")), "%d-%m-%Y")
    print("Дата выполнения:", datetime.strftime(issue_date, "%d-%m-%Y"))
    return issue_date

# расчет дней на исполнение или количества дней просрочки
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

# print("Текущая дата: ", datetime.strftime(current_date, "%d-%m-%Y"))
# print("Дата выполнения: ", datetime.strftime(issue_date, "%d-%m-%Y"))

delta_function()

'''
сделать проверку на правильность ввода
убрать "минус" если дата выполнения истекла
'''