from rest_framework import generics

from tweet.api.serializer import TweetModelSerializer
from tweets.models import Tweet

class ListTweetAPIView(generic.ListAPIView):
	serializer_class=TweetModelSerializer

	def get_queryset(self,*args, **kgargs):
		return Tweet.objects.all();