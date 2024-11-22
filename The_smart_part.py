import requests
import datetime
from dateutil.relativedelta import relativedelta

dt_now = datetime.datetime.now()
dt_now = str(dt_now).split(' ')[0]


def prise(dataopen, dataclose, patern):
    a = requests.get(
        f'https://iss.moex.com/iss/history/engines/stock/markets/shares/'
        f'boards/TQBR/securities/{patern.upper()}.json?from={dataopen}&till={dataclose}').json()
    ansopen = []
    ansclose = []
    sps_stock = []
    name = ''
    for i in a:
        b = a['history']
        deta = b['data']
        for j in deta:
            sps_stock.append(j[3])
            ansopen.append(j[6])
            ansclose.append(j[11])
            name = j[2]
    return ansopen[0], ansclose[-1], sps_stock[0], name



def comparison(dt, mon):
    '''Эта функция берет сегодня время и вычитает кол-во месяцев'''
    dt_sps = list(map(int, dt.split('-')))
    first = datetime.datetime(dt_sps[0], dt_sps[1], 1)
    second = str(first - relativedelta(months=mon)).split()[0]
    return second


print(comparison(dt_now, 1))


def main(dn, patern='SBERP'):
    candle3 = prise(comparison(dn, 3), comparison(dn, 2), patern)[:-1]
    candle2 = prise(comparison(dn, 2), comparison(dn, 1), patern)[:-1]
    candle1 = prise(comparison(dn, 1), comparison(dn, 0), patern)
    name = candle1[-1]
    candle1 = candle1[:-1]
    print(candle3, candle2, candle1)
    if candle3[0] > candle2[0] and candle3[0] > candle1[0] or candle3[1] > candle1[1]:
        return 'Нисходящий тренд', name
    if abs(candle3[0] - candle2[0]) <= 10 and abs(candle2[0] - candle1[0]) <= 10:
        return 'Боковой тренд', name
    return 'Восходящий тренд', name


print(main(dt_now))