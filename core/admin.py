from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Station, Train, Ticket, UserProfile

# Register your models
admin.site.register(Station)
admin.site.register(Train)
admin.site.register(Ticket)
admin.site.register(UserProfile)