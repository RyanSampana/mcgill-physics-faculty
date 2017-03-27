from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index), # '^$' so it doesn't match all strings
]