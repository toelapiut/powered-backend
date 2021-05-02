from django.urls import path

from .views import QuandlAPIView

urlpatterns = [
    path('quandl/markets', QuandlAPIView.as_view()),
    path('quandl/stocks/<str:ticker>', QuandlAPIView.as_view()),
]
