import requests
import datetime
from dateutil.relativedelta import relativedelta

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


def comparison(dt, mon):
    '''Эта функция берет сегодня время и вычитает кол-во месяцев'''
    dt_sps = list(map(int, dt.split('-')))
    first = datetime.datetime(dt_sps[0], dt_sps[1], 1)
    second = str(first - relativedelta(months=mon)).split()[0]
    return second


print(comparison(dt_now, 1))


def main(dn):
    candle3 = prise(comparison(dn, 4), comparison(dn, 3))
    candle2 = prise(comparison(dn, 3), comparison(dn, 2))
    candle1 = prise(comparison(dn, 2), comparison(dn, 1))
    print(candle3, candle2, candle1)
    f = False

    if f:
        return 'покупаем'
    return 'ждём'


print(main(dt_now))
