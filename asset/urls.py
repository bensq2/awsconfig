from django.conf.urls import url
from . import views
app_name = 'asset'
urlpatterns = [
    url(r'^$', views.index, name='index'),
   # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/$',views.AssetCreateView.as_view(),name='add'),
    url(r'^(?P<pk>[0-9])+del/$', views.AssetDeleteView.as_view(), name='del'),
    url(r'^(?P<pk>[0-9])+update/$', views.AssetUpdateView.as_view() , name='update'),
    url(r'^(?P<pk>[0-9])+awsupdate/$', views.AssetUpdateByAws , name='awsupdate'),
    url(r'^grouplist/$',views.GroupView.as_view() ,name='grouplist'),
    url(r'^groupadd/$',views.GroupCreateView.as_view(),name='groupadd'),
    url(r'^(?P<pk>[0-9])+del/$', views.GroupDeleteView.as_view(), name='groupdel'),
    url(r'^(?P<pk>[0-9])+groupupdate/$', views.GroupUpdateView.as_view() , name='groupupdate'),
]
