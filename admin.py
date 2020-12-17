from django.contrib import admin

# Register your models here.
from .models import user,project,rules
admin.site.register(user)
admin.site.register(project)
admin.site.register(rules)

