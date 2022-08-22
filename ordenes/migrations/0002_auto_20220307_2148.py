# Generated by Django 2.2.14 on 2022-03-07 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ordenes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoordenado',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Producto'),
        ),
        migrations.AddField(
            model_name='productoordenado',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orden',
            name='productos',
            field=models.ManyToManyField(to='ordenes.ProductoOrdenado'),
        ),
        migrations.AddField(
            model_name='orden',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='detalleorden',
            name='orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ordenes.Orden', verbose_name='Orden'),
        ),
        migrations.AddField(
            model_name='detalleorden',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Producto', verbose_name='Producto'),
        ),
    ]
