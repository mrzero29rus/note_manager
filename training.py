note = []

print("Выберите новый статус для вашей заметки и нажмите Enter:"
      "\n1 - В процессе \n2 - Выполнено \n3 - Отложено")

while True:
    num = input("Ответ: ")
    if num == 1:
        note[status] = "В процессе"
        break
    elif num == 2:
        note[status] = "Выполнено"
        break
    elif num == 3:
        note[status] = "Отложено"
        break
    else:
        print("Ошибка, поторите ввод")

print(note)