
from django import forms as forms_django
from django.contrib import admin
from django.template.loader import get_template
from django.utils.translation import gettext as _
from django.utils.safestring import mark_safe
from .models import Imoveis,ImoveisImage
from .forms import ImoveisAdminForm
from string import Template


admin.site.site_header = 'Dashboard Winck Imóveis'

class ImoveisImageInline(admin.StackedInline):
    model = ImoveisImage
    fields = ('image','imageThumb')
    list_display = ('image',)
    readonly_fields = ('imageThumb',)

@admin.register(Imoveis)
class ImoveisAdmin(admin.ModelAdmin):
    form = ImoveisAdminForm
    inlines = [ImoveisImageInline]
    list_display = ('nome','id','date','tipo','Capa',)
    list_filter = ('date','tipo',)
    exclude = ('slug',)
    readonly_fields =('Capa',)
    search_fields = ('nome','endereco','itens')
    
    def save_related(self,request,form,formsets,change):
        super().save_related(request,form,formsets,change)
        form.save_photos(form.instance)
    
    class Meta:    
        model = Imoveis


        

