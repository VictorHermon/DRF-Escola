# Generated by Django 4.0.4 on 2022-04-13 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
