from django.db import models
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    question_text = models.CharField(_('question text'), max_length=200)
    pub_date = models.DateTimeField(_('date published'))

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(_('choice text'), max_length=200)
    votes = models.IntegerField(_('votes'), default=0)

    class Meta:
        verbose_name = _('Choice')
        verbose_name_plural = _('Choices')
