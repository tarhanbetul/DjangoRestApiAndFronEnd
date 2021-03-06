# Generated by Django 2.2.3 on 2020-10-02 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('price', models.FloatField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shopcart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
