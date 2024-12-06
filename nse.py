import requests
import pandas as pd
from datetime import datetime
from io import BytesIO
class NSE():
    def __init__(self, timeout=10):
        self.base_url = 'https://www.nseindia.com'
        self.session = requests.sessions.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en-US,en;q=0.9"
        }
        self.timeout = timeout
        self.session.get(self.base_url, timeout=timeout)
        #self.cookies = []
    
    def getHistoricalData(self, symbol, series, from_date, to_date):
        try:
            url = "/api/historical/cm/equity?symbol={0}&series=[%22{1}%22]&from={2}&to={3}&csv=true".format(symbol.replace('&', '%26'), series, from_date.strftime('%d-%m-%Y'), to_date.strftime('%d-%m-%Y'))
            r = self.session.get(self.base_url + url, timeout=self.timeout)
            df = pd.read_csv(BytesIO(r.content), sep=',', thousands=',')
            return df
        except:
            return None

    def getmarketCap(self):
        try:
            url = "/api/quote-equity?symbol=ONGC&section=trade_info"
            r = self.session.get(self.base_url + url, timeout=self.timeout)
            if r.status_code == 200:
                data = r.json()  # Parse the response as JSON
                trade_info = data.get("marketDeptOrderBook").get("tradeInfo")  # Extract the 'tradeInfo' section
                return trade_info
            else:
                print(f"Failed to fetch data. Status Code: {r.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
    def getNifty50HistoricalData(self,from_date, to_date):
            try:
                url = "/api/historical/indicesHistory?indexType=NIFTY%2050&from={0}&to={1}".format(from_date.strftime('%d-%m-%Y'), to_date.strftime('%d-%m-%Y'))
                r = self.session.get(self.base_url + url, timeout=self.timeout)
                if r.status_code == 200:
                    data = r.json()  # Parse the response as JSON
                    trade_info = data.get('data').get("indexCloseOnlineRecords")  # Extract the 'tradeInfo' section
                    return trade_info
                else:
                    print(f"Failed to fetch data. Status Code: {r.status_code}")
                    return None
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                return None

    


if __name__ == '__main__':
    from datetime import date
    nse = NSE()
    # df = nse.getHistoricalData('ONGC', 'EQ', date(2024,12,4), date(2024,12,5))
    # print(df)
    # print("*************************")
    # df = nse.getmarketCap()
    # print(df)
    df= nse.getNifty50HistoricalData(date(2024,12,1), date(2024,12,5))
    print(df)
#    #https://www.nseindia.com
