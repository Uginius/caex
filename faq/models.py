from django.db import models


class Ques(models.Model):
    question = models.TextField()
    note = models.CharField(null=True, blank=True, max_length=250)
    answer = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    order = models.IntegerField(null=True, blank=True)
    published = models.BooleanField(default=True)

    @property
    def question_short(self):
        q = str(self.question)
        return q if len(q) < 48 else q[:48] + '...'

    @property
    def answer_short(self):
        a = str(self.answer)
        return a if len(a) < 96 else a[:96] + '...'

    def __str__(self):
        return f'{self.question_short} : {self.answer_short}'

    class Meta:
        ordering = ['order', 'pk']
        verbose_name = 'FAQ'
