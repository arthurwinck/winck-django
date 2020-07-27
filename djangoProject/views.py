from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import HttpResponse,request
from django.template.loader import render_to_string
from django.shortcuts import render
from django.utils.html import strip_tags
from .forms import ContatoForm
from django.core.validators import validate_email
from . import settings
from imoveis.models  import Imoveis
from imoveis.views import imoveis_index
from django.db.models import Q
from django.http import HttpResponse,request, JsonResponse
from django.core.paginator import Paginator


def index(request):    
    if 'term' in request.GET:
        term = request.GET.get('term')
        query = Imoveis.objects.filter(Q(nome__icontains=term) | Q(endereco__icontains=term))

        imoveisList = []
        for imovel in query:
            imoveisList.append(imovel.nome)
            imoveisList.append(imovel.endereco)

        imoveisJson = JsonResponse(imoveisList, safe=False)

        return imoveisJson

    if 'search' in request.GET:
        imoveis_index(request)
        pass


    return render(request,"index.html")

def sobre(request):
    #return HttpResponse("sobre")

    return render(request,"sobre.html")

def caixa(request):
    return render(request,"caixa.html")

def acessoria(request):
    return render(request,"acessoria.html")

def contato(request):
    form = ContatoForm()

    if request.method == "POST":
        form = ContatoForm(request.POST or None)

        if form.is_valid():
            contatoNome = form.cleaned_data.get('Nome')
            contatoEmail = form.cleaned_data.get('Email')
            contatoCelular = form.cleaned_data.get('Celular')
            contatoComentarios = form.cleaned_data.get('Comentarios')
            
            template_email = settings.BASE_DIR + "/templates/contato_email.html"
            contatoDic ={'Nome': contatoNome, 'Email': contatoEmail, 'Celular': contatoCelular, 'Comentarios': contatoComentarios}
            
            mensagemEmail = render_to_string(template_email, { 'contatoDic': contatoDic, })

            send_mail(
                f"{contatoNome} - Contato",
                strip_tags(mensagemEmail), 
                contatoEmail,
                ['winckdeveloper@gmail.com'],
                html_message=mensagemEmail,
                fail_silently=False,
            )

        else:
            contatoDic ={'Nome': '', 'Email': '', 'Celular': '', 'Comentarios': ''}

    else:
        contatoDic ={'Nome': '', 'Email': '', 'Celular': '', 'Comentarios': ''}

    return render(request, "contato.html", {'form': form, 'contatoDic': contatoDic})
    
def encomenda(request):
    return render(request, "encomenda.html")