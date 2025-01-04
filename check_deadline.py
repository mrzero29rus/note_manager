from datetime import date, timedelta

current_date = date.today()
print("Дата создания:", date.strftime(current_date, "%d-%m-%y"))

print("\nВведите дату выполнения")
year = int(input("Введите год: "))
month = int(input("Введите месяц: "))
day = int(input("Введите день: "))
issue_date = date(year, month, day)

print("\nДата создания:", date.strftime(current_date, "%d-%m-%y"))
print("Дата выполнения:", date.strftime(issue_date, "%d-%m-%y"))

check_deadline: timedelta = issue_date - current_date
cd = check_deadline.days

if cd > 1:
    print("\nДо даты выполнения:", cd, "дней")
elif cd == 0:
    print("\nВнимание! Дата выполнения сегодня!")
else:
    print("\nВнимание! Дата выполнения истекла", cd, "дней назад")