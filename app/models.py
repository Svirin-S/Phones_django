from django.db import models
from django.urls import reverse

class Phone(models.Model):
    name = models.CharField(max_length=60)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=10)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')


    def __str__(self) -> str:
        return self.name


    def get_url(self):
        return reverse('slug', kwargs={'slug':self.slug})  

          


  