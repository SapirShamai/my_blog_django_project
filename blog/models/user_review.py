from django.db import models


class UsersReviews(models.Model):
    post_id = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
