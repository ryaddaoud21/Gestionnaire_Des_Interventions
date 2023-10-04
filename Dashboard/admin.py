from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Intervention)
admin.site.register(Event)
admin.site.register(UserProfile)
admin.site.register(Client)
admin.site.register(Notification)
admin.site.register(Reclamation)

