
# NSE Data Fetcher - Python Script Documentation

This Python script is designed to fetch historical data, market capitalization, and NIFTY 50 index historical data from the National Stock Exchange (NSE) of India. It uses Python's `requests` module to interact with NSE APIs and provides the data in structured formats such as pandas DataFrames or JSON objects.

## **Features**
1. **Historical Data for Individual Stocks:**
   - Fetch daily price and trade information for a given stock symbol and date range.
   - Supports equity series filtering.

2. **Market Capitalization Information:**
   - Retrieve the latest market cap and trade information for a given stock symbol.

3. **NIFTY 50 Historical Data:**
   - Fetch historical index data for NIFTY 50 within a specified date range.

---

## **Dependencies**
Ensure you have the following Python libraries installed:
- `requests`
- `pandas`
- `datetime`

Install them using:
```bash
pip install requests pandas
```

---

## **Usage**
### **Initialization**
The `NSE` class is used to initialize a session with NSE's website and APIs:
```python
nse = NSE(timeout=10)
```
- **`timeout`**: Optional parameter to specify the request timeout in seconds.

---

### **Methods**
#### **1. Get Historical Data for Stocks**
Fetch historical price and trade data for a specific stock symbol:
```python
df = nse.getHistoricalData('ONGC', 'EQ', from_date, to_date)
```
- **Parameters**:
  - `symbol`: Stock symbol (e.g., "ONGC").
  - `series`: Series type (e.g., "EQ" for equity).
  - `from_date`: Start date (datetime object).
  - `to_date`: End date (datetime object).
- **Returns**:
  - A pandas DataFrame containing historical data or `None` if the request fails.

---

#### **2. Get Market Capitalization**
Retrieve the market capitalization and trade information of a stock:
```python
trade_info = nse.getmarketCap()
```
- **Parameters**: None (hardcoded for "ONGC").
- **Returns**:
  - JSON object containing market trade information or `None` if the request fails.

---

#### **3. Get NIFTY 50 Historical Data**
Fetch historical index data for the NIFTY 50:
```python
trade_info = nse.getNifty50HistoricalData(from_date, to_date)
```
- **Parameters**:
  - `from_date`: Start date (datetime object).
  - `to_date`: End date (datetime object).
- **Returns**:
  - JSON object containing historical index records or `None` if the request fails.

---

### **Example Usage**
```python
from datetime import date
nse = NSE()

# Fetch historical data for ONGC
df = nse.getHistoricalData('ONGC', 'EQ', date(2024, 12, 1), date(2024, 12, 5))
print(df)

# Fetch market capitalization for ONGC
trade_info = nse.getmarketCap()
print(trade_info)

# Fetch NIFTY 50 historical data
nifty_data = nse.getNifty50HistoricalData(date(2024, 12, 1), date(2024, 12, 5))
print(nifty_data)
```

---

## **Error Handling**
- The script includes basic error handling to print error messages when requests fail.
- If an API endpoint returns an invalid response or an exception occurs, the method returns `None`.

---

## **Notes**
- **NSE API Restrictions**: NSE often blocks automated scripts. Ensure your script mimics browser behavior by setting appropriate headers (`User-Agent`) and handling session cookies.
- **CSV Parsing**: Some endpoints return CSV files. Ensure the response content is properly parsed into a pandas DataFrame.
- **Legal Use**: Always ensure compliance with NSE's terms of use when fetching data.

---

## **Disclaimer**
This script is provided as-is and is intended for educational purposes. It may need adjustments based on changes to NSE's API or website structure.
