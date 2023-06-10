from django.db import models


class BlogPosts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_all_blog_posts(cls):
        """display a list of all the blog posts"""

        posts = BlogPosts.objects.all()
        return posts

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
            return cls.objects.get(title=title)
        except cls.DoesNotExist:
            return None

    @classmethod
    def create_post(cls, title, content):
        """creating a new post in db"""

        post = cls.objects.create(title=title, content=content)
        post = BlogPosts.get_post_by_title(title)
        return post

    def delete_post_by_id(self):
        """deleting the post from db"""

        self.delete()

    def update_post_title(self, new_title):
        """update the post title in db"""

        self.title = new_title
        self.save()
        return self

    def update_post_content(self, new_content):
        """update the post content in db"""

        self.content = new_content
        self.save()
        return self

