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

def show_default(symbols):
    symbols.sort()
    return symbols

def add_to_default(symbols):
    print("Enter symbol to add: ")
    symbol = input().upper()
    while symbol != '':
       symbols.append(symbol)
       symbol = input("Enter symbol to add: Hit enter to quit")

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
        for i in range(1, len(options) + 1):
            print("{} - {}".format(i, options[i-1]))
        choice = int(input())

        if choice == 1:
            while True:
               print(get_prices(symbols))
               print("CNTL + C to quit")
               sleep(5)
        if choice == 2:
                print(show_default(symbols))
        if choice == 3:
            add_to_default(symbols)
        if choice == 4:
            edit_default()
        if choice == 5:
            add_list()
        if choice == 6:
            run_program = False

if __name__ == "__main__":
    main()