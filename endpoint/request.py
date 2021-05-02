import requests
from decouple import config
from requests.auth import HTTPBasicAuth


def create_endpoint(ticker, start_date, end_date):
	if start_date is not None and end_date is not None:
		url = 'https://www.quandl.com/api/v3/datasets/WIKI/{}.json?start_date={}&end_date={}&order=asc&' \
			'column_index=4&collapse=quarterly&transformation=rdiff'.format(ticker, start_date, end_date)
		return url
	elif start_date is None or end_date is None:
		url = 'https://www.quandl.com/api/v3/datasets/WIKI/{}.json?&order=asc&column_index=4&collapse=quarterly' \
			'&transformation=rdiff'.format(ticker)
		return url


def quandl_endpoint(ticker, start_date, end_date):
	url = create_endpoint(ticker, start_date, end_date)
	api_key = config('API_KEY')
	headers = {"Accept": "application/json"}
	auth = HTTPBasicAuth('api_key', '{}'.format(api_key))
	res = requests.get(url=url, headers=headers, auth=auth)
	return res.json()
