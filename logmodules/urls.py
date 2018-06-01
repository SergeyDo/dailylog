from django.conf.urls import url
from django.contrib import admin 
from django.contrib.auth import views as auth_views
from . import views

app_name = 'logmodules'

urlpatterns = [
        url(r'^logina/$', 
            auth_views.login, 
            {'template_name': 'logmodules/login.html'}, 
            name='login'),
        url(r'^logout/$', 
            auth_views.logout, 
            {'template_name': 'logmodules/logout.html'}, 
            name='logout'),

#url(r'accounts/login', auth_views.login,  {'template_name': 'logmodules/login.html'}),
#            url('^accounts/', admin.site.urls),



#url(r'^log/(?P<pk>\d+)/$', views.IndexView.as_view(), name='list'),
url(r'^log/(?P<pk>\d+)/$', views.log_list, name='list'),
url(r'^log/(?P<pk>\d+)/$', views.log_detail, name='detail'),
url(r'^$', views.IndexView.as_view(), name='list'),
        url(r'^log/entry/$', views.LogEntry.as_view(), name='entry'),
        url(r'^log/(?P<pk>[0-9]+)/$', views.LogUpdate.as_view(), name='update'),
        url(r'^log/(?P<pk>[0-9]+)/delete$', views.LogDelete.as_view(), name='delete'),
]



