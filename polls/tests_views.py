from django.test import TestCase, Client
from django.shortcuts import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
import datetime as dt
from .models import Question, Choice
import random


def _create_question(question_text, pub_date):
    return Question.objects.create(question_text=question_text, pub_date=pub_date)


def _create_choice(question, choice_text):
    return Choice.objects.create(question=question, choice_text=choice_text)


def _create_question_with_choices():
    q = _create_question(
        question_text='Test question',
        pub_date=timezone.now() - dt.timedelta(seconds=1)
    )
    choices = []
    for i in range(3):
        choices.append(
            _create_choice(
                question=q,
                choice_text='choice %s' % i
            )
        )
    return {'question': q, 'choices': choices}


class PollsIndexViewTest(TestCase):

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
        _create_question(
            question_text='Future question',
            pub_date=timezone.now() + dt.timedelta(days=30)
        )
        response = self.client.get(reverse('polls-index'))
        self.assertContains(response, _('There is no polls yet'))
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_past_question_index_page_200_OK(self):
        _create_question(
            question_text='Past question',
            pub_date=timezone.now() - dt.timedelta(days=30)
        )
        response = self.client.get(reverse('polls-index'))
        self.assertContains(response, _('There is no polls yet'))
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_current_question_index_page_200_OK(self):
        _create_question(
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

    def setUp(self):
        self.client = Client(HTTP_ACCEPT_LANGUAGE='ru')

    def test_question_detail_view_200_OK(self):
        q = _create_question(
            question_text='Test question',
            pub_date=timezone.now() - dt.timedelta(seconds=1)
        )
        response = self.client.get(reverse('polls-detail', args=(q.id,)))
        self.assertEqual(response.status_code, 200)

    def test_non_existent_question_detail_view_404_not_found(self):
        q = _create_question(
            question_text='Test question',
            pub_date=timezone.now() - dt.timedelta(seconds=1)
        )
        response = self.client.get(reverse('polls-detail', args=(q.id + 1,)))
        self.assertEqual(response.status_code, 404)

    def test_question_detail_view_choices(self):
        question = _create_question_with_choices()
        response = self.client.get(reverse('polls-detail', args=(question['question'].id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['question'].choice_set.all()), 3)


class PollsVoteViewTest(TestCase):

    def setUp(self) -> None:
        self.client = Client(HTTP_ACCEPT_LANGUAGE='ru')

    def test_polls_vote_view_post_redirect_back(self):
        question = _create_question_with_choices()
        question_id = question['question'].id
        response = self.client.post(
            reverse('polls-vote', args=(question_id,)),
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            reverse('polls-detail', args=(question_id,))
        )
        self.assertNotEqual(
            response.url,
            reverse('polls-result', args=(question_id,))
        )

    def test_polls_vote_view_post_redirect_result(self):
        question = _create_question_with_choices()
        question_id = question['question'].id
        choices = question['choices']
        random_choice = random.choice(choices)
        votes = random_choice.votes
        response = self.client.post(
            reverse('polls-vote', args=(question_id,)),
            {'choice': random_choice.id}
        )
        random_choice.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(
            response.url,
            reverse('polls-detail', args=(question_id,))
        )
        self.assertRedirects(
            response,
            reverse('polls-result', args=(question_id,))
        )
        self.assertEqual(votes + 1, random_choice.votes)
