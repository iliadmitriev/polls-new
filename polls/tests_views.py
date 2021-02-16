from django.test import TestCase, Client
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import datetime as dt
from .models import Question, Choice


class PollsIndexViewTest(TestCase):
    questions = []

    def _create_question(self, question_text, pub_date):
        question = Question.objects.create(question_text=question_text, pub_date=pub_date)
        self.questions.append(question)

    def setUp(self):
        self.client = Client(HTTP_ACCEPT_LANGUAGE='ru')

    def test_empty_index_page_200_OK(self):
        response = self.client.get(reverse('polls-index'))
        self.assertEqual(
            response.status_code, 200,
            msg='Polls index page %s is not responding '
                'with 200 OK status' % reverse('polls-index')
        )
        self.assertContains(response, _('There is no polls yet'))
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_future_question_index_page_200_OK(self):
        self._create_question(
            question_text='Future question',
            pub_date=timezone.now() + dt.timedelta(days=30)
        )
        response = self.client.get(reverse('polls-index'))
        self.assertContains(response, _('There is no polls yet'))
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_past_question_index_page_200_OK(self):
        self._create_question(
            question_text='Past question',
            pub_date=timezone.now() - dt.timedelta(days=30)
        )
        response = self.client.get(reverse('polls-index'))
        self.assertContains(response, _('There is no polls yet'))
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_current_question_index_page_200_OK(self):
        self._create_question(
            question_text='Test question',
            pub_date=timezone.now() - dt.timedelta(seconds=1)
        )
        response = self.client.get(reverse('polls-index'))
        self.assertEqual(
            response.status_code, 200,
            msg='Polls index page %s is not responding '
                'with 200 OK status' % reverse('polls-index')
        )
        self.assertQuerysetEqual(
            response.context['question_list'],
            ['<Question: 1: Test question>']
        )


class PollsDetailViewTest(TestCase):

    def _create_question(self, question_text, pub_date):
        return Question.objects.create(question_text=question_text, pub_date=pub_date)

    def _create_choice(self, question, choice_text):
        return Choice.objects.create(question=question, choice_text=choice_text)

    def setUp(self):
        self.client = Client(HTTP_ACCEPT_LANGUAGE='ru')

    def test_question_detail_view_200_OK(self):
        q = self._create_question(
            question_text='Test question',
            pub_date=timezone.now() - dt.timedelta(seconds=1)
        )
        response = self.client.get(reverse('polls-detail', args=(q.id,)))
        self.assertEqual(response.status_code, 200)

    def test_non_existent_question_detail_view_404_not_found(self):
        q = self._create_question(
            question_text='Test question',
            pub_date=timezone.now() - dt.timedelta(seconds=1)
        )
        response = self.client.get(reverse('polls-detail', args=(q.id + 1,)))
        self.assertEqual(response.status_code, 404)

    def test_question_detail_view_choices(self):
        q = self._create_question(
            question_text='Test question',
            pub_date=timezone.now() - dt.timedelta(seconds=1)
        )
        for i in range(3):
            c = self._create_choice(
                question=q,
                choice_text='choice %s' % i
            )
        response = self.client.get(reverse('polls-detail', args=(q.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['question'].choice_set.all()), 3)


