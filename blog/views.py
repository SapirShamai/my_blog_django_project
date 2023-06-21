from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models.blogpost import BlogPosts
from .forms import BlogPostForm


def list_blog_posts(request):
    """display a list of all the posts in the blog"""

    posts = BlogPosts.get_all_blog_posts()
    context = {'posts': posts}
    return TemplateResponse(request, 'blog_posts/list_all_posts.html', context)


def display_post_by_id(request, id):
    """display post details if exists"""

    post = BlogPosts.get_post_by_id(id)
    if post is None:
        return redirect("/blog")
    context = {'post': post}
    return TemplateResponse(request, 'blog_posts/post_details.html', context)


class CreateBlogPost(FormView):
    form_class = BlogPostForm
    template_name = 'blog_posts/add_post.html'

    def get_success_url(self):
        return reverse_lazy('blog:home')

    def post(self, request, *args, **kwargs):
        return super().post(self, request, *args, **kwargs)

    def form_valid(self, form):
        content = form.cleaned_data.get('content')
        if len(content) < 10:
            form.add_error('content', 'Your post is too short, we require at least 10 characters')
            return super().form_invalid(form)
        BlogPosts.objects.create(**form.cleaned_data)
        return super().form_valid(form)


class EditPost(FormView):
    form_class = BlogPostForm
    template_name = 'blog_posts/add_post.html'

    def get_success_url(self):
        return reverse_lazy('blog:home')

    def get(self, request, *args, **kwargs):
        post_id = self.kwargs.get('id')
        post = BlogPosts.objects.filter(id=post_id)
        post_data = post.values()[0]
        unbound_form = self.form_class(post_data)
        context = {'form': unbound_form}
        return TemplateResponse(request, self.template_name, context)

    def form_valid(self, form):
        content = form.cleaned_data.get('content')
        if len(content) < 10:
            form.add_error('content', 'Your post is too short, we require at least 10 characters')
            return super().form_invalid(form)
        post_id = self.kwargs.get('id')
        post = BlogPosts.objects.filter(id=post_id)
        post.update(**form.cleaned_data)
        return super().form_valid(form)


def delete_post(request, **kwargs):
    """deleting the post if exists"""

    post_id = kwargs.get('id')
    post = BlogPosts.get_post_by_id(post_id)
    if post is None:
        return redirect('blog:home')
    post.delete()
    return redirect('blog:home')

