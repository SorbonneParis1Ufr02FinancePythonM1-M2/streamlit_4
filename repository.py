import os

from helpers_config import get_serialized_data
from helpers_financialmodelingprep import get_financial_data


def get_config():
    file_name = r"input\config.toml"
    config_path = os.path.join(os.getcwd(), file_name)
    return get_serialized_data(config_path)


def get_data(tickers):
    return get_financial_data(tickers)


if __name__ == "__main__":
    config = get_config()
    print(config)
    print("End config test")

    tickers = ["AAPL", "MSFT", "NVDA"]

    incom_stat, balance_sheet, cash_flow = get_data(tickers)
    print(incom_stat.shape)
    print(balance_sheet.shape)
    print(cash_flow.shape)

