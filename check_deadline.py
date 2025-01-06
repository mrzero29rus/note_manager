from datetime import datetime, timedelta
from os import remove

# получение текущей даты, конвертация в формат дд-мм-гггг и вывод на экран
current_date = datetime.today()
print("Текущая дата: ", datetime.strftime(current_date, "%d-%m-%Y"))

# запрос от пользователя ввода даты выполнения
input_date = str(input("Введите дату выполнения (дд-мм-гггг): "))
issue_date = datetime.strptime(input_date, "%d-%m-%Y")

print("Текущая дата: ", datetime.strftime(current_date, "%d-%m-%Y"))
print("Дата выполнения: ", datetime.strftime(issue_date, "%d-%m-%Y"))

# расчет дней на исполнение или количества дней просрочки
delta = issue_date.day - current_date.day

# вывод дней на исполнение или количества дней просрочки
if delta > 1:
    print("\nДо даты выполнения:", delta, "дней")
elif delta == 0:
    print("\nВнимание! Дата выполнения сегодня!")
else:
    print("\nВнимание! Дата выполнения истекла", delta, "дней назад")