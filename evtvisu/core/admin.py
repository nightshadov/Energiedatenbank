from django.contrib import admin
from .models import ExperimentLog, AlmemoLog, EnYear

# Register your models here.

admin.site.register(ExperimentLog)
admin.site.register(AlmemoLog)
admin.site.register(EnYear)
