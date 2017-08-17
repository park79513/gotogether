from django.conf.urls import url
from account.views import RegisterUserView


urlpatterns = [
    url(r'^register/$', view = RegisterUserView.as_view(), name = 'register')
]
