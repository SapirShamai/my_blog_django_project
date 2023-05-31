from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogPosts


def list_blog_posts(request):
    posts = BlogPosts.objects.all()
    posts_title = []
    for post in posts:
        posts_title.append(post.title)
    return HttpResponse(', '.join(posts_title))


def search_post(request, post_id):
    post = BlogPosts.objects.get(id=post_id)
    return HttpResponse(f'{post.title},{post.content},{post.created_at}')


def add_post(request):
    title = input('choose your title: ')
    content = input('enter post content: ')
    new_post = BlogPosts.objects.create(title=title, content=content)
    return HttpResponse(f'new post with id {new_post.id} was created successfully')