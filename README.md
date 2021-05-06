# AutoTradeBitCoin
    This is an app use to auto trade Bitcoin. 
    
# Crawl data phase
- Step 1: Checkout to 001_crawl_data branch
- Step 2: Create venv 
- Step 3: Open venv terminal and rund this code `pip install -r requirement.txt`
- Step 4: Run crawl.py file 

# Guide to Run Load data into BQ
- Step1: checkout 003_bq_study branch
- Step2: Create a venv if not exits
- Step3: Open terminal and run this code `pip install -r requirement.txt`
- Step4: Run file bq_code.py

# Run Luigi:
- Open venv terminal: Run code `luigid` to start luigi
- Dry run: Change DRY_RUN = True in config.ini file
- Normal run: Change DRY_RUN = False in config.ini file
- Open another venv terminal and run the code: `PYTHONPATH='./logic:./model:./luigi_wf:./config' luigi --module luigi_wf AllTasks`