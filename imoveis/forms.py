from django import forms as forms
from django.conf import settings
from django.core import validators
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_image_file_extension
from django.utils.encoding import force_str
from django.utils.translation import gettext as _
from django.forms.widgets import TextInput,NumberInput,Select
from django.utils.safestring import mark_safe
from .models import Imoveis, ImoveisImage
from multiselectfield import MultiSelectField

class UserFullnameChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return force_str(obj.get_full_name())


class ImoveisAdminForm(forms.ModelForm): 
    user = UserFullnameChoiceField(queryset=User.objects.all())

    class Meta:
        model = Imoveis
        fields = (
            "user",
            "nome",
            "slug",
            "tipo",
            "areaP",
            "areaT",
            "preco",
            "endereco",
            "rua",
            "num",
            "bairro",
            "cidade",
            "desc",
            "itens",
            "quartos",
            "suites",
            "banheiros",
            "vagas",
            "thumb",
        )

    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label = _("Adicionar Fotos:"),
        required=False,
    )

    def clean_photos(self):

        for upload in self.files.getlist("images"):
            validate_image_file_extension(upload)

    def save_photos(self,imovel):

        for upload in self.files.getlist("images"):
            image = ImoveisImage(imovel=imovel,image=upload)
            image.save()

            if imovel.image_list == '':
                imovel.image_list += f"{image}"
            else:
                imovel.image_list += f",{image}"

class SearchForm(forms.Form):
    #Dei override nos tipos para poder escolher o 'todos'
    TIPOS_CHOICES = (
    ('Todos','Todos'),
    ('Apartamento','Apartamento'),
    ('Casa','Casa'),
    ('Sobrado','Sobrado'),
    ('Kitnet','Kitnet'),
    ('Loft','Loft'),
    ('Terreno','Terreno'),    
    )

    NUMERO_CHOICES = (
        ('',''),
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )

    Tipo = forms.ChoiceField(choices=TIPOS_CHOICES,widget=Select(attrs={'class':'search-select', 'id':'search-select', 'name':'search-select'}))
    Search = forms.CharField(required=False,widget=TextInput(attrs={'class': 'search--imovel', 'id': 'search', 'name': 'search', 'placeholder': 'Pesquise pelo nome do imóvel ou seu endereço!'}))
    Quartos = forms.ChoiceField(required=False,choices=NUMERO_CHOICES,widget=Select(attrs={'class': 'search--item', 'name': 'qu'}))
    Suites = forms.ChoiceField(required=False,choices=NUMERO_CHOICES,widget=Select(attrs={'class': 'search--item', 'name': 'su'}))
    Banheiros = forms.ChoiceField(required=False,choices=NUMERO_CHOICES,widget=Select(attrs={'class': 'search--item', 'name': 'bh'}))
    Vagas = forms.ChoiceField(required=False,choices=NUMERO_CHOICES,widget=Select(attrs={'class': 'search--item', 'name' : 'va'}))

class BlogForm(forms.Form):
    Search = forms.CharField(widget=TextInput(attrs={'class': 'w100', 'id': 'searchPosts', 'name': 'search', 'placeholder': 'Pesquise pelo nossos posts!'}))