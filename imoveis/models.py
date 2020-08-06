from django import forms as forms_django
from django.apps import apps
from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from multiselectfield import MultiSelectField
from slugify import slugify

ITENS_CHOICES = (
    ('Churrasqueira','Churrasqueira'),
    ('Piscina','Piscina'),
    ('Playground','Playground'),
    ('Academia','Academia'),
    ('Bosque','Bosque'),
    ('Jardim','Jardim'),
    ('Ar condicionado','Ar condicionado'),
    ('Salão de festas','Salão de festas'),
    ('Medição de água individualizada','Medição de água individualizada'),
)

TIPOS_CHOICES = (
    ('Apartamento','Apartamento'),
    ('Casa','Casa'),
    ('Sobrado','Sobrado'),
    ('Kitnet','Kitnet'),
    ('Loft','Loft'),
    ('Terreno','Terreno'),
    
)

ENDERECOS_CHOICES = (
    ('Centro','Centro'),
    ('Exposição','Exposição'),
    ('Desvio Rizzo','Desvio Rizzo'),
    ('Cristo Redentor','Cristo Redentor'),
    ('Panazzolo','Panazzolo'),
    
)

# Create your models here.
class Imoveis(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.DO_NOTHING)
    nome = models.CharField('Nome do Imóvel',max_length=100)
    slug = models.SlugField(unique=True)
    tipo = models.CharField('Tipo',choices=TIPOS_CHOICES,default='',max_length=100)
    areaP = models.CharField('Área Privativa',max_length=10,default='0')
    areaT = models.CharField('Área Total',max_length=10,default='0')
    endereco = models.CharField('Endereço',max_length=100,default='')
    rua = models.CharField('Rua',max_length=40,default='',blank=True)
    num = models.IntegerField('Número',default=0,blank=True,null=True)
    bairro = models.CharField(max_length=40,default='',blank=True)
    cidade = models.CharField(max_length=40,default='',blank=True)
    preco = models.CharField('Preço',max_length=12,default='0')
    desc =  RichTextUploadingField('Descrição',max_length=600)
    date = models.DateTimeField(auto_now_add=True)
    itens = MultiSelectField(choices=ITENS_CHOICES)
    quartos = models.IntegerField(default=0)
    suites = models.IntegerField(default=0)
    banheiros = models.IntegerField(default=0)
    vagas = models.IntegerField('Vagas de Garagem',default=0)
    thumb = models.ImageField('Capa',default='e404.png', blank=True, upload_to='imoveis')
    image_list = models.CharField('Fotos',max_length=400,default='',blank=True)
    

    def Capa(self):
        return mark_safe(f'<img src="{self.thumb.url}" height="80px" />')

    def __str__(self):
        return self.nome

    def snippetAddress(self):
        return self.endereco.split('-')[0]

    def showPreco(self):
        preco = self.preco
        pList = list(preco)
        vList = []

        #condição de que se existe uma vírgula indicando centavos, a partir dai, retiramos da lista original e guardamos em uma segunda lista
        
        #aqui é meio que um lazy fix, mas se ele for menor que 3 nem irá aparecer o preço
        if len(pList) < 3:
            return ''

        elif pList[len(pList)-3] == ',':
            vList.append(pList[len(pList)-3])
            vList.append(pList[len(pList)-2])
            vList.append(pList[len(pList)-1])
            pList.pop(len(pList)-3)
            pList.pop(len(pList)-2)
            pList.pop(len(pList)-1)

        else:
            vList = [',','0','0']

        #Aqui removemos qualquer coisa que não seja um número
        preco = "".join(pList)
        preco = preco.replace(".", "",)
        preco = filter(str.isdigit, preco)
        pList = list(preco)

        #Criamos as strings a partir da listas que modificamos
        preco = "".join(preco) 
        virgula = "".join(vList)

        #Crio digits, simplesmente o número de digitos do número
        digits = len(pList)
        
        #Esse subalgoritmo é serve para sabermos quantos pontos teremos que colocar no número final
        pontos,resto = divmod(digits,3)

        if resto == 0:
            pontos -= 1

        #variável que vai aumentando à medida que vamos colocando os pontos no número
        pos = 3

        #enquanto tivermos mais que 3 dígitos, podemos colocar pontos (ex. 100 possui 3 dígitos, não vai ponto, 1000 possui 4 e por isso vai ponto....) 
        while (digits-pos) > 0:
            pList.insert(digits-pos,".")
            pos += 3

        precoFinal = "".join(pList)

        #Esse serve para o template, que se o valor é zero, nem mostramos o valor na página
        if precoFinal != '0':
            return f'R${precoFinal}' + virgula
        else:
            return ''

    def showEndereco(self):
        pass

    def showMap(self):
        return mark_safe(f"<iframe width='90%' height='450px' frameborder='0' style='border:0' src='https://www.google.com/maps/embed/v1/place?key=AIzaSyB2pzNmRALgf0qlHY8BBmv_P0cxhKO-u4E&q={self.getAddress()}' allowfullscreen></iframe>")

    #Create getAddress to create a query for google maps
    def getAddress(self):
        endereco = self.endereco
        endereco = endereco.replace('-','')
        endereco = endereco.replace(',','')
        endereco = endereco.replace(' ','+')

        return endereco

    class Meta:
        verbose_name_plural = 'Imóveis'

class ImoveisImage(models.Model):
    imovel = models.ForeignKey(Imoveis, default='', on_delete=models.CASCADE)
    image = models.ImageField('Fotos',default='e404.png',blank=True, upload_to='imoveis')
    
    def imageThumb(self):
        return mark_safe(f'<img src="{self.image.url}" width="{self.image.width*0.2}" height={self.image.height*0.2} />')
    
    def __str__(self):
        return self.imovel.nome

    class Meta:
        verbose_name_plural = 'Imagens (Imóveis)'


def save_imovel(sender, instance, **kwargs):
    instance.slug  = slugify(instance.nome)

pre_save.connect(save_imovel, sender=Imoveis)

def getEnderecoFields(sender, instance, **kwargs):
    enderecoField = instance.endereco
    rua = ''
    num = ''
    bairro = ''
    cidade = ''

    count = enderecoField.count('-')
    listEndereco = enderecoField.split('-')

    if count == 2:    
        ruaNum = listEndereco[0]

        if ',' in ruaNum:
            listRuaNum = ruaNum.split(',')
            rua = listRuaNum[0].strip()
            num = listRuaNum[1].strip()

        else:
            rua = ruaNum

        bairroCidade = listEndereco[1]

        if ',' in bairroCidade:
            listBairroCidade = bairroCidade.split(',')
            bairro = listBairroCidade[0].strip()
            cidade = listBairroCidade[1].strip()

    elif count == 1:
        bairroCidade = listEndereco[0]
        listBairroCidade = bairroCidade.split(',')

        if bairroCidade.count(',') > 1:
            rua = listBairroCidade[0].strip()
            num = listBairroCidade[1].strip()
            cidade = listBairroCidade[2].strip()


        elif ',' in bairroCidade:
            bairro = listBairroCidade[0].strip()
            cidade = listBairroCidade[1].strip()

    instance.rua = rua
    instance.bairro = bairro
    instance.cidade = cidade
    
    if num == '':
        instance.num = 0
    else:
        instance.num = num

pre_save.connect(getEnderecoFields, sender=Imoveis)
