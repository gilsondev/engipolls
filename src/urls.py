from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$', 'src.talks.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
