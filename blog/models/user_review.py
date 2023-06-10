from django.db import models
# from django.contrib.auth import get_user_model
#
# User = get_user_model()


class UsersReviews(models.Model):
    post_id = models.ForeignKey('BlogPosts', on_delete=models.CASCADE, related_name='usersreviews')
    content = models.TextField()
    # user_id = models.ForeignKey('User', on_delete=models.CASCADE)  ???
    created_at = models.DateTimeField(auto_now_add=True)
