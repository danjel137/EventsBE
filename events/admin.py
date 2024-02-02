from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from events.models import Photo, Account


class CustomUserInLine(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'


class CustomizedUserAdmin(UserAdmin):
    inlines = (CustomUserInLine,)


admin.site.unregister(User)
admin.site.register(Photo)
admin.site.register(User,CustomizedUserAdmin)
