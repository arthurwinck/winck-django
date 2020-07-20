from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from blog import views as blog_views
from users import views as user_views


urlpatterns = [
    path('',views.index,name='index'),
    path('blog/',include('blog.urls')),
    path('imoveis/', include('imoveis.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('sobre/', views.sobre, name='sobre'),
    path('caixa/', views.caixa, name='caixa'),
    path('acessoria/', views.acessoria, name='acessoria'),
    path('contato/', views.contato, name='contato'),
    path('encomenda/', views.contato, name='encomenda'),
    path('register/', user_views.register, name='register'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    ]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
