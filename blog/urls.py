from django.urls import path
from .views.blog_views import *
from .views.login_views import *
from .views.user_review_views import *

app_name = 'blog'

urlpatterns = [
    path('', list_blog_posts, name='home'),
    path('post/<int:id>', display_post_by_id, name='post'),
    path('add_post', CreateBlogPost.as_view(), name='add_post'),
    path('delete_post/<int:id>', delete_post, name='delete_post'),
    path('edit/<int:id>', EditPost.as_view(), name='edit_post'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('review/<int:post_id>', add_new_review, name='review'),
    path('register/', register, name='register'),
    path('success/', success_register, name='success'),



]
