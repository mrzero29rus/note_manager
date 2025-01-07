# from datetime import datetime, timedelta
#
# current_date = datetime.today()
# print("Текущая дата: ", datetime.strftime(current_date, "%d-%m-%Y"))
#
#
# input_date = str(input("Введите дату (дд-мм-гггг): "))
# issue_date = datetime.strptime(input_date, "%d-%m-%Y")
#
#
# print("Текущая дата: ", datetime.strftime(current_date, "%d-%m-%Y"))
# print("Дата выполнения: ", datetime.strftime(issue_date, "%d-%m-%Y"))
#
#
# delta = issue_date - current_date
# print("До даты выполнения:", datetime.strftime(delta, "%d дней %H часов %M минут"))



note = {}
note["Имя пользоватея"] = input("Введите ваше имя: ")
note["Содержание"] = input("Введите содержание заметки: ")
note["Статус"] = "В процессе"

from add_titles_loop import input_titles
input_titles()

print(note)