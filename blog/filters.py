import django_filters
from .models import *
from django.db.models import Q
from django.forms.widgets import TextInput

class PostsFilterAlt(django_filters.FilterSet):
    q = django_filters.CharFilter(method='mainFilter',label='Pesquisa',widget=TextInput(attrs={'placeholder': 'Pesquise aqui pelos nossos posts!'}))

    class Meta:
        model = Posts
        fields = ['q']

    def mainFilter(self,queryset,name,value):
        return Posts.objects.filter(
            Q(title__icontains=value) | Q(desc__icontains=value)  | Q(body__icontains=value)  
        )
