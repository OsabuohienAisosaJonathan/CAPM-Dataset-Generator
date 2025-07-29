import yfinance as yf
import pandas as pd
import datetime

# 50 diversified U.S. tickers (replace or customize if needed)
tickers = [
    'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'BRK-B', 'JNJ', 'JPM', 'XOM', 'V',
    'PG', 'TSLA', 'NVDA', 'UNH', 'HD', 'MA', 'MRK', 'ABBV', 'PEP', 'KO',
    'PFE', 'AVGO', 'BAC', 'TMO', 'WMT', 'DIS', 'CVX', 'ORCL', 'ACN', 'COST',
    'INTC', 'CMCSA', 'VZ', 'MCD', 'ADBE', 'NFLX', 'ABT', 'CSCO', 'CRM', 'T',
    'DHR', 'TXN', 'NKE', 'QCOM', 'LLY', 'NEE', 'PM', 'MDT', 'AMGN', 'UPS',
    '^GSPC'  # S&P 500 for market reference (will be renamed to sp500)
]

start_date = '2012-01-01'
end_date = datetime.datetime.today().strftime('%Y-%m-%d')

# Download adjusted close prices
prices = yf.download(tickers, start=start_date, end=end_date)['Close']

# Rename S&P 500 column
prices = prices.rename(columns={'^GSPC': 'sp500'})

# Format date
prices = prices.reset_index()
prices['Date'] = prices['Date'].dt.strftime('%d/%m/%Y')

# Reorder columns: Date first
cols = ['Date'] + [col for col in prices.columns if col != 'Date']
prices = prices[cols]

# Save to Excel
prices.to_excel("CAPM_50_Companies_Data.xlsx", index=False)

print("✅ File saved as CAPM_50_Companies_Data.xlsx")
