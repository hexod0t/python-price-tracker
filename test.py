"""
Created on Tuesday December 01

@author: Another Shell

"""

import pandas as pd
import pandas_datareader as pdr

print(pdr.get_quote_yahoo("AAPL")['price'])