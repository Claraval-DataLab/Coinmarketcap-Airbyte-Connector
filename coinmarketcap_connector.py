import requests

class CoinMarketCapStream:
    def __init__(self):
        self.url = 'https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    def read_records(self, **kwargs):
        r = requests.get(self.url, headers=self.headers)
        data = r.json()

        for item in data['data']:
            yield item

stream = CoinMarketCapStream()

# To test the stream, you can print the first record
for record in stream.read_records():
    print(record)
