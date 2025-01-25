


### localhost:8000/ --- home

#### localhost:8000/about ---- about

### localhost:8000/blog/contact

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
    
]

