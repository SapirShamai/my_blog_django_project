from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = [
    path('', list_blog_posts, name='blog'),
    path('post/<int:id>', display_post_by_id, name='post'),
    path('add_post', add_post, name='add_post'),
    path('delete_post/<int:id>', delete_blog_post_by_id, name='delete_post'),
    path('alter_title/<int:id>', alter_post_title, name='alter_title'),
    path('alter_content/<int:id>', alter_post_content, name='alter_content'),

]
