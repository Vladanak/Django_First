from django.conf.urls import url
from django.urls import path
from django.views.generic import ListView
from django.views.generic import DetailView
from news.models import Articles


urlpatterns = [
    url('^$', ListView.as_view
    (queryset=Articles.objects.all().order_by("-date")[:10], template_name="news/posts.html")),
    path('<int:pk>/', DetailView.as_view(model= Articles, template_name="news/post.html"))
]