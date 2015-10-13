from django.views.generic import DetailView
from apps.info.models import Info


class InfoDetailView(DetailView):
    template_name = 'information.html'
    context_object_name = 'info'

    def get_object(self):
        if self.request.user and self.request.user.is_active:
            obj = self.request.user.info.all().first()
        else:
            obj = Info.objects.get(id=1)
        return obj
