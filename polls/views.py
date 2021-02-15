from django.http import HttpResponse
from django.views.generic import View, DetailView
from django.utils.translation import gettext as _
from pprint import pprint, pformat
from .models import Question, Choice


class PollsIndexView(View):
    def get(self, *args, **kwargs):
        request = self.request
        output = _('hello world') + '\n%s' % pformat(request.__dict__)

        response = HttpResponse(output, content_type='text/plain; charset=utf-8')
        return response


class PollsDetailView(DetailView):
    model = Question
    template_name = 'polls_detail_view.html'
