from django.urls import path
from polls.views import PollsIndexView, PollsDetailView

urlpatterns = [
    path('', PollsIndexView.as_view(), name='polls-index'),
    path('<int:pk>/', PollsDetailView.as_view(), name='polls-detail')
]
