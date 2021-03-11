# Generated by Django 3.1.5 on 2021-03-11 08:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FashionerMain', '0010_auto_20210311_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_for',
            field=models.CharField(choices=[('W', 'Women'), ('K', 'Kids'), ('M', 'Men')], max_length=5),
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='FashionerMain.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
