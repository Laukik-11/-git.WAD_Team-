from .models import Reply
from django import forms

# Form to post a reply


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["body"]
