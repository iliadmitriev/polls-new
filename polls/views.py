from django.views.generic import DetailView, ListView, View
from django.shortcuts import HttpResponseRedirect, reverse, get_object_or_404, HttpResponse
from .models import Question, Choice


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
        question = get_object_or_404(Question, pk=kwargs.get('pk'))
        try:
            choice_voted = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return HttpResponseRedirect(reverse('polls-detail', kwargs=kwargs))
        else:
            choice_voted.votes += 1
            choice_voted.save()
            return HttpResponseRedirect(reverse('polls-result', kwargs=kwargs))
