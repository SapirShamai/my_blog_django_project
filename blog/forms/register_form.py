from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=55)
    password = forms.CharField(max_length=55)
    first_name = forms.CharField(max_length=55, required=False, label='First Name')
    last_name = forms.CharField(max_length=55, required=False, label='Last Name')
    email = forms.EmailField()