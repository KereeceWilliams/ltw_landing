from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from .models import *

class Home(TemplateView):
    template_name = "home.html"

# Create your views here.
class RegisterCreateView(CreateView):
    model = Register
    template_name = "register/register_form.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('register_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RegisterCreateView, self).form_valid(form)
      
class RegisterListView(ListView):
    model = Register
    template_name = "register/register_list.html"