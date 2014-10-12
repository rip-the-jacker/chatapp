from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
admin.autodiscover()

from chatapp.api import MessageResource, UserResource, CreateUserResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(CreateUserResource())
v1_api.register(MessageResource())

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'chatapp.views.login_user', name='login'),
    url(r'^login$', 'chatapp.views.login_user', name='login'),
    url(r'^signup$', 'chatapp.views.signup', name='signup'),
    url(r'^chat_view$', 'chatapp.views.chat_view', name='chat-view'),
    url(r'^new_message$', 'chatapp.views.new_message'),
    url(r'^api/', include(v1_api.urls)),
)
