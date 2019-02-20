from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'first_name',
                    'last_name', 'avatar', 'date_joined']
    list_filter = ['date_joined', 'is_active', 'first_name', 'last_name']
