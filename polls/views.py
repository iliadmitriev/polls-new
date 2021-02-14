from django.http import HttpResponse
from django.views.generic import View


class IndexView(View):
    def get(self, *args, **kwargs):
        request = self.request
        response = HttpResponse(b'hello world')
        return response

