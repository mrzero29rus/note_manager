# Разделите функциональность на функции:

# Функция для получения текущей даты
# Функция для расчёта разницы между датами
# Функция для обработки пользовательского ввода

from datetime import datetime, timedelta

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
    delta = input_issue_date_function().day - datetime.today().day
    print(delta)
    # if timedelta > 1:
    #     print("\nДо даты выполнения:", timedelta, "дней")
    # elif timedelta == 0:
    #     print("\nВнимание! Дата выполнения сегодня!")
    # else:
    #     print("\nВнимание! Дата выполнения истекла", timedelta, "дней назад")


# print("Текущая дата: ", datetime.strftime(current_date, "%d-%m-%Y"))
# print("Дата выполнения: ", datetime.strftime(issue_date, "%d-%m-%Y"))

delta_function()
