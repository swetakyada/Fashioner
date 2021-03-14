# Generated by Django 3.1.5 on 2021-03-14 06:52

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('FashionerMain', '0019_auto_20210313_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('XXL', 'Extra Extra Large'), ('L', 'Large'), ('XL', 'Extra Large'), ('M', 'Medium')], default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_for',
            field=models.CharField(choices=[('M', 'Men'), ('K', 'Kids'), ('W', 'Women')], max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='sizes',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('S', 'Small'), ('XXL', 'Extra Extra Large'), ('L', 'Large'), ('XL', 'Extra Large'), ('M', 'Medium')], default='', max_length=12),
        ),
    ]
