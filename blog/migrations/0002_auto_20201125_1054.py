# Generated by Django 2.2 on 2020-11-25 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alamat',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.EmailField(default='nama@web.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
