from django import forms

from ..models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "name": "post",
                "placeholder": "Write your post here.",
                "class": "form-control",
                "row": "8"
            }
        ),
        label=''
    )

    class Meta:
        model = Post
        fields = ['content']

