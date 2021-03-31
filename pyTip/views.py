from django.shortcuts import render
from .models import PyTip
import tweepy  # https://github.com/tweepy/tweepy
from tweepy.auth import OAuthHandler
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.


def tweet_list(request):
    if 'q' in request.GET:
        q = request.GET['q']
        tweets = PyTip.objects.filter(
            tweet_text__icontains=q).order_by('-timestamp')
        page = request.GET.get('page', 1)
        paginator = Paginator(tweets, 10)
    else:
        tweets = PyTip.objects.order_by('-timestamp')
        page = request.GET.get('page', 1)
        paginator = Paginator(tweets, 10)
    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)

    index = tweets.number - 1

    max_page_num = len(paginator.page_range)
    start_page_num = index - 3 if index >= 3 else 0
    end_page_num = index + 3 if index <= max_page_num - 3 else max_page_num
    page_range = list(paginator.page_range)[start_page_num:end_page_num]
    return render(request, 'pyTip/home.html', {'tweets': tweets, 'page_range': page_range})
