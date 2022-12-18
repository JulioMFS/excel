# Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

# fix_yahoo_finance is used to fetch data
#import fix_yahoo_finance as yf
import yfinance as yf
yf.pdr_override()

# input
symbol = 'AAPL' # Apple Company
start = '2018-01-01'
end = '2021-10-01'

# Read data
df = yf.download(symbol,start,end)

# View Columns
df.head()
