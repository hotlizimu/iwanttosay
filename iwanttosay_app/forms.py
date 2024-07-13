from django import forms
from .models import Texts


class TextReadForm(forms.ModelForm):
    class Meta:
        model = Texts
        fields = ['password']
        labels = {'password': '输入你的暗号（八位以内数字）'}


class TextWriteForm(forms.ModelForm):
    class Meta:
        model = Texts
        fields = ['password', 'text']
        labels = {'password': '输入你的暗号（记得告诉Ta哦）', 'text': '写点你想说的吧'}
