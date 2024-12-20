from django.shortcuts import render
from rest_framework.views import APIView

from content.models import Feed


# Create your views here.
class Main(APIView):
    def get(self,request):
        feed_list = Feed.objects.all().order_by('-id')
        for feed in feed_list:
            print(feed.content)
        return render(request,'lilstagram/main.html', context=dict(feeds=feed_list))