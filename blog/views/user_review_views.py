from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from ..models.user_review import UsersReviews
from ..forms.review_form import ReviewForm


def list_all_reviews_by_post_id(request, post_id):
    reviews = UsersReviews.list_reviews_by_post_id(post_id=post_id)
    context = {'reviews': reviews}
    return TemplateResponse(request, 'blog_posts/post_details.html', context)


def add_new_review(request, post_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            UsersReviews.objects.create(post_id_id=post_id, content=content)
            return redirect('blog:home')
    else:
        initial = {}
        if request.session.get('username'):
            initial['username'] = request.session['username']
        form = ReviewForm(initial=initial)

    context = {'form': form}
    template = 'reviews/add_review.html'
    return render(request, template, context)
