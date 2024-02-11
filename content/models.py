from django.db import models


class Txt(models.Model):
    title = models.CharField(max_length=250)
    tag = models.CharField(max_length=250, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    note = models.CharField(max_length=250, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.tag} : {self.title}'


class Titles(models.Model):
    title = models.CharField(max_length=250)
    tag = models.CharField(max_length=250, null=True, blank=True)
