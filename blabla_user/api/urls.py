from django.urls import path

from .views import Signup, Record

app_name = 'api'

urlpatterns = [
    path('', Signup.as_view()),
    path('record/', Record.as_view(), name='record'),
]
