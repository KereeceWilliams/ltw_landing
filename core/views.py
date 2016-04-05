from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import *

class Home(TemplateView):
    template_name = "home.html"

# Create your views here.
class RegisterCreateView(CreateView):
    model = Register
    template_name = "register/register_form.html"
    fields = ['First_Name', 'Last_Name', 'Street', 'City', 'State', 'Country', 'Zip_Code', 'Phone_Number', 'Email', 'Date_of_Birth', 'Gender', 'Shirt_Size', 'Waiver', 'Emergency_Contact_First_Name', 'Emergency_Contact_Last_Name', 'Emergency_Contact_Phone_Number']
    success_url = reverse_lazy('register_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RegisterCreateView, self).form_valid(form)


class DonateView(CreateView):
  model = Donate
  template_name = "donate/donate_form.html"
  fields = ['first_name', 'last_name', 'email', 'phone_number', 'cardholders_name', 'credit_card_number', 'card_cvv', 'expiration_date']
  success_url = reverse_lazy('home')

  def form_valid(self, form):
      form.instance.user = self.request.user
      return super(DonateCreateView, self).form_valid(form)

class TeamCreateView(CreateView):
    model = Team
    template_name = "team/team_form.html"
    fields = ['name','description']
    success_url = reverse_lazy('team_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TeamCreateView, self).form_valid(form)

class TeamListView(ListView):
    model = Team
    template_name = "team/team_list.html"

class TeamDetailView(DetailView):
    model = Team
    template_name = 'team/team_detail.html'

class TeamUpdateView(UpdateView):
    model = Team
    template_name = 'team/team_form.html'
    fields = ['name', 'description']