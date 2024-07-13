from django.urls import path
from . import views
app_name = 'freetalk'
urlpatterns = [
    path('', views.start, name='start'),
    path('<int:number>', views.room, name='room'),
]
