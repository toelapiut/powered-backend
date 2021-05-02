from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .request import quandl_endpoint


class QuandlAPIView(APIView):
	def post(self, request, ticker):
		start_date = request.data.get('start', None)
		end_date = request.data.get('end', None)
		response = quandl_endpoint(ticker=ticker, start_date=start_date, end_date=end_date)
		
		return Response(data=response, status=status.HTTP_200_OK)
