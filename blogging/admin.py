from django.contrib import admin
from blogging.models import Post, Category



class CategoryInline(admin.TabularInline):
    """

    """
    model = Category.posts.through

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """

    """
    list_display = ('title', 'author', 'created_date',
                    'modified_date', 'published_date', 'categories')

    inlines = [
        CategoryInline,
    ]

    def categories(self, posts):
        for post in posts:
            return post.category_name()

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """

    """
    exclude = ('posts',)
