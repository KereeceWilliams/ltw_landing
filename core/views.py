from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied
from .models import *

class Home(TemplateView):
    template_name = "home.html"

# Create your views here.
class RegisterCreateView(CreateView):
    model = Register
    template_name = "register/register_form.html"
    fields = ['First_Name', 'Last_Name', 'Street', 'City', 'State', 'Country', 'Zip_Code', 'Phone_Number', 'Email', 'Date_of_Birth', 'Gender', 'Shirt_Size', 'Waiver', 'Emergency_Contact_First_Name', 'Emergency_Contact_Last_Name', 'Emergency_Contact_Phone_Number', 'cardholders_name', 'credit_card_number', 'card_cvv', 'expiration_date']
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

    def get_context_data(self, **kwargs):
      context = super(TeamDetailView, self).get_context_data(**kwargs)
      team = Team.objects.get(id=self.kwargs['pk'])
      members = Member.objects.filter(team=team)
      context['members'] = members
      return context

class TeamUpdateView(UpdateView):
    model = Team
    template_name = 'team/team_form.html'
    fields = ['name', 'description']

    def get_object(self, *args, **kwargs):
        object = super(TeamUpdateView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'team/team_confirm_delete.html'
    success_url = reverse_lazy('team_list')

    def get_object(self, *args, **kwargs):
        object = super(TeamDeleteView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

class MemberCreateView(CreateView):
    model = Member
    template_name = "member/member_form.html"
    fields = ['name']

    def get_success_url(self):
        return self.object.team.get_absolute_url()

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.team = Team.objects.get(id=self.kwargs['pk'])
        return super(MemberCreateView, self).form_valid(form)

class MemberUpdateView(UpdateView):
    model = Member
    pk_url_kwarg = 'member_pk'
    template_name = 'member/member_form.html'
    fields = ['name']

    def get_success_url(self):
        return self.object.team.get_absolute_url()

    def get_object(self, *args, **kwargs):
        object = super(MemberUpdateView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
          raise PermissionDenied()
        return object

class MemberDeleteView(DeleteView):
    model = Member
    pk_url_kwarg = 'member_pk'
    template_name = 'member/member_confirm_delete.html'

    def get_success_url(self):
        return self.object.team.get_absolute_url()

    def get_object(self, *args, **kwargs):
        object = super(MemberDeleteView, self).get_object(*args, **kwargs)
        if object.user != self.request.user:
            raise PermissionDenied()
        return object

class UserDetailView(DetailView):
    model = User
    slug_field = 'username'
    template_name = 'user/user_detail.html'
    context_object_name = 'user_in_view'

    def get_context_data(self, **kwargs):
      context = super(UserDetailView, self).get_context_data(**kwargs)
      user_in_view = User.objects.get(username=self.kwargs['slug'])
      team = Team.objects.filter(user=user_in_view)
      context['team'] = team
      member = Member.objects.filter(user=user_in_view)
      context['member'] = member
      return context

class UserUpdateView(UpdateView):
    model = User
    slug_field = "username"
    template_name = "user/user_form.html"
    fields = ['email', 'first_name', 'last_name']
    
    def get_success_url(self):
        return reverse('user_detail', args=[self.request.user.username])

    def get_object(self, *args, **kwargs):
        object = super(UserUpdateView, self).get_object(*args, **kwargs)
        if object != self.request.user:
            raise PermissionDenied()
        return object