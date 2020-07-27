from multiselectfield import MultiSelectField
from django import forms
from django.conf import settings
from django.forms.widgets import TextInput,NumberInput,Select
from django.utils.safestring import mark_safe
from .models import Lead

class LeadForm(forms.Form):
    CONTATO_OPTIONS = (
        ('Whatsapp',mark_safe('<div class="contact-li"><i class="fab fa-whatsapp  fa-2x"></i><p>Whatsapp</p></div')),
        ('Ligação',mark_safe('<div class="contact-li"><i class="fas fa-phone-alt fa-2x phone phone-header"></i><p>Ligação</p></div>')),
        ('Email',mark_safe('<div class="contact-li"><i class="far fa-envelope  fa-2x" style="color:#FF7900;"></i><p>Email</p></div>'))
    )

    nome = forms.CharField(max_length=60,label=False,widget=forms.TextInput(attrs={'placeholder': 'Seu nome completo!'}))
    email = forms.EmailField(max_length=60,label=False,widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    celular = forms.CharField(max_length=13,label=False,widget=forms.TextInput(attrs={'placeholder': 'Celular (Whatsapp)'}))
    comentarios = forms.CharField(max_length=250,label=False,widget=forms.Textarea(attrs={'placeholder': 'Comentários (Opcional)','rows':5,'cols':20,'style':'resize: none'}))
    contato = forms.MultipleChoiceField(choices=CONTATO_OPTIONS,required=False,label='Como quer receber o nosso contato?',widget=forms.CheckboxSelectMultiple(attrs={'style':'display: inline-block; padding: 5px 5px 5px 5px;'}))
