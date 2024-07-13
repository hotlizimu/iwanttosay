from django.urls import path
from . import views
app_name = 'iwanttosay_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('read/<int:password>', views.read, name='read'),
    path('write/', views.write, name='write'),
    path('delete/<int:password>', views.delete, name='delete'),
]
