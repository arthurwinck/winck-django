from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',views.imoveis_index, name="imoveis"),
    path('<slug:slug>/',views.imoveis_details, name="details_imoveis"),
]
