from datetime import datetime

current_date = datetime.today()
print("Текущая дата: ", datetime.strftime(current_date, "%d-%m-%Y"))


input_date = str(input("Введите дату (дд-мм-гггг): "))
issue_date = datetime.strptime(input_date, "%d-%m-%Y")


print("Текущая дата: ", datetime.strftime(current_date, "%d-%m-%Y"))
print("Дата выполнения: ", datetime.strftime(issue_date, "%d-%m-%Y"))