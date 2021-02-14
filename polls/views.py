from django.http import HttpResponse
from django.views.generic import View
from django.utils.translation import gettext as _
from pprint import pprint, pformat


class IndexView(View):
    def get(self, *args, **kwargs):
        request = self.request
        output = _('hello world') + '\n%s' % pformat(request.__dict__)

        response = HttpResponse(output, content_type='text/plain; charset=utf-8')
        return response

