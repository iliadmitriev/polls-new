from django.urls import path
from polls.views import (
    PollsIndexView,
    PollsDetailView,
    PollsResultView,
    PollsVoteView
)

urlpatterns = [
    path('', PollsIndexView.as_view(), name='polls-index'),
    path('<int:pk>/', PollsDetailView.as_view(), name='polls-detail'),
    path('<int:pk>/result', PollsResultView.as_view(), name='polls-result'),
    path('<int:pk>/vote', PollsVoteView.as_view(), name='polls-vote')
]
