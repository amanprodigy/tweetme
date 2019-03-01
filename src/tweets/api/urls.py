from django.urls import path
from .views import TweetAPIView

app_name = 'api_tweets'

urlpatterns = [
    path('', TweetAPIView.as_view(), name='tweets'),  # /api/tweets
]
