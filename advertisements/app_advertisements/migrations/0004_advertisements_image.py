# Generated by Django 4.2.3 on 2023-08-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0003_advertisements_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements',
            name='image',
            field=models.ImageField(default='', upload_to='advertisements/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
