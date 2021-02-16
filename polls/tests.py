from django.test import TestCase
from django.utils import timezone
import datetime as dt

from .models import Question, Choice
from .admin import ChoiceAdmin
from django.contrib.admin.sites import AdminSite

from django.conf import settings
from importlib import import_module
from django.contrib.sessions.models import Session as SessionModel
from .admin import SessionAdmin
import json
from django.utils.safestring import mark_safe


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + dt.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False,
                      msg='This test is testing '
                          'polls.models.Question.was_published_recently '
                          'for a pub_date in a 30 days future')

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - dt.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False,
                      msg='This test is testing '
                          'polls.models.Question.was_published_recently '
                          'for a pub_date in 30 days past')

    def test_was_published_recently_with_23_hours_question(self):
        time = timezone.now() - dt.timedelta(hours=23)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), True,
                      msg='This test is testing '
                          'polls.models.Question.was_published_recently '
                          'for a pub_date in 23 hours past')

    def test_str_question(self):
        question = Question(question_text='Test question', pub_date=timezone.now())
        question.save()
        self.assertEqual(question.__str__(), '%s: %s' % (question.id, question.question_text))


class ChoiceModelTests(TestCase):

    def test_str_choice(self):
        question = Question(question_text='Test question', pub_date=timezone.now())
        question.save()
        choice = Choice(question=question, choice_text='Test choice')
        choice.save()
        self.assertEqual(choice.__str__(), '%s: %s' % (choice.id, choice.choice_text))


class ChoiceAdminTests(TestCase):

    def test_admin_choice_question_text(self):
        question = Question(question_text='Test question', pub_date=timezone.now())
        question.save()
        choice = Choice(question=question, choice_text='Test choice')
        choice.save()
        choice_admin = ChoiceAdmin(model=Choice, admin_site=AdminSite)
        choice_admin.question_text(obj=choice)
        self.assertEqual(choice_admin.question_text(obj=choice), question.question_text)


class SessionTestCase(TestCase):

    def setUp(self):
        engine = import_module(settings.SESSION_ENGINE)
        store = engine.SessionStore()
        store.save()

        self.session = store
        self.client.cookies[settings.SESSION_COOKIE_NAME] = store.session_key


class SessionAdminTests(SessionTestCase):

    def test_admin_session_decode(self):
        session = self.session
        session['testData'] = 'testValue'
        session.save()
        session_obj = SessionModel.objects.get(pk=session.session_key)
        session_admin = SessionAdmin(model=SessionModel, admin_site=AdminSite)
        self.assertEqual(
            session_admin._session_data(obj=session_obj),
            mark_safe(u'<pre>%s</pre>' % (json.dumps(session_obj.get_decoded(), indent=4)))
        )