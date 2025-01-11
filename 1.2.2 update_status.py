# изменение статуса заметки
print("Текущий статуст заметки:", status)
print("Выберите новый статус для вашей заметки и нажмите Enter:"
      "\n1 - В процессе \n2 - Выполнено \n3 - Отложено")
while True:
    num = input("Ответ: ")
    if num == "1":
        status = "В процессе"
        break
    elif num == "2":
        status = "Выполнено"
        break
    elif num == "3":
        status = "Отложено"
        break
    else:
        print("Ошибка, поторите ввод")