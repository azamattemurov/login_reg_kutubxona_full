from audioop import reverse

from django.db import models
from django.utils.html import mark_safe



class Book(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="55" height="55"/>' % self.image)

    def get_absolute_url(self):
        return reverse('User-Posts-Details', kwargs={'pk': self.pk})