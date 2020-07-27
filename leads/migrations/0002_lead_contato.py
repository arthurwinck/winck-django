# Generated by Django 3.0.7 on 2020-07-27 19:07

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='contato',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Whatsapp', '<div class="contact-li"><i class="fab fa-whatsapp  fa-2x"></i><p>Whatsapp</p></div'), ('Ligação', '<div class="contact-li"><i class="fas fa-phone-alt fa-2x phone phone-header"></i><p>Ligação</p></div>'), ('Email', '<div class="contact-li"><i class="far fa-envelope  fa-2x" style="color:#FF7900;"></i><p>Email</p></div>')], default='', max_length=22),
        ),
    ]
