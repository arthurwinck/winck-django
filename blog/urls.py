from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.blog_index, name="blog"),
    path('<slug:slug>/',views.blog_details, name="details_blog"),
]

