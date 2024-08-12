#This example uses Python 2.7 and the python-request library. https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '814a01a3-faa4-42aa-91bf-5751a2896f10',
}

session = Session()
session.headers.update(headers)

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
  'id':'1',
  'convert':'USD'
  }

def fetch_bitcoin_latest_quote():

  try:
    response = session.get(url, params=parameters)
  except response.exceptions.RequestException as e:
        # Handle network errors (e.g., connection timeout, connection error)
        print(f"Network Error: {e}")
        # You can retry the request or log the error here
  except KeyError as e:
        # Handle invalid API responses (e.g., missing data)
        print(f"Invalid Response: {e}")
        # You can log the error or skip this data point
  except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected Error: {e}")
        # Log the error and potentially exit
  except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
  if response.status_code == 200:
        data = json.loads(response.text) #data = response.json()
        pprint.pprint(data) #return data['data']['BTC']
  else:
        raise Exception(f"Error fetching data: {response.status_code}")

fetch_bitcoin_latest_quote()