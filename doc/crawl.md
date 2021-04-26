- guide: https://betterprogramming.pub/easiest-way-to-use-the-bitmex-api-with-python-fbf66dc38633
- binance_api: https://www.binance.com/en/my/settings/api-management
    - sdt: 0328808826
    - email: vutienmung@gmail.com
    - mk: Mung1234
- python-binance: https://python-binance.readthedocs.io/en/latest/overview.html

# Crawl data phase
- Step 1: Checkout to 001_crawl_data branch
- Step 2: Create venv 
- Step 3: Open venv terminal and rund this code `pip install -r requirement.txt`
- Step 4: Run crawl.py file
# Meaning of columns
- timestamp = A day of trade time
- open = Open BTC price by USDT
- high = High BTC price by USDT
- low = Low BTC price by USDT
- close = Close BTC price by USDT
- volume = Volume BTC by BTC
- close_time = Close time
- quote_av = Quote asset volume // Volume BTC by USDT
- trades = Number of trades
- tb_base_av = Taker buy base asset volume
- tb_quote_av = Taker buy quote asset volume
- ignore = Ignore.