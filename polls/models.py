import datetime
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _


class Question(models.Model):
    question_text = models.CharField(_('question text'), max_length=200)
    pub_date = models.DateTimeField(_('date published'))

    def __str__(self):
        return '%s: %s' % (self.id, self.question_text)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = _('Published recently?')

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(_('choice text'), max_length=200)
    votes = models.IntegerField(_('votes'), default=0)

    def __str__(self):
        return '%s: %s' % (self.id, self.choice_text)

    class Meta:
        verbose_name = _('Choice')
        verbose_name_plural = _('Choices')
