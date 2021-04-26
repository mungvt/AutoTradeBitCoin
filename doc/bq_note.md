# Command line BQ
- bq ls: list private databases
- bq ls publicdata: : list public databases
- bq ls db: list all table in the db
- bq load db.tbl file.txt col1:type,col:type,...
- bq show db.tbl: show sture of the table
- bq query "SELECT st FROM db.tbl LIMIT number"
- bq rm -r db





# CURD table
- Create table:
    - Method 1: bq load db.tbl file.txt col1:type,col:type,...
- Update
- Read: bq query "SELECT st FROM db.tbl LIMIT number"

- Delete table: bq rm db.tbl



# Delete data without fee



# Partition by hour
- Create schema: bq mk -t --schema "unix:TIMESTAMP, date:STRING, symbol:STRING, open:FLOAT, high:FLOAT, low:FLOAT, close:FLOAT, Volume_BTC:FLOAT, Volume_USDT:FLOAT, tradecount: STRING" --time_partitioning_field unix --time_partitioning_type HOUR --require_partition_filter --description "This is my partitioned table of bitcoin price by hour" --label org:bitcoin bitcoin_auto_trade.btc_1h
    - Must use "" when use many filed:type instate of ''.
- Load data: bq load bitcoin_auto_trade.btc_1h Binance_BTCUSDT_1h3.txt date:DATETIME,symbol:STRING,open:FLOAT,high:FLOAT,low:FLOAT,close:FLOAT,Volume_BTC:FLOAT,Volume_USDT:FLOAT,tradecount:STRING