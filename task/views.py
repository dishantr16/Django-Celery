from celerytask.task.form import GenerateRandomUserForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import FormView

# Create your views here.
from .form import GenerateRandomUserForm
from .task import create_random_user_accounts


class UserListView(ListView):
    template_name = 'task/user_list.html'
    model = User


class GenerateRandomUserView(FormView):
    template_name = 'task/generate_random_user.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'we are generating random user')

        return redirect('users_list')
