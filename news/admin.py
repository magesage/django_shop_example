from django.contrib import admin
from .models import News, NewsCategory


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published', 'title', 'preview', 'created_at', 'updated_at', 'category', 'slug',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content',)
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category',)

class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(NewsCategory, NewsCategoryAdmin)