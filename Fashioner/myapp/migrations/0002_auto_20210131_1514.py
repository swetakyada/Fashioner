# Generated by Django 3.1.4 on 2021-01-31 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100000)),
                ('product_image', models.ImageField(height_field=300, max_length=500, upload_to=None, width_field=300)),
            ],
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]
