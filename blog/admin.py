from django.contrib import admin
from .models.blogpost import BlogPosts
from .models.user_review import UsersReviews

# Register your models here.
admin.site.register(BlogPosts)
admin.site.register(UsersReviews)
