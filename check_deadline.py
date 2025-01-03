import datetime

# current_date = datetime.date.today()
# print(datetime.datetime.strftime(current_date, "%d-%m-%y"))

# issue_date = input("Введите дату: ")
# print(issue_date)

from datetime import date

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
d = date(day-month-year)
print(d)
