# реализован цикл для добавления любого количества заголовков в список
# реализована возможность завершить ввод, указав специальную команду (например, "стоп" или пустой ввод)
# все заголовки добавляются в список

# def input_titles():
#     titles = []
#     while True:
#         title = input("Введите название заметки (введите \"Стоп\" или нажмите \"Enter\" чтобы закончить ввод): ")
#         if title.lower() == "стоп" or title == "":
#             break
#         else:
#             titles.append(title)
#         return titles

# создать функцию
# добавить проверку на уникальность заголовков

def input_titles():
    titles = []
    while True:
        title = input("Введите название заметки\n(введите \"Стоп\" или нажмите \"Enter\" чтобы закончить ввод): ")
        if title.lower() == "стоп" or title == "":
            break
        if title in titles:
            print("Такой заголовок уже существует!")
        else:
            titles.append(title)
    return titles

print(input_titles())