from django.views.generic import DetailView, View
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


class InfoDetailView(DetailView):
    template_name = 'information.html'
    context_object_name = 'info'

    def get_object(self):
        if self.request.user.is_authenticated():
            obj = self.request.user.info.all().first()
            return obj


def login_view(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        possible_user = User.objects.filter(Q(username=username) &
                                            Q(is_active=True)).first()
        if possible_user is None:
                error_msg = ("Provided wrong credentials data")
        else:
            user = authenticate(username=possible_user.username,
                                password=password)
            if user is None:
                error_msg = ("Provided wrong credentials data")
            else:
                login(request, user)
                return HttpResponseRedirect(reverse_lazy('info'))
    else:
        return render_to_response('login.html', {}, context)
    return render_to_response('login.html',
                              {'username': username,
                               'password': password,
                               'error_msg': error_msg}, context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('info'))
