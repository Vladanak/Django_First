from . import views
from django.conf.urls import url


urlpatterns = [
    url('^$', views.template, name = 'Template'),
    url('^contact/$', views.contact, name = 'Template'),
]