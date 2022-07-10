from django.contrib import admin
from django.urls import path
import common.views
import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', common.views.index, name='index'),
]
