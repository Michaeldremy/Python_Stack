# Generated by Django 2.2 on 2020-03-10 21:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninjas',
            name='dojo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninja', to='dojo_ninjas_app.Dojos'),
        ),
    ]