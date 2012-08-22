from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'src.talks.views.home', name='home'),
    url(r'^votacao/(?P<talk_id>[\d]+)/$', 'src.talks.views.poll_form',
        name='poll_form'),
    url(r'^admin/', include(admin.site.urls)),
)
