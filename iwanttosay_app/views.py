from django.shortcuts import render, redirect, get_object_or_404
from .models import Texts
from .forms import TextReadForm, TextWriteForm


# Create your views here.
def index(request):
    if request.method != 'POST':
        form = TextReadForm()
    else:
        form = TextReadForm(data=request.POST)
        if form.is_valid():
            getform = form.save(commit=False)
            if Texts.objects.filter(password=getform.password).exists():
                return redirect('iwanttosay_app:read', password=getform.password)
            else:
                form.add_error('password', "输入的暗号不存在")
    return render(request, 'index.html', {'form': form})


def read(request, password):
    text = get_object_or_404(Texts, password=password)
    return render(request, 'read.html', {'text': text})


def write(request):
    if request.method != 'POST':
        form = TextWriteForm()
    else:
        form = TextWriteForm(data=request.POST)
        if form.is_valid and not Texts.objects.filter(password=form.save(commit=False).password).exists():
            form.save()
            return redirect('iwanttosay_app:index')
        else:
            form.add_error('password', "输入的暗号已存在或输入无效")
    return render(request, 'write.html', {'form': form})


def delete(request, password):
    get_object_or_404(Texts, password=password).delete()
    return redirect('iwanttosay_app:index')
