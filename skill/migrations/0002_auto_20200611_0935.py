# Generated by Django 3.0.3 on 2020-06-11 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50)),
                ('cemail', models.EmailField(max_length=50)),
                ('cquery', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='myskill',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
