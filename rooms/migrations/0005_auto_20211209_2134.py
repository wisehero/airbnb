# Generated by Django 2.2.5 on 2021-12-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20211209_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(upload_to='room_photos'),
        ),
    ]
