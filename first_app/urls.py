from django.urls import path
from django.conf.urls import *
from first_app.views import *
from . import views
import first_app
urlpatterns = [

    # path('/',  views.hello, name = 'hello'),
    path('viewpolls', views.PollList.as_view(), name = 'poll_list'),
    path('index', TemplateView.as_view(template_name = 'index.html'), name = 'home'),
    path('login', views.login, name = 'login'),
    path('connection', views.formview, name = 'connection'),
]
