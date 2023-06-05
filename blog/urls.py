from django.urls import path
from blog.views import BlogMethods

app_name = 'blog'
urlpatterns = [
    path('', BlogMethods.list_blog_posts, name='blog'),
    path('post/<int:id>', BlogMethods.search_post_by_id, name='post'),
    path('add_post', BlogMethods.add_post, name='add_post'),
    path('delete_post/<int:id>', BlogMethods.delete_post_by_id, name='delete_post'),
    path('alter_title/<int:id>', BlogMethods.alter_post_title, name='alter_title'),
    path('alter_content/<int:id>', BlogMethods.alter_post_content, name='alter_content'),

]
