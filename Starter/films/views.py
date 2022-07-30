from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from films.forms import RegisterForm


# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"


class Login(LoginView):
    template_name = "registration/login.html"


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)


def check_username(request):
    username = request.POST.get("username")
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse(
            '<div id="username-error" style="color: red;">This username already exists</div>'
        )
    return HttpResponse('<div id="username-error" style="color: green;">This username is available')
