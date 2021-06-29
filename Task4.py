my_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
target = []
with open('text_4.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for s in lines:
        target.append(s.replace(s.split()[0], my_dic[s.split()[0]]))
with open('text_4_out.txt', 'w', encoding='utf-8') as f:
    f.writelines(target)
