"""
Forms for the blog application.

This module contains the forms for the blog application. The forms are
used to validate the user input.

The forms are:

    - EmailPostForm: a form to send a post by email to a friend
    - CommentForm: a form to validate a comment model

"""
from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    """
    Form to send a post by email to a friend.

    Fields:
        - name: name of the person sending the email
        - email: email address of the person sending the email
        - to: email address of the person to send the email to
        - comments: additional comments to add to the email
    """
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea
    )


class CommentForm(forms.ModelForm):
    """
    Form to validate a comment model.

    Fields:
        - name: name of the person posting the comment
        - email: email address of the person posting the comment
        - body: the text of the comment
    """
    class Meta:
        """
        Meta class for CommentForm.

        Attributes:
            - model: the model the form is for
            - fields: the fields to include in the form
        """
        model = Comment
        fields = ('name', 'email', 'body')
