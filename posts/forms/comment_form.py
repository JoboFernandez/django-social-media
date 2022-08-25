from django import forms

from ..models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "name": "comment",
                "placeholder": "comment",
                "class": "form-control",
                "row": "3"
            }
        ),
        label=''
    )

    class Meta:
        model = Comment
        fields = ['content']

