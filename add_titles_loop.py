titles = []
while True:
    title = input("Введите название заметки (введите \"Стоп\" или нажмите \"Enter\" чтобы закончить ввод): ")
    if title.lower() == "стоп" or title == "":
        break
    else:
        titles.append(title)
print(titles)

# добавить проверку на уникальность заголовков