"""Define [wzorce adresów] URL for learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # main page
    path('', views.index, name='index'),
    # all the topcis
    path('topics/', views.topics, name='topics'),
]