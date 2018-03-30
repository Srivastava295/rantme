"""import required modules."""
from django import forms
from .models import Topic, Post


class NewTopicForm(forms.ModelForm):
    """Topic form."""

    message = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
    ), max_length=4000, help_text='The max length of the text is 4000')

    class Meta:
        """Meta data."""

        model = Topic
        fields = ['subject', 'message']


class PostForm(forms.ModelForm):
    """Post form."""

    class Meta:
        """Meta data."""

        model = Post
        fields = ['message', ]
