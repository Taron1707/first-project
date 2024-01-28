# Generated by Django 4.2.7 on 2023-12-28 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atricles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='name')),
                ('anons', models.CharField(max_length=250, verbose_name='anons')),
                ('textfull', models.TextField(verbose_name='Text')),
                ('date', models.DateTimeField(verbose_name='datapublikacia')),
            ],
        ),
    ]
