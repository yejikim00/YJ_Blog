from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.post, name='post'),
    path('post/<int:poster_id>/', views.detail, name='detail'),
    path('post/create/', views.poster_create, name='poster_create'),
]
