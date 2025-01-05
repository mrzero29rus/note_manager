# импорт классов date и timedelta для работы с датами и разницей между датами
from datetime import date, timedelta

# вывод текущей даты и конвертация в формат д-м-г
current_date = date.today()
print("Дата создания:", date.strftime(current_date, "%d-%m-%y"))

# запрос от пользователя ввода даты выполнения
print("\nВведите дату выполнения")
year = int(input("Введите год: "))
month = int(input("Введите месяц: "))
day = int(input("Введите день: "))
issue_date = date(year, month, day)

# вывод дат создания и выполнения
print("\nДата создания:", date.strftime(current_date, "%d-%m-%y"))
print("Дата выполнения:", date.strftime(issue_date, "%d-%m-%y"))

# расчет дней на исполнение или количества дней просрочки
check_deadline: timedelta = issue_date - current_date
cd = check_deadline.days

# вывод дней на исполнение или количества дней просрочки
if cd > 1:
    print("\nДо даты выполнения:", cd, "дней")
elif cd == 0:
    print("\nВнимание! Дата выполнения сегодня!")
else:
    print("\nВнимание! Дата выполнения истекла", cd, "дней назад")