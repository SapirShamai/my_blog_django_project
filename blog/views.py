from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogPosts


class BlogMethods:
    @staticmethod
    def list_blog_posts(request):
        posts = BlogPosts.objects.all()
        posts_titles = f"""
        <h1>TITLES:</h1>
        {''.join(["<ol>" + post.title + "</ol>" for post in posts])}
        """
        return HttpResponse(posts_titles)

    @staticmethod
    def search_post_by_id(request, id):
        post = BlogPosts.objects.get(id=id)
        return HttpResponse(f'{post.title},{post.content},{post.created_at}')

    @staticmethod
    def add_post(request):
        title = input('choose your title: ')
        content = input('enter post content: ')
        new_post = BlogPosts.objects.create(title=title, content=content)
        return HttpResponse(f'new post with id {new_post.id} was created successfully')

    @staticmethod
    def delete_post_by_id(request, id):
        post = BlogPosts.objects.filter(id=id).delete()
        return HttpResponse(f'Post with id {id} was successfully deleted!')

    @staticmethod
    def alter_post_title(request, id):
        new_title = input('Please enter the new title: ')
        post = BlogPosts.objects.get(id=id)
        old_title = post.title
        post.title = new_title
        post.save()
        return HttpResponse(f'The post with id {id} and the title "{old_title}" now has a new title: "{post.title}"')

    @staticmethod
    def alter_post_content(request, id):
        new_content = input("Please enter the new content: ")
        post = BlogPosts.objects.get(id=id)
        old_content = post.content
        post.content = new_content
        post.save()
        return HttpResponse(f'The post with id {id} and the content "{old_content}" now has a new content: "{post.content}"')



