# Generated by Django 5.0.3 on 2024-03-13 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zooApp', '0004_dog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Картинка'),
        ),
    ]
