from django.urls import path
from . import views 
from .views import IndexView, TestView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
app_name= 'core'

urlpatterns = [
  path('', login_required(IndexView.as_view()), name='index'),
  path('test/', login_required(TestView.as_view()), name='test'),
]




