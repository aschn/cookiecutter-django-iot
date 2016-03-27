from django.contrib import admin
from {{ cookiecutter.repo_name }}.apps.observations.models import Attribute, PowerStatus


class AttributeAdmin(admin.ModelAdmin):
    list_display = ['valid_at', 'device', 'value', 'units']


class PowerStatusAdmin(admin.ModelAdmin):
    list_display = ['valid_at', 'device', 'is_on']


admin.site.register(Attribute, AttributeAdmin)
admin.site.register(PowerStatus, PowerStatusAdmin)
