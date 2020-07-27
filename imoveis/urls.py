from django.urls import path
from .views import imoveis_details, imoveis_index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',imoveis_index, name="imoveis"),
    path('<slug:slug>/',imoveis_details, name="details_imoveis"),
]
