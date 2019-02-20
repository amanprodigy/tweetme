from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django import forms
from django.forms.utils import ErrorList
from django.http import HttpResponseRedirect

from braces.views import AnonymousRequiredMixin

from .forms import LoginForm, RegisterForm
from .models import User


class UserLogin(AnonymousRequiredMixin, FormView):
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')
    form_class = LoginForm

    def form_valid(self, form):
        ''' Authenticate user through a login form '''

        # redirect if already authenticated
        redirect_to = self.request.POST.get('next', '')
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(redirect_to)

        cd = form.cleaned_data
        user = authenticate(self.request,
                            username=cd['username'],
                            password=cd['password'])
        if user is not None:
            login(self.request, user)
            if redirect_to:
                # https://stackoverflow.com/questions/35796195/how-to-redirect-to-previous-page-in-django-after-post-request/35796559
                return redirect(redirect_to)
            return super(UserLogin, self).form_valid(form)
        else:
            # failed to login
            form._errors[forms.forms.NON_FIELD_ERRORS] = \
                ErrorList(['Please check email or password'])
            return super(UserLogin, self).form_invalid(form)


class Register(AnonymousRequiredMixin, FormView):
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')
    form_class = RegisterForm

    def form_valid(self, form):
        ''' Register a new user in the system '''

        cd = form.cleaned_data
        user = User.objects.create_user(
            cd['username'],
            cd['email'],
            cd['password']
        )
        if user is not None:
            login(self.request, user)
            redirect(reverse_lazy('home'))
            return super(Register, self).form_valid(form)
        else:
            # failed to login
            form._errors[forms.forms.NON_FIELD_ERRORS] = \
                ErrorList(['Failed to register'])
            return super(Register, self).form_invalid(form)


# FIXME: Deprecated
def user_login(request):
    login_error = None
    form = LoginForm(request.POST or None)
    if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(request,
                            username=cd['username'],
                            password=cd['password'])
        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            login_error = 'Incorrect username or password'
    context = {'form': form, 'login_error': login_error}
    return render(request, 'users/login.html', context)


# FIXME: Deprecated
def user_logout(request):
    logout(request)
    return redirect(reverse('home'))
