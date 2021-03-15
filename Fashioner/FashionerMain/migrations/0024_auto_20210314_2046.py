# Generated by Django 3.1.5 on 2021-03-14 15:16

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('FashionerMain', '0023_auto_20210314_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='size',
            field=models.CharField(choices=[('XXL', 'Extra Extra Large'), ('M', 'Medium'), ('S', 'Small'), ('XL', 'Extra Large'), ('L', 'Large')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_for',
            field=models.CharField(choices=[('K', 'Kids'), ('M', 'Men'), ('W', 'Women')], max_length=5),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.CharField(default=' ', max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('XXL', 'Extra Extra Large'), ('M', 'Medium'), ('S', 'Small'), ('XL', 'Extra Large'), ('L', 'Large')], default='', max_length=12),
        ),
    ]
