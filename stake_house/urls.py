import main_app.views as main_app
import adminApp.views as admin_app
"""stake_house URL Configuration

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

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^my_admin/$', admin_app.admin_page),
    url(r'^my_admin/view/(\d+)/$', admin_app.view_user, name='view_user'),
    url(r'^my_admin/delete/(\d+)/$', admin_app.delete_user, name='delete_user'),
    url(r'^my_admin/create_user/$', admin_app.create_user, name='create_user'),
    url(r'^my_admin/update_user/(\d+)/$', admin_app.update_user, name='update_user'),



    url(r'^$', main_app.main_page),
    #url(r'^user/login/$', main_app.login),
    #url(r'^user/logout/$', main_app.logout),
    #url(r'^user/register/$', main_app.register),

    url(r'^stakes/$', main_app.stakes),
    url(r'^contacts/$', main_app.contacts),
    url(r'^galary/$', main_app.galary),
    url(r'^menu/$', main_app.menu),
    url(r'^news/$', main_app.news),
    url(r'^reviews/$', main_app.reviews),
]
