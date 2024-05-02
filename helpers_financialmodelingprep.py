import pandas as pd
import requests
import xlwings as xw


def get_df(url):
    r = requests.get(url)
    data = r.json()
    return pd.DataFrame(data)


def get_financial_data(tickers):
    key = '3RALEHWSAoMGPGqflfzFUb3tEvWeesZh'
    df_is = pd.DataFrame()
    df_bss = pd.DataFrame()
    df_cfs = pd.DataFrame()

    for ticker in tickers:
        url_is = f'https://financialmodelingprep.com/api/v3/income-statement/{ticker}?apikey={key}'
        url_bss = f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{ticker}?&apikey={key}'
        url_cfs = f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?apikey={key}'

        df_is = pd.concat([df_is, get_df(url_is)])
        df_bss = pd.concat([df_bss, get_df(url_bss)])
        df_cfs = pd.concat([df_cfs, get_df(url_cfs)])

    return df_is, df_bss, df_cfs


if __name__ == '__main__':
    tickers = ['AAPL', 'MSFT']
    income_statements, balance_sheet_statements, cash_flow_statements = get_financial_data(tickers)
    xw.view(income_statements)
