from django.contrib import admin
from .models import *
from django.db.models import QuerySet
from .models import *

# from guardian.admin import *
#
#
# class PostAdmin(GuardedModelAdmin):
#     list_display = ["title", ]


#


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['id']


class BooksAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'id_book']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['subcategory1', 'subcategory2']


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone_number']


admin.site.register(BooksModel, BooksAdmin)
# admin.site.register(BooksModel, PostAdmin)
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ReviewsModel, ReviewsAdmin)
admin.site.register(User, UserAdmin)
