# Generated by Django 2.2 on 2020-03-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0002_auto_20200310_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
