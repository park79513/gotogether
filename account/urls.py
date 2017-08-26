from django.conf.urls import url
from account.views import RegisterUserView
from django.contrib.auth.views import LogoutView

from account.views import RegisterUserView, LoginUserView, DashboardView

urlpatterns = [
    url(r'^register/$', view = RegisterUserView.as_view(), name = 'register'),
    url(r'^login/$', LoginUserView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),
]
