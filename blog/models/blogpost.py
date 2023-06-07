from django.db import models
from blog.methods.blog_methods import BlogMethods


class BlogPosts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_all_blog_posts(cls):
        """display a list of all the blog posts"""

        posts = BlogPosts.objects.all()
        post_html = BlogMethods.list_blog_posts_html(posts)
        return post_html

    @classmethod
    def get_post_by_id(cls, id):
        """finds the post by the id"""

        try:
            return cls.objects.get(id=id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_post_by_title(cls, title):
        """finds the post by the title"""

        try:
            return cls.objects.get(id=title)
        except cls.DoesNotExist:
            return None

    @classmethod
    def create_post(cls):
        """creating a new post"""

        user_info = BlogMethods.get_post_from_user()
        post = cls.objects.create(title=user_info['title'], content=user_info['content'])
        return post

    def delete_post_by_id(self):
        """deleting the post from db"""

        self.delete()

    def update_post_title(self):
        """update the post title in db"""

        new_title = BlogMethods.get_title()
        self.title = new_title
        self.save()
        return self

    def update_post_content(self):
        """update the post content in db"""

        new_content = BlogMethods.get_content()
        self.content = new_content
        self.save()
        return self

