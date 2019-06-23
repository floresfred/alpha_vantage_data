from .core import requests, BASE_URL, ENDPOINTS

class AlphaVantage:

    '''Wrapper class that allows the user to hit various endpoints of the AlphaVantage
    API.  For more information about Alpha Vantage or its API documentation, see
    alphavantage.co

    NOTE: Not all endpoints are available through this class, but most are.

    Parameters
    ----------
    key : str
        Your personal API key
    '''

    def __init__(self, key, test = True):
        self.key = key
        self.test = test
        self._session = requests.Session()

    @property
    def key(self):
        return self._key
    @key.setter
    def key(self, value):
        if not isinstance(value, str):
            raise TypeError('key must be string')
        self._key = value

    @property
    def test(self):
        return self._test
    @test.setter
    def test(self, value):
        if not isinstance(value, bool):
            raise TypeError('test must be Boolean')
        self._test = value

    @property
    def outputsize(self):
        if self.test:
            return 'compact'
        return 'full'

    def _check_resp(self, resp):
        '''Check whether a response came back correctly'''

        #first check the response code and make sure it's 200
        #if not, raise Warning
        if resp.status_code != 200:
            raise Warning(f'Unexpected Response Code {resp.status_code}')

        #we know response came back, so populate the json
        data = resp.json()

        #if there is an error, then data.get('Error Message') != None
        error = data.get('Error Message')
        if error:
            raise ValueError(error)

        #if not errors, then return data
        return data

    def get_intraday(self, symbol, interval = '1min'):
        '''Hit the TIME_SERIES_INTRADAY endpoint

        Parameters
        ----------
        symbol : str
            The symbol for the stock wanted
        interval : str (default '1min')
            The interval between each data point
        outputsize : str (default 'full')
            Either one of 'full', 'compact'.  If 'compact', only returns 100
            entries

        Returns
        -------
        data : dict
            The data returned by the API
        '''

        #format the url
        url = f'{BASE_URL}{ENDPOINTS.get("intraday")}&symbol={symbol}&interval={interval}&outputsize={self.outputsize}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_daily(self, symbol):
        '''Hit the TIME_SERIES_DAILY endpoint

        Parameters
        ----------
        symbol : str
            The symbol for the stock wanted
        outputsize : str (default 'full')
            Either one of 'full', 'compact'.  If 'compact', only returns 100
            entries

        Returns
        -------
        data : dict
            The data returned by the API
        '''

        #format the url
        url = f'{BASE_URL}{ENDPOINTS.get("daily")}&symbol={symbol}&outputsize={self.outputsize}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_daily_adjusted(self, symbol):
        '''Hit the TIME_SERIES_DAILY_ADJUSTED endpoint

        Parameters
        ----------
        symbol : str
            The symbol for the stock wanted
        outputsize : str (default 'full')
            Either one of 'full', 'compact'.  If 'compact', only returns 100
            entries

        Returns
        -------
        data : dict
            The data returned by the API
        '''

        #format the url
        url = f'{BASE_URL}{ENDPOINTS.get("daily adjusted")}&symbol={symbol}&outputsize={self.outputsize}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_weekly(self, symbol,):
        '''Hit the TIME_SERIES_WEEKLY endpoint

        Parameters
        ----------
        symbol : str
            The symbol for the stock wanted
        outputsize : str (default 'full')
            Either one of 'full', 'compact'.  If 'compact', only returns 100
            entries

        Returns
        -------
        data : dict
            The data returned by the API
        '''

        #format url
        url = f'{BASE_URL}{ENDPOINTS.get("weekly")}&symbol={symbol}&outputsize={self.outputsize}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_weekly_adjusted(self, symbol):
        '''Hit the TIME_SERIES_WEEKLY_ADJUSTED endpoint

        Parameters
        ----------
        symbol : str
            The symbol for the stock wanted
        outputsize : str (default 'full')
            Either one of 'full', 'compact'.  If 'compact', only returns 100
            entries

        Returns
        -------
        data : dict
            The data returned by the API
        '''

        #format the url
        url = f'{BASE_URL}{ENDPOINTS.get("weekly adjusted")}&symbol={symbol}&outputsize={self.outputsize}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_monthly(self, symbol):
        '''Hit the TIME_SERIES_MONTHLY endpoint

        Parameters
        ----------
        symbol : str
            The symbol for the stock wanted
        outputsize : str (default 'full')
            Either one of 'full', 'compact'.  If 'compact', only returns 100
            entries

        Returns
        -------
        data : dict
            The data returned by the API
        '''

        #format the url
        url = f'{BASE_URL}{ENDPOINTS.get("monthly")}&symbol={symbol}&outputsize={self.outputsize}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_monthly_adjusted(self, symbol):
        '''Hit the TIME_SERIES_MONTHLY_ADJUSTED endpoint

        Parameters
        ----------
        symbol : str
            The symbol for the stock wanted
        outputsize : str (default 'full')
            Either one of 'full', 'compact'.  If 'compact', only returns 100
            entries

        Returns
        -------
        data : dict
            The data returned by the API
        '''

        #format the url
        url = f'{BASE_URL}{ENDPOINTS.get("monthly adjusted")}&symbol={symbol}&outputsize={self.outputsize}&apikey={self.key}'

        #get and check
        resp =self._session.get(url)
        return self._check_resp(resp)

    def search(self, keywords):
        '''Hit the SYMBOL_SEARCH endpoint

        Parameters
        ----------
        keywords : str
            The search string

        Returns
        -------
        results : dict
            The search results returned by the API
        '''

        #format the url
        url = f'{BASE_URL}{ENDPOINTS.get("search")}&keywords={keywords}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_exchange_rate(self, from_currency, to_currency):
        '''Hit the CURRENCY_EXCHANGE_RATE endpoint

        Parameters
        ----------
        from_currency : str
            The symbol of the first currency
        to_currency : str
            The symbol of the second currency

        Returns
        -------
        exchange_data : dict
            The exchange data results returned by the API
        '''

        #format the url
        url = f'{BASE_URL}{ENDPOINTS.get("exchange")}&from_currency={from_currency}&to_currency={to_currency}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_fx_intraday(self, from_symbol, to_symbol, interval = '1min', outputsize = 'full'):
        '''Hit the FX_INTRADAY endpoint

        Parameters
        ----------
        from_symbol : str
            The symbol of the first currency
        to_symbol : str
            The symbol of the second currency
        interval : str (default '1min')
            The interval between each data point
        outputsize : str (default 'full')
            Either one of 'full', 'compact'.  If 'compact', only returns 100
            entries

        Returns
        -------
        data : dict
            The exchange data returned by the API
        '''

        #foramt url
        url = f'{BASE_URL}{ENDPOINTS.get("fx intraday")}&from_symbol={from_symbol}&to_symbol={to_symbol}&interval={interval}&outputsize={self.outputsize}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_fx_daily(self, from_symbol, to_symbol):
        '''Hit the FX_DAILY endpoint

        Parameters
        ----------
        from_symbol : str
            The symbol of the first currency
        to_symbol : str
            The symbol of the second currency
        outputsize : str (default 'full')
            Either one of 'full', 'compact'.  If 'compact', only returns 100
            entries

        Returns
        -------
        data : dict
            The exchange data returned by the API
        '''

        #format the url
        url = f'{BASE_URL}{ENDPOINTS.get("fx daily")}&from_symbol={from_symbol}&to_symbol={to_symbol}&outputsize={self.outputsize}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_fx_weekly(self, from_symbol, to_symbol):
        '''Hit the FX_WEEKLY endpoint

        Parameters
        ----------
        from_symbol : str
            The symbol of the first currency
        to_symbol : str
            The symbol of the second currency
        outputsize : str (default 'full')
            Either one of 'full', 'compact'.  If 'compact', only returns 100
            entries

        Returns
        -------
        data : dict
            The exchange data returned by the API
        '''

        #format url
        url = f'{BASE_URL}{ENDPOINTS.get("fx weekly")}&from_symbol={from_symbol}&to_symbol={to_symbol}&outputsize={self.outputsize}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_fx_monthly(self, from_symbol, to_symbol):
        '''Hit the FX_MONTHLY endpoint

        Parameters
        ----------
        from_symbol : str
            The symbol of the first currency
        to_symbol : str
            The symbol of the second currency
        outputsize : str (default 'full')
            Either one of 'full', 'compact'.  If 'compact', only returns 100
            entries

        Returns
        -------
        data : dict
            The exchange data returned by the API
        '''

        #format url
        url = f'{BASE_URL}{ENDPOINTS.get("fx monthly")}&from_symbol={from_symbol}&to_symbol={to_symbol}&outputsize={self.outputsize}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_crypto_daily(self, symbol, market):
        '''Hit the DIGITAL_CURRENCY_DAILY endpoint

        Parameters
        ----------
        symbol : str
            The symbol of the digital currency
        market : str
            The symbol for the market

        Returns
        -------
        data : dict
            The data returned by the API
        '''

        #format url
        url = f'{BASE_URL}{ENDPOINTS.get("crypto daily")}&symbol={symbol}&market={market}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_crypto_weekly(self, symbol, market):
        '''Hit the DIGITAL_CURRENCY_WEEKLY endpoint

        Parameters
        ----------
        symbol : str
            The symbol of the digital currency
        market : str
            The symbol for the market

        Returns
        -------
        data : dict
            The data returned by the API
        '''

        #format url
        url = f'{BASE_URL}{ENDPOINTS.get("crypto weekly")}&symbol={symbol}&market={market}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)

    def get_crypto_monthly(self, symbol, market):
        '''Hit the DIGITAL_CURRENCY_MONTHLY endpoint

        Parameters
        ----------
        symbol : str
            The symbol of the digital currency
        market : str
            The symbol for the market

        Returns
        -------
        data : dict
            The data returned by the API
        '''

        #format url
        url = f'{BASE_URL}{ENDPOINTS.get("crypto monthly")}&symbol={symbol}&market={market}&apikey={self.key}'

        #get and check
        resp = self._session.get(url)
        return self._check_resp(resp)
