from django.urls import path
from .views import index, create, modify, detail, delete, makePick, addInterest, minusInterest

app_name = 'idea'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('modify/<int:pk>', modify, name='modify'),
    path('idea/<int:pk>/', detail, name='detail'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('pick/<int:pk>/', makePick, name="make_pick"),
    path('idea/<int:pk>/add_interest/', addInterest, name='add_interest'),
    path('idea/<int:pk>/minus_interest/', minusInterest, name='add_interest')
]