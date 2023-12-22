
from django.contrib import admin
from .models import (
    Post, Category, PostCategory,
)
class CategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1
class PostAdmin(admin.ModelAdmin):
    inlines = (CategoryInline, )
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('date_create', 'title', 'content', 'post_type')
    list_filter = ('date_create', 'title', 'content', 'post_type')
    #search_fields = ('date_create', 'title', 'content', 'post_type')

admin.site.register(Post, PostAdmin, )
admin.site.register(PostCategory,)
admin.site.register(Category,)
admin.site.register(Post.categories.through)
#admin.site.register(Author)
#admin.site.register(Comment)


