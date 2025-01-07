def input_titles():
    titles = []
    while True:
        title = input("Введите название заметки (введите \"Стоп\" или нажмите \"Enter\" чтобы закончить ввод): ").lower()
        if title == "стоп" or title == "":
            break
        else:
            titles.append(title)
    return titles

print(input_titles())