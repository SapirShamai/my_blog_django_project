from django.db import models
from django.contrib.auth.models import User


class UsersReviews(models.Model):
    post_id = models.ForeignKey('BlogPosts', on_delete=models.CASCADE, related_name='usersreviews')
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def list_reviews_by_post_id(cls, post_id):
        reviews = UsersReviews.objects.filter(post_id=post_id)
        print(reviews)
        return reviews
