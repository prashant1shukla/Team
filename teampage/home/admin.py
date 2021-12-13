from django.contrib import admin
from django.contrib.auth.models import Group
from home.models import Details

# Register your models here.
admin.site.register(Details)


admin.site.site_header = 'Admin RECursion NIT Durgapur'

