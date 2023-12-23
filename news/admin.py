
from django.contrib import admin
from .models import (
    Post, Category,
)

class PostAdmin(admin.ModelAdmin):
    def category(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('date_create', 'title', 'content', 'post_type', 'category')
    #list_filter = ('date_create', 'title', 'content', 'post_type')
    search_fields = ('date_create', 'title', 'content', 'post_type')



admin.site.register(Post, PostAdmin, )
admin.site.register(Category, )
#admin.site.register(Post.categories.through)



