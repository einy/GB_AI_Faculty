with open('text_2.txt', 'r', encoding='utf-8') as f:
    my_line = f.readlines()
    enum_obj = enumerate(my_line)
    for i, s in enum_obj:
        print(f"Строка №{i+1} - {len(s.split())} слов")
    print(f"Всего строк в файле: {i+1}")
