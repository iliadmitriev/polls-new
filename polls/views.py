from django.views.generic import DetailView, ListView
from .models import Question


class PollsIndexView(ListView):
    queryset = Question.objects.order_by('-pub_date')[:5]
    template_name = 'polls_index_view.html'


class PollsDetailView(DetailView):
    model = Question
    template_name = 'polls_detail_view.html'
