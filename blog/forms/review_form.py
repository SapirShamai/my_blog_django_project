from django import forms


class ReviewForm(forms.Form):

    username = forms.CharField(max_length=55, label='Your Name')
    content = forms.CharField(max_length=400,
                              label='Your Comment',
                              widget=forms.Textarea(attrs={'rows': 8, 'cols': 40}))
