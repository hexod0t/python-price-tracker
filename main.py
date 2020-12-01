"""
Created on Tuesday December 01

@author: Another Shell

"""

import pandas as pd
import pandas_datareader as pdr
from time import sleep

symbols = "AMZN GOOG NFLX FB GLD SPY".split()

def get_prices(symbols):
    symbols.sort()
    return pdr.get_quote_yahoo(symbols)['price']

def main():
    while True:
        print(get_prices(symbols))
        print("CNTL + C to quit")
        sleep(5)

if __name__ == "__main__":
    main()