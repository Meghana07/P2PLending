from django.conf.urls import url
from UserApp import views
from django.urls import path

app_name = 'UserApp'

urlpatterns = [
	path('register/',views.register, name='register'),
	path('user_login/',views.user_login,name='user_login'),
	path('profile/',views.profile, name='profile'),
	path('changepwd/',views.changepwd, name='changepwd'),
	]
