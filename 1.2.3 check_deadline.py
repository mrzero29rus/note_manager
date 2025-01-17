from datetime import datetime

# функция для получения текущей даты
def current_date_function():
    print("Текущая дата:", datetime.strftime(datetime.today(), "%d-%m-%Y"))

# функция для обработки пользовательского ввода и расчета даты выполнения
def input_issue_date_function():
    while True:
        try:
            issue_date = datetime.strptime(str(input("Введите дату выполнения (дд-мм-гггг): ")), "%d-%m-%Y").date()
        except:
            print("Введен неверный формат даты, повторите снова")
        else:
            delta = issue_date - datetime.today().date()
            issue_date = datetime.strftime(issue_date, "%d-%m-%Y")
            if delta.days >= 1:
                print("До даты выполнения:", delta.days, "дней")
            elif delta.days == 0:
                print("Внимание! Дата выполнения сегодня!")
            else:
                print("Внимание! Дата выполнения истекла", delta.days, "дней назад")
            return issue_date

current_date_function()
input_issue_date_function()







# print("Текущая дата: ", datetime.strftime(current_date, "%d-%m-%Y"))
# print("Дата выполнения: ", datetime.strftime(issue_date, "%d-%m-%Y"))