from django.db import models
from django.contrib.postgres.fields import ArrayField
import ast


'''
class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
'''
class TexasDoc(models.Model):
    number = models.IntegerField()
    volume = models.IntegerField()
    page = models.IntegerField()
    #images = ListField()
    images = models.CharField(max_length=200, blank=True)
    
    '''
    def __unicode__(self):
        return "%s" % (self.images) 
    '''
    
    
    class Meta:
        ordering = ['id']