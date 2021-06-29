with open('text_1.txt', 'w', encoding='utf-8') as f:
    while True:
        s = input('Введите очередную строку. Для завершения ввода просто нажмите <ENTER> : ')
        if (s == ''):
            break
        f.write(f"{s}\n")

