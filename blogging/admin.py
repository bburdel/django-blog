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

    # def categories(self, title):
    #     p = Category.object.posts.all()
    #     category_dictionary = p.__dict__
    #     print(category_dictionary)
    #     for key, value in category_dictionary.items():
    #         if title == Post.title:
    #             cat_name = value
    #     assert isinstance(cat_name, object)
    #     return cat_name


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """

    """
    exclude = ('posts',)
