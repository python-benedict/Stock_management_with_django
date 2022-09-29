from django.contrib import admin
from .models import *
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']    
    search_fields = ['title', 'content']

admin.site.register(Articles, ArticleAdmin)
