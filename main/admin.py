from django.contrib import admin
from main.models import Post, Category

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title', )}

admin.site.register(Post)