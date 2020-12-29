from django.db import models


class Retreat(models.Model):
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    description = models.TextField(null=False, blank=False, default='')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2, null=False, default=0)
    location = models.CharField(max_length=200)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
