

import requests

class BSE():
    def __init__(self, timeout=10):
        self.base_url = 'https://www.bseindia.com'
        self.session = requests.sessions.Session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
            "Origin": "https://www.bseindia.com",
            "Referer": "https://www.bseindia.com/"
        }
        self.timeout = timeout
        self.session.get(self.base_url, timeout=timeout)

    def getBSE500Data(self, from_date, to_date):
        try:
            param={
                    "period": "D",
                    "index": "BSE500",
                    "fmdt": from_date.strftime('%d/%m/%Y'),  # From Date 03/12/2024
                    "todt": to_date.strftime('%d/%m/%Y')   # To Date 05/12/2024
                }
            url = "https://api.bseindia.com/BseIndiaAPI/api/IndexArchDaily/w"
            # Send request with parameters for date range and index
            r = self.session.get(
                url,
                params=param,
                timeout=self.timeout
            )
            
            if r.status_code == 200:
                data = r.json()  # Parse the response as JSON
                return data
            else:
                print(f"Failed to fetch data. Status Code: {r.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


if __name__ == "__main__":
    from datetime import date
    bse = BSE()
    bse500_data = bse.getBSE500Data(date(2024,12,1), date(2024,12,5))
    
    if bse500_data:
        print("BSE 500 Data:")
        print(bse500_data)
    else:
        print("Failed to fetch BSE 500 data.")


