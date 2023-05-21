from django.urls import path

from .views import signup

app_name = 'api'

urlpatterns = [
    path('', signup),
    path('record/')
]
