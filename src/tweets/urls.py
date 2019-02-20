from django.urls import path
from django.views.generic.base import RedirectView

from .views import (TweetDetail,
                    TweetCreate,
                    TweetUpdate,
                    TweetDelete)

app_name = 'tweets'

urlpatterns = [
    path('', RedirectView.as_view(url="/")),
    path('<int:pk>/', TweetDetail.as_view(), name='detail'),
    path('create/', TweetCreate.as_view(), name='create'),
    path('<int:pk>/edit/', TweetUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', TweetDelete.as_view(), name='delete'),
]
