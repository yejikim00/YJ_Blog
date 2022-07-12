from django.contrib import admin
from django.urls import path, include
import common.views
import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('common/', include('common.urls')),
    path('', blog.views.index, name='index'),
]
