"""controlador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from projects import views

urlpatterns = [
    
    url(r'^$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^reset/$',
                   auth_views.PasswordResetView.as_view(
                                                        template_name='password_reset.html',
                                                        email_template_name='password_reset_email.html',
                                                        subject_template_name='password_reset_subject.txt'
                                                        ),
                   name='password_reset'),
    url(r'^reset/done/$',
                   auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
                   name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                   auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
                   name='password_reset_confirm'),
    url(r'^reset/complete/$',
                   auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
                   name='password_reset_complete'),
    
    url(r'^projects/$', views.ProjectListView.as_view(), name='home'),
    url(r'^new_project/$', views.new_project, name='new_project'),
    url(r'^modules/(?P<pk>\d+)/$', views.project_modules, name='project_modules'),
    url(r'^modules/(?P<pk>\d+)/new/$', views.new_module, name='new_module'),
    url(r'^modules/(?P<pk>\d+)/activities/(?P<module_pk>\d+)/$', views.module_activities, name='module_activities'),
    url(r'^activities/(?P<pk>\d+)/new/$', views.new_activity, name='new_activity'),
    url(r'^activities/(?P<pk>\d+)/first_activity/$', views.first_activity, name='first_activity'),
    url(r'^activities/(?P<pk>\d+)/last_activity/$', views.last_activity, name='last_activity'),

    url(r'^admin/', admin.site.urls),
]
