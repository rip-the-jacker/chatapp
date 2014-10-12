from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'chatapp.views.login_user', name='login'),
    url(r'^login$', 'chatapp.views.login_user', name='login'),
    url(r'^signup$', 'chatapp.views.signup', name='signup'),
    url(r'^chat_view$', 'chatapp.views.chat_view', name='chat-view'),
    url(r'^new_message$', 'chatapp.views.new_message'),
)
