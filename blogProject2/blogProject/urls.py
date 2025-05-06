from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='homepage'),
    path('categories/<slug:category_slug>/', views.home, name='category-wise-post'),
    path('author/', include('author.urls')),
    path('categories/', include('categories.urls')),
    path('posts/', include('posts.urls')),
]
