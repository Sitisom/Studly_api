from django.contrib import admin

# Register your models here.
from core.models import User
from gettext import gettext as _


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'first_name', 'last_name', 'email', 'avatar', 'role')}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active')}),
        (_('Dates'), {'fields': ('last_login', 'date_joined')})
    )
    exclude = ('user_permissions', 'groups', )
