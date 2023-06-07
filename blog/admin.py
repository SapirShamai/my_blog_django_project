from django.contrib import admin
from blog.models.blogpost import BlogPosts
from blog.models.user_review import UsersReviews

# Register your models here.
admin.site.register(BlogPosts)
admin.site.register(UsersReviews)
