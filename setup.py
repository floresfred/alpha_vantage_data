from distutils.core import setup
from AlphaVantage.__init__ import __version__

setup(
name = 'AlphaVantage',
version = __version__,
packages = ['AlphaVantage'],
author_name = 'Jacob Renn',
author_email = 'jwrenn4@outlook.com',
install_requires = ['requests'],
description = 'Python package for hitting the Alpha Vantage set of APIs',
long_description = open('README.md','r').read()
)
