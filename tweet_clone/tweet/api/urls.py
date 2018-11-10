

from django.urls import path

app_name="api_tweet"


urlpatterns=[
	path('list_tweet/',views.ListTweetAPIView.as_view(),name='listAPIView')
	]