"""
Created on Tuesday December 01

@author: Another Shell

"""

import pandas as pd
import pandas_datareader as pdr
from time import sleep

symbols = "AMZN GOOG NFLX FB GLD SPY".split()

options = "Track Default List, Show Default List, \
    Add to Default, Edit Default List, Add new List, \
        Quit".split(",")

def show_default():
    pass

def add_to_default():
    pass

def edit_default():
    pass

def add_list():
    pass

def get_prices(symbols):
    symbols.sort()
    return pdr.get_quote_yahoo(symbols)['price']

def main():
    run_program = True
    while run_program:
        print("Choose Options")
        for i in range(len(options) + 1):
            print("{} - {}".format(i, options[i-1]))
        print(get_prices(symbols))
        print("CNTL + C to quit")
        sleep(5)

if __name__ == "__main__":
    main()