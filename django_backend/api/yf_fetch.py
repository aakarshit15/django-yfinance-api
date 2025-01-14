import yfinance as yf
import pandas as pd
import json
from datetime import datetime

# Helper Functions
def convert_timestamps_to_strings(data):
    if isinstance(data, dict):
        return {str(key): convert_timestamps_to_strings(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [convert_timestamps_to_strings(item) for item in data]
    else:
        return data

def convert_timestamp_to_string(timestamp):
    return timestamp.strftime("%Y-%m-%d %H:%M:%S") if isinstance(timestamp, (datetime, pd.Timestamp)) else str(timestamp)

def convert_data_to_json(data):
    if data is not None:
        data_dict = data.to_dict()
        data_dict = convert_timestamps_to_strings(data_dict)
        data_json = json.dumps(data_dict, indent=4)
    else:
        data_json = json.dumps({"error": "No data available"}, indent=4)
    return data_json

def convert_to_json(data):
    if isinstance(data, dict):  # Handle dictionaries
        for key, value in data.items():
            if isinstance(value, (datetime, pd.Timestamp)):
                data[key] = convert_timestamp_to_string(value)
    elif isinstance(data, pd.DataFrame):  # Handle DataFrames
        data = data.reset_index()
        for col in data.columns:
            if pd.api.types.is_datetime64_any_dtype(data[col]):
                data[col] = data[col].apply(convert_timestamp_to_string)
        data = data.to_dict(orient="records")  # Convert DataFrame to list of dictionaries
    elif isinstance(data, pd.Series):  # Handle Series
        data = data.to_dict()

    return json.dumps(data, indent=4)

# Function to fetch balance sheet as JSON for single ticker
def get_balance_sheet_as_json(ticker_symbol, **kwargs):
    try:
        my_data = yf.Ticker(ticker_symbol)
        my_balance_sheet = my_data.balance_sheet
        balance_sheet_json = convert_data_to_json(my_balance_sheet)
        return balance_sheet_json
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=4)

# Function to fetch cash flow as JSON for single ticker
def get_cash_flow_as_json(ticker_symbol, **kwargs):
    try:
        my_data = yf.Ticker(ticker_symbol)
        my_cash_flow = my_data.cashflow
        cash_flow_json = convert_data_to_json(my_cash_flow)
        return cash_flow_json
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=4)

# Function to fetch historical data for single or multiple tickers
def get_historical_data(tickers, **kwargs):
    if isinstance(tickers, str):
        tickers = [tickers]

    result = {}
    for ticker in tickers:
        data = yf.Ticker(ticker).history(**kwargs)
        result[ticker] = convert_to_json(data)
    return result if len(result) > 1 else result[tickers[0]]

# Function to fetch sector and industry data for single or multiple tickers
def get_sector_and_industry(tickers, **kwargs):
    if isinstance(tickers, str):
        tickers = [tickers]

    result = {}
    for ticker in tickers:
        info = yf.Ticker(ticker).info
        sector = info.get("sector", "N/A")
        industry = info.get("industry", "N/A")
        result[ticker] = {"sector": sector, "industry": industry}
    return convert_to_json(result) if len(result) > 1 else convert_to_json(result[tickers[0]])

# Function to fetch calendar data for single ticker
def get_calendar_as_json(ticker_symbol, **kwargs):
    try:
        my_data = yf.Ticker(ticker_symbol)
        my_calendar = my_data.calendar
        calendar_json = convert_data_to_json(my_calendar)
        return calendar_json
    except Exception as e:
        return json.dumps({"error": str(e)}, indent=4)

# Example usage
if __name__ == "__main__":

    single_ticker = "AAPL"
    multiple_tickers = ["AAPL", "MSFT", "GOOGL"]

    # # Balance sheet for a single ticker
    # print("Balance Sheet for Single Ticker:")
    # print(get_balance_sheet_as_json(single_ticker))

    # # Cash flow for a single ticker
    # print("\nCash Flow for Single Ticker:")
    # print(get_cash_flow_as_json(single_ticker))

    # # Historical data for single ticker
    # print("\nHistorical Data for Single Ticker:")
    # print(get_historical_data(single_ticker))

    # # Historical data for multiple tickers
    # print("\nHistorical Data for Multiple Tickers:")
    # print(get_historical_data(multiple_tickers))

    # # Sector / Industry information for single ticker
    # print("\nSector and Industry Data for Single Ticker:")
    # print(get_sector_and_industry(single_ticker))

    # # Sector / Industry information for multiple tickers
    # print("\nSector and Industry Data for Multiple Tickers:")
    # print(get_sector_and_industry(multiple_tickers))

    # # Calendar information for single ticker
    # print("\nCalendar Information for Single Ticker:")
    # print(get_calendar_as_json(single_ticker))
