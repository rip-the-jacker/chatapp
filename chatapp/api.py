from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.fields import ForeignKey
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from django.contrib.auth.models import User

from chatapp.models import Message


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        filtering = {'username': ALL, }


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
        return bundle


class MessageResource(ModelResource):
    user = ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Message.objects.all()
        resource_name = 'message'
        authorization = Authorization()
        filtering = {'user': ALL_WITH_RELATIONS, }
