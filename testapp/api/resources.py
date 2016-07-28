from tastypie.resources import ModelResource
from testapp.models import TexasDoc
from django.conf import settings
from django.contrib.sites.models import Site
import sys, ast
import socket



class TexasDocResource(ModelResource):
    class Meta:
        queryset = TexasDoc.objects.all()
        allowed_methods = ['get']
        resource_name = 'texasdoc'
        
        
    def dehydrate(self, bundle):
        bundle.data['images'] = settings.MEDIA_URL + bundle.data.get('images')
        return bundle