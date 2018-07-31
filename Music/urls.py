from django.conf.urls import url
from . import views

app_name = 'Music'

urlpatterns = [
    # Music
    url(r'^$', views.HomView.as_view(), name='hom'),
    # url(r'^place1/', views.place1),
    # /Music/album_id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /Music/album_id/favorite
    # url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
]
