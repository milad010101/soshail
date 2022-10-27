from django.contrib import admin
from .models import Relaship, Profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile


class ExtendUserAdmin(UserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)

admin.site.register(User, ExtendUserAdmin)
admin.site.register(Relaship)
