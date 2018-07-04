from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^$', views.index, name='home'),
    url(r'^additem/$', views.addItem, name='addItem'),
    url(r'^item/(?P<item_id>\d+)$', views.item, name='item'),
    url(r'^wish/(?P<wish_id>\d+)$', views.addWish, name='addWish'),
    url(r'^rwish/(?P<wish_id>\d+)$', views.removeWish, name='removeWish'),
    url(r'^delete(?P<item_id>\d+)$', views.delete, name='delete')
]