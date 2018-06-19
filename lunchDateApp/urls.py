from django.urls import path

from . import views
from .controllers import user_controller

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('landing_admin', views.landing_admin, name='landing_admin'),
    path('landing_member', views.landing_member, name='landing_member'),
    path('billing', views.billing, name='billing'),
    path('session_detail', views.session_detail, name='session_detail'),
    path('member_status', views.member_status, name='member_status'),
    path('set_up_new_user_login', user_controller.create_new_user, name='set_up_new_user_login'),
    path('set_up_new_user_detail', user_controller.new_user_detail, name='set_up_new_user_detail'),
]