from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 
from django.utils import timezone
from django.utils.text import slugify 
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('phones', 'Phones'),
        ('computers', 'Computers'),
        ('electronics', 'Electronics'),
        ('home & kitchen', 'Home & Kitchen'),
        ('office', 'Office'),
    ]

    CONDITION_CHOICES = [
        ('new', 'New'),
        ('refurbirshed', 'Refurbished'),
        ('used', 'Used')
    ]
    buyer       = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='products_ordered', on_delete=models.CASCADE)
    name        = models.CharField(max_length=250, help_text="Enter the name of the product you would like to purchase.")
    slug        = models.SlugField(max_length=250, blank=True, unique_for_date='created')
    category    = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Phones', help_text='Indicates the category which your products belongs, helping us find the best vendor')
    condition   = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='New', help_text='What condition is the item that you would like to purchase?')
    image       = models.ImageField(blank=True, upload_to='images/%Y/%m/%d', help_text='Upload a photo of a similar image')
    description = models.TextField(help_text='Provide specifications of the product.')
    created     = models.DateField(auto_now_add=True, db_index=True)
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering    = ('-created',)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:detail', args=[self.id, self.slug])





