from django.urls import path

from .views import QuandlAPIView

urlpatterns = [
    path('quandl/<str:ticker>', QuandlAPIView.as_view()),
]
