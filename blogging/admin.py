from django.contrib import admin
from blogging.models import Post, Category


# TODO Create a customized ModelAdmin class for the Post and Category models


class CategoryInline(admin.TabularInline):
    model = Category.posts.through

    def __str__(self):
        return self.model

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'author', 'created_date',
                    'modified_date', 'published_date', 'categories')

    # def categories(self):
    #     return Category.posts.through

    inlines = [
        CategoryInline,
    ]


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]
    exclude = ('posts',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
