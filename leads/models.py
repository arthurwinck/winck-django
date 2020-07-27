from django.db import models
from multiselectfield import MultiSelectField
from django.utils.safestring import mark_safe

CONTATO_OPTIONS = (
    ('Whatsapp',mark_safe('<div class="contact-li"><i class="fab fa-whatsapp  fa-2x"></i><p>Whatsapp</p></div')),
    ('Ligação',mark_safe('<div class="contact-li"><i class="fas fa-phone-alt fa-2x phone phone-header"></i><p>Ligação</p></div>')),
    ('Email',mark_safe('<div class="contact-li"><i class="far fa-envelope  fa-2x" style="color:#FF7900;"></i><p>Email</p></div>'))
)

class Lead(models.Model):
    nome = models.CharField('Nome',max_length=60)
    email = models.CharField('Email',max_length=60)
    celular = models.CharField('Celular',max_length=13)
    comentarios = models.CharField('Comentários',max_length=200)
    contato = MultiSelectField(default='',choices=CONTATO_OPTIONS)

