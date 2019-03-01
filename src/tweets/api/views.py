from rest_framework import generics

from tweets.models import Tweet
from .serializers import TweetSerializer


class TweetAPIView(generics.ListAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
