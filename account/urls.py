from django.urls import path

from account import views
app_name = 'account'
urlpatterns = [
    path('logout' , views.logout_view , name='logout' ),
    path('login', views.login_view , name='login' ),
    path('register', views.register_view  , name='register' ),

]