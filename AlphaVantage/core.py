import requests

BASE_URL = 'https://www.alphavantage.co/query?'

ENDPOINTS = {
    'intraday':'function=TIME_SERIES_INTRADAY',
    'daily':'function=TIME_SERIES_DAILY',
    'daily adjusted':'function=TIME_SERIES_DAILY_ADJUSTED',
    'weekly':'function=TIME_SERIES_WEEKLY',
    'weekly adjusted':'function=TIME_SERIES_WEEKLY_ADJUSTED',
    'monthly':'function=TIME_SERIES_MONTHLY',
    'monthly adjusted':'function=TIME_SERIES_MONTHLY_ADJUSTED',
    'search':'function=SYMBOL_SEARCH',
    'exchange':'function=CURRENCY_EXCHANGE_RATE',
    'fx intraday':'function=FX_INTRADAY',
    'fx daily':'function=FX_DAILY',
    'fx weekly':'function=FX_WEEKLY',
    'fx monthly':'function=FX_MONTHLY',
    'crypto daily':'function=DIGITAL_CURRENCY_DAILY',
    'crypto weekly':'function=DIGITAL_CURRENCY_WEEKLY',
    'crypto monthly':'function=DIGITAL_CURRENCY_MONTHLY',

}
