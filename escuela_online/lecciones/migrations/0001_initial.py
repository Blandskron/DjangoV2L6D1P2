# Generated by Django 5.0.6 on 2024-05-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('duracion_video', models.IntegerField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='lecciones_imagenes/')),
            ],
        ),
    ]
