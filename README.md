# AlphaVantage

This package (when fully developed) will provide functionality to access various API endpoints for the Alpha Vantage API.

*All end-user functionality exists within the AlphaVantage class in this package.*

Please note that not all endpoints are accessible with this package.  A full list
of accessed endpoints is:

- TIME_SERIES_INTRADAY
- TIME_SERIES_DAILY
- TIME_SERIES_DAILY_ADJUSTED
- TIME_SERIES_WEEKLY
- TIME_SERIES_WEEKLY_ADJUSTED
- TIME_SERIES_MONTHLY
- TIME_SERIES_MONTHLY_ADJUSTED
- SYMBOL_SEARCH
- CURRENCY_EXCHANGE_RATE
- FX_INTRADAY
- FX_DAILY
- FX_WEEKLY
- FX_MONTHLY
- DIGITAL_CURRENCY_DAILY
- DIGITAL_CURRENCY_WEEKLY
- DIGITAL_CURRENCY_MONTHLY

## Getting Started

This section provides instructions for getting this package installed on your
local machine using pip

### Prerequisites

**Python:**  AlphaVantage was developed on Python version 3.7.3, and it is known
to be fully functional on this version of Python.  **NOTE:** Due to the use of f-strings,
AlphaVantage will not work on Python 2.

**Dependencies:**

AlphaVantage requires that the package requests is installed, and it was developed
on requests version 2.22.0.

### Installation

AlphaVantage is not hosted on PyPi, so in order to install it, it has to be first
cloned using Git.  Installation instructions are as follows:

```bash
cd directory_to_place_into
git clone https://github.com/jwrenn4/AlphaVantage.git
cd AlphaVantage
pip install .
```
