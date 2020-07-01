from django.conf.urls import url

from Two import views

app_name ='two'
urlpatterns = [
    url(r'^hello/',views.hello,name = 'hello'),
    url(r'^login/', views.login, name='login'),
    url(r'^mine/', views.mine, name='mine'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^register/', views.register, name='register'),
    url(r'^stslogin/', views.stslogin, name='stslogin'),

]