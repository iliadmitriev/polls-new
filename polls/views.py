from django.http import HttpResponse
from django.views.generic import View
from django.utils.translation import gettext as _


class IndexView(View):
    def get(self, *args, **kwargs):
        # request = self.request
        output = _('hello world')
        response = HttpResponse(output)
        return response

