import requests

data = input('Введите дату в формате гггг-мм-дд чтобы узнать сколько стоила акция в этот день')

a = requests.get(
    f'https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/SBERP.json?from={data}&till={data}').json()
f = True
for i in a:
    if f:
        b = a['history']
        deta = b['data']
        for j in deta:
            print(j)
            print(f'Акция: {j[3]} \n Дата:{j[1]}\n Цена открытия {j[7]} \n цена закрытия {j[11]}')
            f = False
            break
