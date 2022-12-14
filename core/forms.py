from django import forms
from django.utils.safestring import mark_safe


class CommentForm(forms.Form):
    text = forms.CharField(label='text', max_length=300)
    # video = forms.IntegerField(widget=forms.HiddenInput(), initial=1)


class NewVideoForm(forms.Form):
    title = forms.CharField(label=' Video Title', max_length=20)
    description = forms.CharField(label='Video Description', max_length=300)
    file = forms.FileField()


class ChannelForm(forms.Form):
    channel_name = forms.CharField(max_length=50, label='Channel Name')
    channel_image = forms.ImageField(max_length=50)
    # username = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # suscribers = models.IntegerField(default=0, blank=False, null=False)
