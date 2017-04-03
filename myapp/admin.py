from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Person)
admin.site.register(models.Skills)
admin.site.register(models.Talents)

def __str__(self):
    return '{} - {}'.format(self.name, self.age)