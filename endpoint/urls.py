from django.urls import path

from .views import QuandlAPIView

urlpatterns = [
    path('quandl/market', QuandlAPIView.as_view()),
    path('quandl/stock/<str:ticker>', QuandlAPIView.as_view()),
]
