# Generated by Django 3.1 on 2020-08-30 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the product you would like to purchase.', max_length=250)),
                ('slug', models.SlugField(blank=True, max_length=250, unique_for_date='created')),
                ('category', models.CharField(choices=[('phones', 'Phones'), ('computers', 'Computers'), ('electronics', 'Electronics'), ('home & kitchen', 'Home & Kitchen'), ('office', 'Office')], default='Phones', help_text='Indicates the category which your products belongs, helping us find the best vendor', max_length=20)),
                ('condition', models.CharField(choices=[('new', 'New'), ('refurbirshed', 'Refurbished'), ('used', 'Used')], default='New', help_text='What condition is the item that you would like to purchase?', max_length=20)),
                ('image', models.ImageField(blank=True, help_text='Upload a photo of a similar image', upload_to='images/%Y/%m/%d')),
                ('description', models.TextField(help_text='Provide specifications of the product.')),
                ('created', models.DateField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_ordered', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
    ]