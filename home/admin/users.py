from django.contrib import admin
from django.contrib.auth.models import Group
from home.models import User, Category, Menu, Tag, Article


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'nickname', 'email', 'is_deleted', 'is_active', 'is_admin')
    search_fields = ('username', 'nickname', 'email',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
