import django_filters
from .models import *
from django.db.models import Q
from django.forms.widgets import TextInput

class ImoveisFilter(django_filters.FilterSet):
    class Meta:
        model = Imoveis
        fields = ['tipo','quartos','banheiros','suites','vagas']

class ImoveisFilterAlt(django_filters.FilterSet):
    q = django_filters.CharFilter(method='mainFilter',label='Pesquisa',widget=TextInput(attrs={'placeholder': 'Digite o nome do imóvel ou endereço (Rua, Bairro e Cidade)!'}))

    class Meta:
        model = Imoveis
        fields = ['q','tipo','quartos','banheiros','suites','vagas']

    def mainFilter(self,queryset,name,value):
        return Imoveis.objects.filter(
            Q(nome__icontains=value) | Q(endereco__icontains=value)
        )
