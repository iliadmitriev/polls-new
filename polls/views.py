from django.http import HttpResponse
from django.views.generic import View, DetailView, ListView
from django.utils.translation import gettext as _
from pprint import pformat
from .models import Question


class PollsIndexView(ListView):
    queryset = Question.objects.order_by('-pub_date')[:5]
    template_name = 'polls_index_view.html'


class PollsDetailView(DetailView):
    model = Question
    template_name = 'polls_detail_view.html'
