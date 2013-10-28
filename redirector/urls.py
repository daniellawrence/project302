from django.conf.urls import patterns, include, url
import redirector

urlpatterns = patterns('',
                       url(r'^miss/(?P<source_name>.*)$', 'redirector.views.show_miss'),
                       url(r'^redirector/(?P<source_name>.*)$', 'redirector.views.named_redirect'),
                       url(r'^r/(?P<source_name>.*)$', 'redirector.views.named_redirect'),
                       url(r'^r/', 'redirector.views.index'),
)
