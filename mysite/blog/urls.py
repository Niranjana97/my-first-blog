from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Home.as_view(), name='post_list'),
    url(r'^post/', views.List.as_view(), name='post'),
    url(r'^new/(?P<pk>[0-9]+)/$', views.Detailed.as_view(), name='det'),
    url(r'^user/', views.List2.as_view(), name='user'),
    url(r'^detail/(?P<pk1>[0-9]+)/$', views.Detail2.as_view(), name='detail'),
    url(r'^del/(?P<pk2>[0]+)/$', views.Delete.as_view(), name='del'),

]
