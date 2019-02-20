import datetime

from django.utils import timezone
from django.db.models import Q, F
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from core.mixins import FormUserNeededMixin, OwnerAllowedMixin

from .models import Tweet
from .forms import TweetForm


class TweetList(ListView):
    template_name = 'tweets/list_view.html'
    context_object_name = 'tweets'

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all()
        print(self.request.GET)
        search_query = self.request.GET.get('search', None)
        if search_query is not None:
            qs = qs.filter(
                Q(content__icontains=search_query) |
                Q(user__username__icontains=search_query) &
                Q(created_at__gte=timezone.now() - datetime.timedelta(days=1))
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(TweetList, self).get_context_data(*args, **kwargs)
        context['tweet_form'] = TweetForm
        context['action_url'] = reverse_lazy('tweets:create')
        # context['additional'] = 'hello world'
        return context


class TweetDetail(DetailView):
    queryset = Tweet.objects.all()
    template_name = 'tweets/detail_view.html'
    context_object_name = 'tweet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['additional'] = 'hello world'
        return context


class TweetCreate(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = TweetForm
    template_name = 'tweets/create_view.html'
    # success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_url'] = reverse_lazy('tweets:create')
        return context


class TweetUpdate(LoginRequiredMixin, OwnerAllowedMixin, UpdateView):
    form_class = TweetForm
    model = Tweet
    template_name = 'tweets/update_view.html'
    # success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_url'] = reverse_lazy('tweets:create')
        return context


class TweetDelete(LoginRequiredMixin, OwnerAllowedMixin, DeleteView):
    model = Tweet
    success_url = reverse_lazy('home')
    template_name_suffix = '_delete_confirm'


# Deprecated
@login_required
def create_tweet(request):
    tweet_form = TweetForm(data=request.POST or None)
    if tweet_form.is_valid():
        tweet = tweet_form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        return redirect(reverse('home'))
    return render(request,
                  'tweets/create_view.html',
                  {'form': tweet_form})


# Deprecated
def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        'tweets': queryset.all()
    }
    return render(request, "tweets/list_view.html", context)


# Deprecated
def tweet_detail_view(request, pk):
    obj = Tweet.objects.get(pk=pk)
    context = {
        'object': obj
    }
    return render(request, "tweets/detail_view.html", context)
