from django.db import models


class Expertise(models.Model):
    order = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=127)
    text = models.CharField(max_length=127)
    image = models.CharField(max_length=127, blank=True, null=True)
    published = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} : {self.text}'

    class Meta:
        ordering = ['order', 'pk']
        verbose_name = 'Expertise'


class Partner(models.Model):
    name = models.CharField(max_length=127)
    text = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/partners/', blank=True, null=True)
    link = models.CharField(max_length=255)
    style = models.CharField(max_length=127)


