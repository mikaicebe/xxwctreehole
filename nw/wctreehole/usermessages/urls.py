from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all$', views.getAllMessages, name='all'),
    url(r'^message$', views.createMessage, name='message'),
    url(r'^comment/(?P<message_id>[0-9]+)$', views.createComment,name='comment')
]