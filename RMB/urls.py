from django.conf.urls import patterns, url
from RMB import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^like_image/$', views.like_image, name='like_image'),
    url(r'^dislike_image/$', views.dislike_image, name='dislike_image'),
	url(r'^comment_image/$', views.comment_image, name='comment_image'),
	url(r'^worst_image/$', views.worst_image, name='worst_image'),
	url(r'^profile/$', views.upload_images, name='upload_images'),
    url(r'^newest/$', views.newest, name='newest'),
    url(r'^worse/$', views.worse, name='worse'),
    url(r'^noob/$', views.noob, name='noob'),
    url(r'^full/$', views.full, name='full'),
    url(r'^half/$', views.half, name='half'),
    url(r'^moustache/$', views.moustache, name='moustache'),
    )+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	