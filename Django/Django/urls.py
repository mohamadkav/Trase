from django.conf.urls import patterns, include, url
from django.contrib import admin
from Django import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoTest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^form/$', views.search),
    url(r'^search/$', views.show_search),
)
