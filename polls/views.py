from django.views.generic import DetailView, ListView, View
from django.shortcuts import HttpResponseRedirect, reverse
from .models import Question


class PollsIndexView(ListView):
    queryset = Question.objects.order_by('-pub_date')[:5]
    template_name = 'polls_index_view.html'


class PollsDetailView(DetailView):
    model = Question
    template_name = 'polls_detail_view.html'


class PollsResultView(DetailView):
    model = Question
    template_name = 'polls_results_view.html'


class PollsVoteView(View):
    def post(self, request, *args, **kwargs):
        redirect = HttpResponseRedirect(reverse('polls-result', kwargs=kwargs))
        return redirect
