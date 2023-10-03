from django.views.generic import ListView

from django.http import HttpResponse
from django.utils import simplejson as json

from .models import Place


class Lookup(ListView):
    model = Place

    def get_queryset(self):
        qs = super(Lookup, self).get_queryset()

        term = self.request.GET.get('term', '')
        qs = qs.filter(name__istartswith=term)
        qs = qs.order_by('name')

        return qs

    def render_to_response(self, context, **kwargs):

        to_serialize = []
        for obj in context['object_list'][:8]:
            to_serialize.append({
                "id":   obj.id,
                "text": obj.context_name,
                "lat":  obj.centre.y,
                "lon":  obj.centre.x,
            });

        json_string = json.dumps( to_serialize, sort_keys=True, indent=4 )

        kwargs['content_type'] = 'application/json'
        return HttpResponse(json_string, **kwargs)
