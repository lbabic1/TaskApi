from django.conf.urls import url
from PlayersApp import views


urlpatterns = [
    url(r'^player$', views.PlayerApi),
    url(r'^player/([0-9]+)$', views.PlayerApi)
]