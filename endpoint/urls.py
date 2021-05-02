from django.urls import path

from .views import QuandlAPIView

urlpatterns = [
    path('<str:ticker>', QuandlAPIView.as_view()),
]
