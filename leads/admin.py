from django.contrib import admin
from .models import Lead
from .forms import LeadForm
# Register your models here.

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('nome','email','celular','id')

    class Meta:
        model = Lead
        