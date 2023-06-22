from django.contrib import admin

from .models import Follow, User


class UserAdmin(admin.ModelAdmin):
    """Админка пользователя."""
    list_display = (
        'username', 'first_name', 'last_name', 'email',
    )
    search_fields = ('username',)
    list_filter = ('username', 'email')
    ordering = ('username',)
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    """Админка подписчика."""
    list_display = (
        'username', 'author'
    )
    search_fields = ('username',)
    list_filter = ('username', 'author')
    ordering = ('username',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
