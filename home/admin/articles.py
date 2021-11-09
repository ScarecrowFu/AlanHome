from django.contrib import admin
from django.db import models
from martor.widgets import AdminMartorWidget
from home.models import User, Category, Menu, Tag, Article


class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'sort', 'created_time',)
    search_fields = ('name',)

    def get_changeform_initial_data(self, request):
        get_data = super(MenuAdmin, self).get_changeform_initial_data(request)
        get_data['creator'] = request.user.pk
        return get_data


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('menu', 'name', 'creator', 'sort', 'created_time',)
    search_fields = ('name',)

    def get_changeform_initial_data(self, request):
        get_data = super(CategoryAdmin, self).get_changeform_initial_data(request)
        get_data['creator'] = request.user.pk
        return get_data


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'sort', 'created_time',)
    search_fields = ('name',)

    def get_changeform_initial_data(self, request):
        get_data = super(TagAdmin, self).get_changeform_initial_data(request)
        get_data['creator'] = request.user.pk
        return get_data


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'creator', 'sort', 'created_time', 'status', 'is_deleted', 'view_count', 'like_count')
    search_fields = ('title',)

    def get_changeform_initial_data(self, request):
        get_data = super(ArticleAdmin, self).get_changeform_initial_data(request)
        get_data['creator'] = request.user.pk
        return get_data


admin.site.register(Menu, MenuAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)