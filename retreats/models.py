from django.db import models


class Retreat(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField(u'Date of retreat', help_text=u'Date of retreat')
    duration = models.DurationField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=200)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name
