import requests
import datetime

dt_now = datetime.datetime.now()
dt_now = str(dt_now).split(' ')[0]


def prise(dataopen, dataclose):
    a = requests.get(
        f'https://iss.moex.com/iss/history/engines/stock/markets/shares/'
        f'boards/TQBR/securities/SBERP.json?from={dataopen}&till={dataclose}').json()
    ansopen = []
    ansclose = []
    for i in a:
        b = a['history']
        deta = b['data']
        for j in deta:
            ansopen.append(j[7])
            ansclose.append(j[11])
    return ansopen[0], ansclose[-1]

print(prise('2024-05-01', '2024-09-01'))
