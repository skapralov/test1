from django.urls import path

from .views import RequestAPIView, OfferAPIView


urlpatterns = [
    path('request', RequestAPIView.as_view()),
    path('request/<uuid:uuid>', RequestAPIView.as_view()),
    path('offer', OfferAPIView.as_view()),
]
