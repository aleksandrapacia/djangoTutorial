"""Define adresses' URL pattern for learning_logs"""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # main page
    path('', views.index, name='index'),
    # all the topcis
    # then it goes to a function topics() defined in views.py
    path('topics/(<int:topic_id>)', views.topic, name = 'topic'),
    path('topics/', views.topics, name='topics'),
    path('new_topic/', views.new_topic, name='new_topic'),
]