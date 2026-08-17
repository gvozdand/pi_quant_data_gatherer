#We will gather historical options chain data
import pandas as pd
import polars as pl
import numpy as np
import yfinance as yf
import selenium


def options_chain_pull():

    #we will gather options chain history for the S&P 500 basket

    driver = webdriver.Chrome()
    driver.get("https://stockti.com/stocks/sp500")
    pulled_tickers = driver.find_elements(By.XPATH, "//a[contains(@href, '/stock/')]")


    spy = yf.Ticker("SPY")
    spy_basket = spy.funds_data
    for key, value in spy_basket.items():
        print(key)
        print(value)
    print(spy_basket)




def main():

    options_chain_pull()





    return 0



if __name__ == "__main__":
    main()







