from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models.blogpost import BlogPosts
from blog.methods.blog_methods import BlogMethods


def list_blog_posts(request):
    """display a list of all the posts in the blog"""

    posts = BlogPosts.get_all_blog_posts()
    html_posts_title = BlogMethods.list_blog_posts_html(posts)
    return HttpResponse(html_posts_title)


def display_post_by_id(request, id):
    """display post details if exists"""

    post = BlogPosts.get_post_by_id(id)
    if post is None:
        return redirect("/blog")
    return HttpResponse(f'{post.title},{post.content},{post.created_at}')


def add_post(request):
    """adding a new post if valid"""
    user_info = BlogMethods.get_post_from_user()
    print(user_info)
    post = BlogPosts.create_post(user_info['title'], user_info['content'])
    if not post:
        return "Post isn't valid"
    return HttpResponse(f'new post with title {post.title} id {post.id} was created successfully')


def delete_blog_post_by_id(request, id):
    """deleting the post if exists"""

    post = BlogPosts.get_post_by_id(id)
    print(post)
    if post is None:
        return redirect('/blog')
    post.delete()
    return HttpResponse(f'Post with id {id} was successfully deleted!')


def alter_post_title(request, id):
    """altering the post title"""

    post = BlogPosts.get_post_by_id(id)
    if post is None:
        return redirect('/blog')
    new_title = BlogMethods.get_title()
    post = post.update_post_title(new_title)
    return HttpResponse(f'The post with id {id} now has a new title: "{new_title}"')


def alter_post_content(request, id):
    """altering the post content"""

    post = BlogPosts.get_post_by_id(id)
    if post is None:
        return redirect('/blog')
    new_content = BlogMethods.get_content()
    post = post.update_post_content(new_content)
    print(post)
    return HttpResponse(f'The post with id {id} has a new content: "{new_content}"')

