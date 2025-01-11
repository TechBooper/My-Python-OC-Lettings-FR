from django.contrib import admin

from property_lettings.models import Letting
from property_lettings.models import Address
from accounts.models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
