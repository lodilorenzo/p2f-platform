from django.conf.urls import patterns, url

from core import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^project/(?P<prj_id>\d+)/$', views.project, name='project'),
)