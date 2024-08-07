from django.contrib import admin
from .models import News, NewsImage

class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1
    verbose_name = "Изображение Спецпроекта"
    verbose_name_plural = "Изображения Спецпроекта"

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'category', 'views', 'publication_date')
    list_filter = ('language', 'category', 'publication_date')
    search_fields = ('title', 'content', 'category')
    inlines = [NewsImageInline]