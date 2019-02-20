from django import forms

from .models import Tweet
# from core.utils import get_urls


class TweetForm(forms.ModelForm):

    # content = forms.CharField(
    #     label='',
    #     widget=forms.Textarea(attrs={
    #         'placeholder': 'What\'s happening!',
    #         'class': 'form-control'
    #     })
    # )

    class Meta:
        model = Tweet
        exclude = ('user',)
        fields = ('content',)

    # def clean_content(self, *args, **kwargs):
        # content = self.cleaned_data.get('content')
        # if get_urls(content):
            # raise forms.ValidationError('Text cannot consist of urls')
        # return content
