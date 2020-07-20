from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from slugify import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Posts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
    title = models.CharField('Título',max_length=100)
    desc = models.CharField('Descrição',max_length=100,default='')
    slug = models.SlugField()
    body = RichTextUploadingField('Corpo do texto')
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField('Capa',default='default.png',blank=True)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

def save_post(sender, instance, **kwargs):
        instance.slug  = slugify(instance.title)

pre_save.connect(save_post, sender=Posts)
