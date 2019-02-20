from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Tweet

User = get_user_model()


class TweetModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='amangamer',
            email='amanprodigy@gmail.com',
            password='123')
        self.tweet = Tweet.objects.create(
            content='Hello world',
            user=self.user
        )

    def test_tweet_item(self):
        self.assertTrue(self.tweet.content, 'Hello world')
        self.assertTrue(self.tweet.id, 1)
        absolute_url = reverse('tweets:detail', kwargs={'pk': 1})
        self.assertTrue(self.tweet.get_absolute_url(), absolute_url)
