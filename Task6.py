import re

my_dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as f:
    for s in f.readlines():
        subject = re.search(r"(\w*):", s).group(1)
        my_dict[subject] = 0
        for match in re.finditer(r"(\d*)\(\w*\)", s):
            my_dict[subject] += int(match.group(1))
print(my_dict)
