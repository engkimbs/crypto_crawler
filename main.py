import requests

from const import UPBIT_MARKET_API_URL

from upbit import *

if __name__ == '__main__':
    Upbit = Upbit()
    upbit_market_list = Upbit.get_market_list()
    print(upbit_market_list)
    upbit_BTC_candles = Upbit.get_daily_history()
    print(upbit_BTC_candles)
    print(len(upbit_BTC_candles))
    for upbit_BTC in upbit_BTC_candles:
        print(upbit_BTC)
