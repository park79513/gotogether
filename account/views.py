
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden, HttpResponse


from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView

from account.forms import RegisterUserForm, LoginForm


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = "account/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseForbidden()

        return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        return HttpResponse('User registered')


class LoginUserView(LoginView):
    form_class = LoginForm
    template_name = "account/login.html"
    redirect_authenticated_user = True
    success_url = '//'


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'account/dashboard.html'

    def dispatch(self, request, *args, **kwargs):
        return super(DashboardView, self).dispatch(request, *args, **kwargs)
# Create your views here.
