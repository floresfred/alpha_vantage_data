from .core import requests, BASE_URL, ENDPOINTS

class AlphaVantage:

    def __init__(self, key):
        self.key = key
        self._session = requests.Session()

    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, value):
        if not isinstance(value, str):
            raise TypeError('key must be string')
        self._key = value

    def _check_resp(self, resp):
        if resp.status_code != 200:
            raise Warning(f'Unexpected Response Code {resp.status_code}')
        data = resp.json()
        possible_error = data.get('Error Message')
        if possible_error:
            raise ValueError(possible_error)
        return resp.json()

    def get_intraday(self, symbol, interval = '1min', outputsize='full'):
        url = f'{BASE_URL}{ENDPOINTS.get("intraday")}&symbol={symbol}&interval={interval}&outputsize={outputsize}&apikey={self.key}'
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_daily(self, symbol, outputsize = 'full'):
        url = f'{BASE_URL}{ENDPOINTS.get("daily")}&symbol={symbol}&outputsize={outputsize}&apikey={self.key}'
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_daily_adjusted(self, symbol, outputsize = 'full'):
        url = f'{BASE_URL}{ENDPOINTS.get("daily adjusted")}&symbol={symbol}&outputsize={outputsize}&apikey={self.key}'
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_weekly(self, symbol, outputsize = 'full'):
        url = f'{BASE_URL}{ENDPOINTS.get("weekly")}&symbol={symbol}&outputsize={outputsize}&apikey={self.key}'
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_weekly_adjusted(self, symbol, outputsize = 'full'):
        url = f'{BASE_URL}{ENDPOINTS.get("weekly adjusted")}&symbol={symbol}&outputsize={outputsize}&apikey={self.key}'
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_monthly(self, symbol, outputsize = 'full'):
        url = f'{BASE_URL}{ENDPOINTS.get("monthly")}&symbol={symbol}&outputsize={outputsize}&apikey={self.key}'
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_monthly_adjusted(self, symbol, outputsize = 'full'):
        url = f'{BASE_URL}{ENDPOINTS.get("monthly adjusted")}&symbol={symbol}&outputsize={outputsize}&apikey={self.key}'
        resp =self._session.get(url)
        return self._check_resp(resp)

    def search(self, keywords):
        url = f'{BASE_URL}{ENDPOINTS.get("search")}&keywords={keywords}&apikey={self.key}'
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_exchange_rate(self, from_currency, to_currency):
        url = f'{BASE_URL}{ENDPOINTS.get("exchange")}&from_currency={from_currency}&to_currency={to_currency}&apikey={self.key}'
        resp = self._session.get(url)
        return self._check_resp(resp)

    #def get_fx_intraday(self, )
