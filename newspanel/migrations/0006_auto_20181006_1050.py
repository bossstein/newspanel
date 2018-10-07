# Generated by Django 2.1.2 on 2018-10-06 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newspanel', '0005_auto_20181006_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='catagory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newspanel.Catagory'),
        ),
    ]