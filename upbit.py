import time

import requests
import json
import datetime

from const import *


class Upbit:

    def get_market_list(self):
        querystring = {
            "isDetails": "false"
        }

        response = self.get(URL=UPBIT_MARKET_API_URL, params=querystring)
        return json.loads(response.text) if response.status_code == 200 else None

    def get_daily_history(self, market="KRW-BTC"):
        daily_history = []
        day = datetime.datetime.now() - datetime.timedelta(days=1)
        while True:
            daily_candle = self.get_daily_candle(market=market, to=day.strftime('%Y-%m-%d %H:%M:%S'))
            if not daily_candle :
                break
            daily_history.extend(daily_candle)
            last_day_in_daily_candle = daily_candle[-1]['candle_date_time_utc'][:-9]
            last_day_in_daily_candle = datetime.datetime.strptime(last_day_in_daily_candle, '%Y-%m-%d')

            day_ago = last_day_in_daily_candle - datetime.timedelta(days=1)
            day = day_ago

        return daily_history


    def get_daily_candle(self, market="KRW-BTC", to=None, count=200):
        querystring = {
            "market": market,
            "to": to,
            "count": count
        }
        response = self.get(URL=UPBIT_DAILY_PRICE_API_URL, params=querystring)
        return json.loads(response.text) if response.status_code == 200 else None

    def get(self, URL, params):
        time.sleep(0.3)
        return requests.get(url=URL, params=params)