from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', list_blog_posts, name='home'),
    path('post/<int:id>', display_post_by_id, name='post'),
    path('add_post', CreateBlogPost.as_view(), name='add_post'),
    path('delete_post/<int:id>', delete_post, name='delete_post'),
    path('edit/<int:id>', EditPost.as_view(), name='edit_post'),


]
