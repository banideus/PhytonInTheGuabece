from django.shortcuts import render
from django.views import generic
from .models import Tweet
# Create your views here.

def index(request):
	return render(request, "tweet/index.html",{})

class List_Tweets(generic.ListView):
 	template_name = "tweet/list_tweets.html"
 	model = Tweet

def list_tweets(request):
	queryset = Tweet.objects.all()
	context = {
		"tweets": Tweet.objects.all()
	}
	return render(request,"tweet/list_tweets.html",context)

def detail_tweet(request, id=1):
	queryset = Tweet.objects.get(id=id)
	context = {
		"tweet_object": queryset
	}
	return render(request, "tweet/detail.html", context)

