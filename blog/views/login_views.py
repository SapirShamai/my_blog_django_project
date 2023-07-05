from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from ..forms.login import LoginForm
from ..forms.register_form import RegisterForm
from django.http import HttpResponse


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        users = User.objects.filter(username=request.POST.get('username'))
        for user in users:
            print(user.password)
            print(make_password(request.POST.get('password'), 'G6jRmFd0Dd4fxJsjKnNIPb'))
            print(user.check_password(request.POST.get('password')))
            print(check_password(user.password, request.POST.get('password')))

        # user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            request.session['username'] = user.username
            request.session['user_id'] = user.id
            return redirect('blog:home')

    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


def log_out(request):
    request.session.flush()
    return redirect('blog:home')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = make_password(request.POST.get('password'), 'G6jRmFd0Dd4fxJsjKnNIPb')

            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=password
            )
            if 'first_name' in form.cleaned_data:
                user.first_name = form.cleaned_data['first_name']
            if 'last_name' in form.cleaned_data:
                user.last_name = form.cleaned_data['last_name']

            user.save()

        return redirect('blog:success')
    form = RegisterForm()
    template = 'login/login.html'
    context = {'form': form}
    return render(request, template, context)


def success_register(request):
    return render(request, 'login/success.html')


def test(request):
    users = User.objects.all()

    print(users.values())
    return HttpResponse('hi')

