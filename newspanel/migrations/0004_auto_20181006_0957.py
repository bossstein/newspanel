# Generated by Django 2.1.2 on 2018-10-06 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newspanel', '0003_auto_20181006_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newspanel.Auther'),
        ),
    ]
