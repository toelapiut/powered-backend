import requests
from decouple import config
from requests.auth import HTTPBasicAuth

base_url = config('BASE_URL')


def header_config():
	api_key = config('API_KEY')
	headers = {"Accept": "application/json"}
	auth = HTTPBasicAuth('api_key', '{}'.format(api_key))
	return api_key, headers, auth


def stock_url(ticker, start_date, end_date):
	if start_date is not None and end_date is not None:
		url = '{}/datasets/WIKI/{}.json?start_date={}&end_date={}&order=asc&column_index=4&collapse=quarterly&' \
			'transformation=rdiff'.format(base_url, ticker, start_date, end_date)
		return url
	elif start_date is None or end_date is None:
		url = '{}/datasets/WIKI/{}.json?&order=asc&column_index=4&collapse=quarterly&transformation=rdiff'.format(
			base_url, ticker)
		return url


def market_url():
	url = '{}/datatables/ZACKS/CP?&'.format(base_url)
	return url


def stock_endpoint(ticker, start_date, end_date):
	url = stock_url(ticker, start_date, end_date)
	api_key, headers, auth = header_config()
	res = requests.get(url=url, headers=headers, auth=auth)
	return res.json()


def market_endpoint():
	url = market_url()
	api_key, headers, auth = header_config()
	res = requests.get(url=url+'api_key={}'.format(api_key), headers=headers)
	return res.json()
