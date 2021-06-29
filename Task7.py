import json

profits = {}
avg_profit = {}
sum = 0
cnt = 0
with open('text_7.txt', 'r', encoding='utf-8') as f:
    for s in f.readlines():
        my_list = s.split()
        profit = float(my_list[2]) - float(my_list[3])
        profits[my_list[1] + ' ' + my_list[0]] = profit
        if profit >= 0:
            sum += profit
            cnt += 1
    avg_profit["average_profit"] = sum / cnt
with open('text_7.json', 'w', encoding='utf-8') as f:
    json.dump([profits, avg_profit], f, ensure_ascii=False)
