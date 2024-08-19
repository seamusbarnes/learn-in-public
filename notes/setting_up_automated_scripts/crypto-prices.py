#!/usr/bin/env python3

import requests

def get_binance_price(symbol):
    """
    Retrieve the current price of a cryptocurrency symbol from the Binance API.
    
    Parameters:
        symbol (str): The symbol of the cryptocurrency to fetch, e.g., 'BTCUSDT'.
    
    Returns:
        dict: A dictionary containing the current price data.
    """
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    response = requests.get(url)
    data = response.json()
    return data

def get_daily_open_price(symbol, interval='1d'):
    """
    Retrieve the opening price of a cryptocurrency symbol for a given interval from the Binance API.
    
    Parameters:
        symbol (str): The symbol of the cryptocurrency to fetch, e.g., 'BTCUSDT'.
        interval (str): The time interval for the data, defaults to '1d' (one day).
    
    Returns:
        float or None: The opening price as a float if successful, None if an error occurs.
    """
    url = 'https://api.binance.com/api/v3/klines'
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': 1
    }
    response = requests.get(url, params=params)
    data = response.json()

    try:
        open_price = data[0][1]
        return float(open_price)
    except Exception as e:
        print(f'Error occurred: {e}')
        return None

# Example usage of the functions
if __name__ == "__main__":
    print('\nPrices - Current')
    unit = 'USDT'
    symbols = ['BTC', 'ETH', 'LINK', 'DOT', 'ADA']

    for symbol in symbols:
        price_data = get_binance_price(f'{symbol}{unit}')
        print(f"{symbol}: {price_data['price']} {unit}")

    print('\nPrices - Daily Open')
    for symbol in symbols:
        price = get_daily_open_price(f'{symbol}{unit}')
        if price is not None:
            print(f'{symbol}: ${price} {unit}')
        else:
            print(f'Failed to fetch opening price for {symbol}.')
