# Generated by Django 3.1.5 on 2021-03-13 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FashionerMain', '0014_auto_20210313_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_for',
            field=models.CharField(choices=[('M', 'Men'), ('W', 'Women'), ('K', 'Kids')], max_length=5),
        ),
    ]