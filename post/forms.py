from django import forms

class PostForm(forms.Form):
    message = forms.CharField(label= 'Your message',widget=forms.Textarea)
