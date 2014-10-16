from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.fields import ForeignKey
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.utils.urls import trailing_slash
from tastypie.http import HttpUnauthorized
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.conf.urls import url

from chatapp.models import Message


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        filtering = {'username': ALL, }

    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('login'), name="api_login")
        ]

    def login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])

        data = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/json'))

        username = data.get('username', '')
        password = data.get('password', '')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return self.create_response(request, {
                'success': True
            })
        else:
            return self.create_response(request, {
                'success': False,
                'reason': 'incorrect',
                }, HttpUnauthorized)


class CreateUserResource(ModelResource):
    class Meta:
        allowed_methods = ['post']
        object_class = User
        resource_name = 'create_user'
        authentication = Authentication()
        authorization = Authorization()
        include_resource_uri = False
        fields = ['username']

    def obj_create(self, bundle, request=None, **kwargs):
        username, password = bundle.data['username'], bundle.data['password']
        bundle.obj = User.objects.create_user(username, '', password)
        user = authenticate(username=username, password=password)
        if user:
            login(bundle.request, user)
        return bundle


class MessageResource(ModelResource):
    user = ForeignKey(UserResource, 'user', full=True)

    class Meta:
        queryset = Message.objects.all()
        resource_name = 'message'
        authorization = Authorization()
        filtering = {'user': ALL_WITH_RELATIONS, }
