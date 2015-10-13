from django.views.generic import DetailView
from apps.info.models import Info


class InfoDetailView(DetailView):
    template_name = 'information.html'
    context_object_name = 'info'

    def get_object(self):
        obj = Info.objects.get(id=1)
        return obj
