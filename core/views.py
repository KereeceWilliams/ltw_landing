from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.exceptions import PermissionDenied

from .models import *
from .forms import *
from formtools.wizard.views import SessionWizardView

class Home(TemplateView):
    template_name = "home.html"

# Create your views here.
class RegisterCreateView(CreateView):
    model = Register
    template_name = "register/register_form.html"
    fields = ['Street', 'City', 'State', 'Country', 'Zip_Code', 'Phone_Number', 'Date_of_Birth', 'Gender', 'Shirt_Size', 'Emergency_Contact_First_Name', 'Emergency_Contact_Last_Name', 'Emergency_Contact_Phone_Number']
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RegisterCreateView, self).form_valid(form)

class RegisterCreateWizardView(SessionWizardView):
    form_list = [RegisterCreateWizardForm1]
    template_name = 'register/register_wizard_form.html'
    
    def done(self, form_list, **kwargs):
        register = Register()
        register.user = self.request.user
        register.Street = form_list[0].cleaned_data['Street']
        register.City = form_list[0].cleaned_data['City']
        register.State = form_list[0].cleaned_data['State']
        register.Country = form_list[0].cleaned_data['Country']
        register.Zip_Code = form_list[0].cleaned_data['Zip_Code']
        register.Phone_Number  = form_list[0].cleaned_data['Phone_Number']
        register.Date_of_Birth= form_list[0].cleaned_data['Date_of_Birth']
        register.Shirt_Size = form_list[0].cleaned_data['Shirt_Size']
        register.Emergency_Contact_First_Name = form_list[0].cleaned_data['Emergency_Contact_First_Name']
        register.Emergency_Contact_Last_Name = form_list[0].cleaned_data['Emergency_Contact_Last_Name']
        register.Emergency_Contact_Phone_Number = form_list[0].cleaned_data['Emergency_Contact_Phone_Number']
        register.save()
        return redirect('register_waiver')


class DonateView(CreateView):
  model = Donate
  template_name = "donate/donate_form.html"
  fields = ['first_name', 'last_name', 'email', 'phone_number']
  success_url = reverse_lazy('thank_you')

  def form_valid(self, form):
      form.instance.user = self.request.user
      return super(DonateView, self).form_valid(form)

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
    paginate_by = 5

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

class UserDeleteView(DeleteView):
    model = User
    slug_field = "username"
    template_name = 'user/user_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('logout')

    def get_object(self, *args, **kwargs):
        object = super(UserDeleteView, self).get_object(*args, **kwargs)
        if object != self.request.user:
            raise PermissionDenied()
        return object

    def delete(self, request, *args, **kwargs):
        user = super(UserDeleteView, self).get_object(*args)
        user.is_active = False
        user.save()
        return redirect(self.get_success_url())

class SearchTeamListView(TeamListView):
    def get_queryset(self):
        incoming_query_string = self.request.GET.get('query','')
        return Team.objects.filter(name__icontains=incoming_query_string)

class VendorCreateView(CreateView):
    model = Vendor
    template_name = "vendor/vendor_form.html"
    fields = ['First_Name', 'Last_Name', 'Street', 'City', 'State', 'Country', 'Zip_Code', 'Phone_Number', 'Email']
    success_url = reverse_lazy('success')

class VolunteerCreateView(CreateView):
    model = Volunteer
    template_name = "volunteer/volunteer_form.html"
    fields = ['First_Name', 'Last_Name', 'Street', 'City', 'State', 'Country', 'Zip_Code', 'Phone_Number', 'Email','Activity']
    success_url = reverse_lazy('success')

class Success(TemplateView):
  template_name = "success.html"

class Contact_Us(CreateView):
    model = Contact_Us
    template_name = "contact_us/contact_us.html"
    fields = ['name', 'email', 'phone_number', 'topic', 'description']
    success_url = reverse_lazy('success')

class About_Us(TemplateView):
  template_name = "about_us.html"

class RegisterWaiverCreateView(CreateView):
    model = RegisterWaiver
    template_name = "register/register_waiver_form.html"
    fields = ['waiver']
    success_url = reverse_lazy('success')
    
class Thank_You(TemplateView):
    template_name = "thank_you.html"
    
class FAQ(TemplateView):
    template_name = "faq.html"