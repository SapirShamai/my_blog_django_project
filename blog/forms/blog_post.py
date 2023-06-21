from django import forms


class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=60,
                            required=True)

    content = forms.CharField(max_length=500,
                              initial='Write your post here',
                              widget=forms.Textarea(attrs={'rows': 8, 'cols': 70}))
