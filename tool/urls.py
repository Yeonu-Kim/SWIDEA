from django.urls import path
from .views import index, create, modify, detail, delete

app_name = 'tool'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('modify/<int:pk>', modify, name='modify'),
    path('idea/<int:pk>/', detail, name='detail'),
    path('delete/<int:pk>/', delete, name='delete')
]