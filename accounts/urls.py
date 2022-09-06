from django.urls import path
from .views import SignupView, SignupsuccessView, profileView
from django.contrib.auth import views as auth_views
from .froms import AuthenticationForm
from django.contrib.auth.decorators import login_required, permission_required
from .views import UserView, UserUpdateView
app_name= 'accounts'

urlpatterns = [
  
 path('signup/', SignupView.as_view(), name="signup"),
 path('signup_success/', SignupsuccessView.as_view(), name="signup_success"),
 path('login/', auth_views.LoginView.as_view(template_name="login.html",form_class=AuthenticationForm,),name="login",),
 path('logout/' , auth_views.LogoutView.as_view(), name= 'logout' ),
 path('userdetail/', login_required(UserView.as_view()), name="userdetail"),
 path('edituser/<int:pk>/', login_required(UserUpdateView.as_view()), name="edituser"),
 path('profile/', login_required(profileView.as_view()), name="profile"),
]




