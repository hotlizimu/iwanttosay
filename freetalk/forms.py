from django import forms
from .models import Rooms, Messages


class JoinRoom(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ['number']
        labels = {'number': '输入Free Talk房间号（八位以内数字）'}


class WriteMessage(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['message']
        labels = {'message': '写点你想说的吧'}
        widgets = {'message': forms.Textarea(attrs={'rows': 3})}

