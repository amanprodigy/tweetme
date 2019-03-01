from rest_framework import serializers

from users.serializers import UserDisplaySerializer
from tweets.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True)
    tweet_likes = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            'user',
            'content',
            'tweet_likes'
        ]

    def get_tweet_likes(self, object):
        return 21
