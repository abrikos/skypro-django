from django import forms

from .models import Post

class BlogPostForm(forms.ModelForm):
    """Blog post form"""
    def clean(self):
        cleaned_data = super().clean()
        header = cleaned_data.get('header')
        if 'fuck' in header:
            self.add_error('header', 'Obsolete lexic')

    class Meta:
        model = Post
        fields = ['header', 'text', 'image']

    def __init__(self, *args, **kwargs):
        super(BlogPostForm, self).__init__(*args, **kwargs)
        self.fields['header'].widget.attrs.update({'class':'form-control', 'placeholder':'Header of post'})
        self.fields['text'].widget.attrs.update({'class':'form-control', 'placeholder':'Text of post'})


