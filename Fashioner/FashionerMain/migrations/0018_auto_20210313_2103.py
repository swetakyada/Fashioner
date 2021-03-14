# Generated by Django 3.1.5 on 2021-03-13 15:33

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('FashionerMain', '0017_auto_20210313_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='cart',
            name='size',
            field=models.CharField(choices=[('XL', 'Extra Large'), ('XXL', 'Extra Extra Large'), ('L', 'Large'), ('S', 'Small'), ('M', 'Medium')], default='', max_length=3),
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('XL', 'Extra Large'), ('XXL', 'Extra Extra Large'), ('L', 'Large'), ('S', 'Small'), ('M', 'Medium')], default='', max_length=12),
        ),
    ]