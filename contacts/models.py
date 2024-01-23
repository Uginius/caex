from django.db import models


class Subject(models.Model):
    theme = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.theme


class Feedback(models.Model):
    created = models.DateTimeField(auto_created=True)
    name = models.CharField(max_length=150)
    account = models.CharField(max_length=150, verbose_name='Email or Phone')
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    message = models.TextField()
    phone = models.CharField(max_length=31, blank=True)
    email = models.CharField(max_length=63, blank=True)

    def __str__(self):
        return f'{self.name} : {self.subject} : {self.message}'

    class Meta:
        ordering = '-pk',
